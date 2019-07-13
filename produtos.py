class Produtos:
	def __init__(self):
		self.quantidade = 0
		self.total = 0
		self.products = []
	def __add__(self,prod):
		self.quantidade += prod.quantidade
		self.total += prod.product[prod.valor]
		self.push(prod)
		return self
	def push(self,prod):
		self.products.append(prod)