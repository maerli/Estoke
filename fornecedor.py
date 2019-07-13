from db import DBProduct
from db import DB
class Fornecedor:
	fakedb  = DBProduct()
	table = None
	database = None
	def __init__(self,forn):
		self.forn = forn
	def create_forn(self):
		sql = "CREATE TABLE fornecedores (id int(10),nome varchar(100),endereco varchar(100))"
		db2 = database.execute(sql)
	def insert(self):
		sql = Fornecedor.fakedb.insert(Fornecedor.table,self.forn)
		Fornecedor.database.execute(sql).commit()
	def show(self,fields = ('*')):
		sql = Fornecedor.fakedb.select(Fornecedor.table,fields)
		db1 = Fornecedor.database.execute(sql)
		rows = db1.fetchall()
		for row in rows:
			print(row)
	def load(self,id = None,fields=('*')):
		wh = ' where id='+str(id)
		if id == None: wh = ''
		sql = Fornecedor.fakedb.select(Fornecedor.table,fields) + wh
		return Fornecedor.database.execute(sql).fetchall()
