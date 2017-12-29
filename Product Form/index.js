var express = require('express');
var mysql = require('mysql');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: true })); 

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'store_db'
})

connection.connect(function(error){
    if(!!error)
    {
        console.log('Error');
    }else{
        console.log('connected');
    }
})

app.get('/', function(req, res){
    res.sendfile('form.html');
    connection.query("SELECT * FROM product_table", function(error,rows,fields){
        if(!!error)
        {
            console.log('Error in the query');
        }else{
            console.log('success');
            console.log(rows);
        }
    });
})

app.post('/myaction', function(req, res) {
    console.log('req.body');
    console.log(req.body);
    res.write('You sent the code "' + req.body.code+'".\n');
    res.write('You sent the name "' + req.body.name+'".\n');
    res.write('You sent the size "' + req.body.size+'".\n');
    res.write('You sent the price "' + req.body.price+'".\n');
    res.end()

    connection.query("Insert into product_table (product_code,product_name,product_size,product_price) VALUES ('"+req.body.code+"','"+req.body.name+"','"+req.body.size+"','"+req.body.price+"')",function(err, result)      
    {                                                      
      if (err)
         throw err;
    });
    });
app.listen(1337);