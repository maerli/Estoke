import db
from produtos import Produtos
from produto import Produto
from caixa import Caixa
from fornecedor import Fornecedor

database = db.DB('vendas.db')

Produto.table = 'produtos'
Produto.database = database
a = Produto({'nome':'manga','valor':100})
b = Produto({'nome':'maracuja','valor':200})
c = Produto({'nome':'macarrao','valor':300})
print(a.load())
venda = a + b + c


caixa = Caixa()
#caixa.venda(venda)
print(venda.total)

#db1.execute("create table produdos (id int(10),nome varchar(20),valor int(10))")
#db1.execute("insert into produdos values(1,'manga',100)")
#db1.commit()

forn = Fornecedor(None)
Fornecedor.table = 'fornecedores'
Fornecedor.database = database
print(forn.load(1))
