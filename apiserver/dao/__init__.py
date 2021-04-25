import pymysql
from pymysql.cursors import DictCursor

CONFIG = {
    'host':'47.101.137.66',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'school',
    'charset':'utf8',
    'cursorclass':DictCursor
}
class DB():
    def __init__(self):
        self.conn = pymysql.Connect(**CONFIG)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()


    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None


class BaseDao():
    def __init__(self):
        self.db = DB()

    def find_all(self,table,where=None,*whereArgs):
        sql = "select * from %s"%table
        if where:
            sql += where
        with self.db as c:
            c.execute(sql,whereArgs)
            result = list(c.fetchall())
        return result