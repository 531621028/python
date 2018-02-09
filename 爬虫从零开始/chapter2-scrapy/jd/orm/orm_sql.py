# coding:utf-8

from pymysqlpool import ConnectionPool 


def create_pool(**kw):

    global __pool
    __pool = ConnectionPool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),  # 默认编码为utf-8
        autocommit=kw.get('autocommit', True),  # 自动提交事务
        maxsize=kw.get('maxsize', 10),  # 池中最多有10个链接对象
        minsize=kw.get('minsize', 1),
    )


async def select(sql, args, size=None):  # size可以决定取几条

    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        # 用参数替换而非字符串拼接可以防止sql注入
        await cur.execute(sql.replace('?', '%s'), args or ())  
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        return rs


async def execute(sql, args):
    global __pool
    try:
        with (await __pool) as conn:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
    except BaseException as e:
        raise e
    return affected
