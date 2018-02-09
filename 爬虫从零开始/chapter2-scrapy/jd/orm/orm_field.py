class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name  # 字段名
        self.column_type = column_type  # 字段数据类型
        self.primary_key = primary_key  # 是否是主键
        self.default = default  # 有无默认值

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self,
                 name=None,
                 column_type='VARCHAR(255)',
                 primary_key=False,
                 default=None):
        super(StringField, self).__init__(name, column_type, primary_key,
                                          default)


class IntField(Field):
    def __init__(self,
                 name=None,
                 column_type='INT',
                 primary_key=False,
                 default=0):
        super(IntField, self).__init__(name, column_type, primary_key, default)


class DateField(Field):
    def __init__(self,
                 name=None,
                 column_type='DATETIME',
                 primary_key=False,
                 default=0):
        super(DateField, self).__init__(name, column_type, primary_key,
                                        default)
