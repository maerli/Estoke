//javascript
const express = require('express')
const exec= require('child_process').exec
const fetch = require('node-fetch')
const crypto = require('crypto')
const sqlite3 = require('sqlite3').verbose()
const datetime = require('node-datetime')

function dbinsert(db,table,object,close = true){
  var keys = '(' + Object.keys(object).join(',')+')'
  var values = Object.values(object)
  var inter = values.map(_=> '?').join(',')
  var sql = 'insert into '+table+' '+keys+' values('+inter+')'
  db.run(sql,values,(err)=>console.log(err))
  if(close)  db.close()
}

const app = express()
app.use(express.json())
app.use(express.static('public'))
app.use(express.static('node_modules/bootstrap/dist/css'))
app.use(express.static('node_modules/bootstrap/js/dist'))
app.use(express.static('node_modules/jquery/dist'))


app.get('/',function(request,respose){
  respose.send('Hello, World!')
})

app.get('/connect',function(request,respose){
  respose.json({connect:true})
})
app.get('/produtos',function(request,response){
  var content = request.body
  var db = new sqlite3.Database('vendas.db')
  db.all('select * from produtos order by id desc',function(err,rows){
    if(err){
      response.json({err})
    }else{
      response.json(rows)
    }
  })
  db.close()
})
app.post('/produtos',function(request,response){
  var content = request.body
  var db = new sqlite3.Database('vendas.db')
  dbinsert(db,'produtos',content)
  response.json(content)
})

app.post('/send',function(request,response){
  console.log(request.body)
  response.json({data:true})
  E('python3 produto.py post '+JSON.stringify(request.body).replace(/\"/g,"\\\""))
})

app.get('/fornecedores',function(request,response){
  var db = new sqlite3.Database('vendas.db')
  db.all('select * from fornecedores order by id desc',function(err,rows){
    if(err){
      response.json({err})
    }else{
      response.json(rows)
    }
  })
  db.close()
})
app.post('/fornecedores',function(request,response){
  var content = request.body
  var db = new sqlite3.Database('vendas.db')
  var keys = Object.keys(content)
  var values = Object.values(content)
  db.run(
    'insert into fornecedores ('+
    keys.join(',')+
    ') values('+
    keys.map(k => '?').join(',')+
    ')'
    ,values,
    function(err){
      console.log(err)
    })
  db.close()
  response.json(content)
})

app.post('/user',function(request,response){
  var body = request.body
  if(body.senha){
    var hash = crypto.createHash('md5').update(body.senha).digest('hex')
    body.senha = hash
  }
  var db = new sqlite3.Database('vendas.db')
  db.run('insert into users (nome,senha) values(?,?)',[body.nome,body.senha],function(err){
    console.log(err)
  })
  //ok
  response.json(request.body)
})

app.post('/isuser',function(request,response){
  var nome = request.body['nome']
  var senha = crypto.createHash('md5').update(request.body['senha']).digest('hex')
  var db = new sqlite3.Database('vendas.db')
  x = db.all('select * from users where nome=? and senha=?',[nome,senha],function(err,row){
    if(err){
    console.log(err)
      response.send('err')
    }
    console.log(row.length)
    response.json(row)
  })
  //response.json()
  db.close()
})

app.post('/caixa',function(request,response){
var db = new sqlite3.Database('vendas.db')
  var content = request.body
  var head = content.head
  console.log(head.recebido)
  var data = content.data
  db.run('insert into lotes (valor,user,data,recebido,troco) values(?,?,?,?,?)',
  [head.valor,head.user,datetime.create().format('d/m/Y à\s H:M:S'),head.recebido,head.troco],function(err){
    console.log(err)
  })
  var lote;
  db.each('select id from lotes order by id desc limit 1',function(err,row){
    var id = row.id
    for(produto of data){
      delete produto.id
      produto.lote = id
      dbinsert(db,'venda',produto,false)
    }
    db.close()
  })
  response.json(content)
})

app.get('/vendas/:user',function(request,response){
  var user = request.params.user
  var db = new sqlite3.Database('vendas.db')
  db.all('select * from lotes where user=? order by id desc',[user],function(err,rows){
    if(err){
      response.json(err)
    }else{
      response.json(rows)
    }
  })
  db.close()
})

app.get('/lotes/:lote',function(request,response){
  var lote = request.params.lote
  var db = new sqlite3.Database('vendas.db')
  db.each('select valor from lotes where id=? limit 1',[lote],function(err,row){
  var valor = row.valor
  db.all('select * from venda where lote=?',[lote],function(err,rows){
      if(err){
        respose.json(err)
      }else {
        response.json({valor,rows})
      }
    })
    db.close()
  })
})

app.get('/search/:q',(request,response)=>{
  var q = request.params.q
  var db = new sqlite3.Database('vendas.db')
  db.all('select * from produtos where nome like ? or id=? order by nome asc',['%'+q+'%',q],function(err,rows){
    if(err){
      response.json([{err}])
    }else{
      response.json(rows)
    }
  })
})

app.listen(80,'0.0.0.0',function(){
  console.log('Estoke server running!')
})
