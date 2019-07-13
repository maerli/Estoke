from flask import Flask,request,jsonify
from flask import Response
import json
from produto import Produto
from fornecedor import Fornecedor
from db import DB
from user import User

db = DB('vendas.db')
Produto.table = 'produtos'
Produto.database = db

Fornecedor.table = 'fornecedores'
Fornecedor.database = db

User.table = 'users'
User.database = db

app = Flask(__name__)
@app.route("/produtos")
def hello():
    content = request.json
    p = Produto(None)
    return jsonify(p.load())
@app.route("/fornecedores")
def fornecedores():
    content = request.json
    f = Fornecedor(None)
    return jsonify(f.load())
@app.route("/user",methods=['POST','GET'])
def nuser():
    u = User()
    if(request.method == 'GET'):
        return jsonify(u.load())
    if(request.method == 'POST'):
        content = request.json
        print(content)
        u.user = content
        u.insert()
        return jsonify(content)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
