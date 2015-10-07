var express = require('express'),
    swig = require('swig');

var app = express();

// Configuracion para mostrar vistas
app.engine('html', swig.renderFile);
app.set('view engine', 'html')
app.set('views', './app/views')

app.get('/', function(req, res){
    res.render('home');
});

app.post('/log-in', function(req, res){
    res.render('Quien eres?');
});

var server = app.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log('App listening at http://%s:%s', host, port);
})
