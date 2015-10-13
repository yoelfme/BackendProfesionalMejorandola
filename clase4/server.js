var express = require('express');
var swig = require('swig');
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var session = require('express-session');
var RedisStore = require('connect-redis')(session);
var _ = require('underscore');
var passport = require('passport');

var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);
var users = [];

// Configuracion para mostrar vistas
app.engine('html', swig.renderFile);
app.set('view engine', 'html')
app.set('views', './app/views')

// Configurando post, cookies
app.use(logger('dev'));
app.use(cookieParser())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// Configurando sesiones
app.use(session({
    sotre: new RedisStore({}),
    secret: 'lolcatz' 
}));

// Configurar passport
app.use(passport.initialize());
app.use(passport.session());

// Configurando archivos estaticos
app.use(express.static('public'));

// Agregando controladores
var homeController = require('./app/controllers/home');
var appController = require('./app/controllers/app');

homeController(app, users);
appController(app, users);

// Agregando conexiones
var twitterConnection = require('./app/connections/twitter');

twitterConnection(app);

server.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log('App listening at http://%s:%s', host, port);
})
