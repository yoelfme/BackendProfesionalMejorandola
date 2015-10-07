var express = require('express');
var swig = require('swig');
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var session = require('express-session');
var RedisStore = require('connect-redis')(session);

var app = express();

// Configuracion para mostrar vistas
app.engine('html', swig.renderFile);
app.set('view engine', 'html')
app.set('views', './app/views')

// Configurando post, cookies y sesiones
app.use(logger('dev'));
app.use(cookieParser())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.use(session({
    sotre: new RedisStore({}),
    secret: 'lolcatz' 
}));

app.get('/', function (req, res) {
    res.render('home');
});

app.get('/app', function (req, res) {
    res.render('app', {
        user: req.session.user
    });
})

app.post('/log-in', function(req, res){
    req.session.user = req.body.username;

    res.redirect('/app')
});

var server = app.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log('App listening at http://%s:%s', host, port);
})
