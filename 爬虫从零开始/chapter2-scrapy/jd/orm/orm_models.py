# coding:utf-8
from orm_sql import select, execute
from orm_field import Field


class ModelMetaclass(type):

    # 元类必须实现__new__方法，当一个类指定通过某元类来创建，那么就会调用该元类的__new__方法
    # 该方法接收4个参数
    # cls为当前准备创建的类的对象 
    # name为类的名字，创建User类，则name便是User
    # bases类继承的父类集合,创建User类，则base便是Model
    # attrs为类的属性/方法集合，创建User类，则attrs便是一个包含User类属性的dict
    def __new__(cls, name, bases, attrs):
        # 排除Model类本身:
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # 获取table名称:
        tableName = attrs.get('__table__', None) or name
        print('found model: %s (table: %s)' % (name, tableName))
        # 获取所有的Field和主键名:
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键:
                    if primaryKey:
                        raise RuntimeError(
                            'Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k) # 从attrs删除类中的所有类属性
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (
            primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (
            tableName, ', '.join(escaped_fields), primaryKey,
            create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
            tableName, ', '.join(
                map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)),
            primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName,
                                                                 primaryKey)
        return type.__new__(cls, name, bases, attrs)


# 让Model继承dict,主要是为了具备dict所有的功能，如get方法
# metaclass指定了Model类的元类为ModelMetaClass
class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    # 实现__getattr__与__setattr__方法，可以使引用属性像引用普通字段一样  如self['id']

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 貌似有点多次一举
    def getValue(self, key):
        value = getattr(self, key, None)
        return value

    # 取默认值，上面字段类不是有一个默认值属性嘛，默认值也可以是函数
    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(
                    field.default) else field.default
                setattr(self, key, value)
        return value

# 一步异步，处处异步，所以这些方法都必须是一个协程
# 下面 self.__mappings__,self.__insert__等变量据是根据对应表的字段不同，而动态创建

    def save(self):
        args = list(map(self.getValueOrDefault, self.__mappings__))
        return execute(self.__insert__, args)

    def remove(self):
        args = []
        args.append(self[self.__primaryKey__])
        print(self.__delete__)
        return execute(self.__delete__, args)

    def update(self, **kw):
        print("enter update")
        args = []
        for key in kw:
            if key not in self.__fields__:
                raise RuntimeError("field not found")
        for key in self.__fields__:
            if key in kw:
                args.append(kw[key])
            else:
                args.append(getattr(self, key, None))
        args.append(getattr(self, self.__primaryKey__))
        return execute(self.__update__, args)

    # 类方法
    @classmethod
    async def find(cls, pk):
        rs = select('%s where `%s`=?' %
                               (cls.__select__, cls.__primaryKey__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])  # 返回的是一个实例对象引用

    @classmethod
    def findAll(cls, where=None, args=None):
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        rs = select(' '.join(sql), args)
        return [cls(**r) for r in rs]
