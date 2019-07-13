from db import DBProduct,DB
class User:
  table = None
  database = None
  fkdb = DBProduct()
  def __init__(self,user = None):
      self.user = user
  def create_table(self):
      User.database.execute('create table users()')
  def insert(self):
      sql = User.fkdb.insert(User.table,self.user)
      User.database.execute(sql)
      User.database.commit()
  def load(self,id = None,fields=('*')):
      wh = ' where id='+str(id)
      if id == None: wh = ''
      sql = User.fkdb.select(User.table,fields) + wh
      return User.database.execute(sql).fetchall()
