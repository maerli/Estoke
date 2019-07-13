class Caixa:
	def __init__(self):
		pass
	def venda(self,produtos):
		for produto in produtos.products:
			produto.todb()