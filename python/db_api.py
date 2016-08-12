#!/usr/bin/env python

try:
    import MySQLdb as DB
except ImportError:
    print "Please install MySQLdb module"

class db(object):
    def __init__(self, user='root', host='127.0.0.1', passwd='root', db='test1'):
        self._db = DB.connect(user=user,
                              host=host,
                              passwd=passwd,
                              db=db)
        self._cursor = self._db.cursor()
        self.table_name = 't1'

    def query(self, query, gap=25):
        ''' Send a MySQL query to the database'''
        self._cursor.execute(query)
        results = self._cursor.fetchall()
        return results

_db = db()

result = _db.query("select * from " + _db.table_name)
print result

