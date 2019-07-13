from db import DBProduct
from produtos import Produtos
class Produto:
	fakedb = DBProduct()
	table = None
	database = None
	def __init__(self,product):
		self.quantidade = 0
		self.product = product
		self.valor = 'valor'
	def __add__(self,product):
		if(type(product) == Produto):
			prod = Produtos()
			prod.quantidade = self.quantidade + product.quantidade
			prod.total += self.product[self.valor] + product.product[self.valor]
			prod.push(self)
			prod.push(product)
			return prod
	def todb(self):
		sql = Produto.fakedb.insert(Produto.table,self.product)
		Produto.database.execute(sql)
		Produto.database.commit()
	def load(self,id = None,fields=('*')):
		wh = ' where id='+str(id)
		if id == None: wh = ''
		sql = Produto.fakedb.select(Produto.table,fields) + wh
		return Produto.database.execute(sql).fetchall()
