const exec = require('child_process').exec
const ip = require('ip')
console.dir(ip.address())
exec('firefox http:'+ip.address()+':3000',function(err,stdout,stderr){console.log(err,stdout)})
