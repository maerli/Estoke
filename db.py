import sqlite3
class DB:
    def __init__(self,db):
        '''
            /*Documentation
            DB(database_path)
        '''
        self.connection = sqlite3.connect(db,check_same_thread=False)
    def execute(self,sql):
        '''
            DB.execute(sql_string)
        '''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.cursor = cursor
        return cursor
    def commit(self):
        self.connection.commit()
    def close(self):
        self.connection.close()

class DBProduct:
	def __init__(self):
		pass
	def insert(self,table,object):
		keys = []
		values = []
		for key in object:
			keys.append(str(key))
			values.append("'"+str(object[key])+"'")
		sql = "INSERT INTO "+table+" ("+(','.join(keys))+") VALUES("+(','.join(values))+");"
		return sql
	def print(self):
		pass
	def select(self,table,_fields):
		values = []
		for _field in _fields:
			values.append(str(_field))
		sql = "SELECT  "+(','.join(values))+" FROM "+table
		return sql
