var express = require('express');
var swig = require('swig');
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var session = require('express-session');
var RedisStore = require('connect-redis')(session);
var _ = require('underscore');

var app = express();
var users = [];

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

// Configurando middleware

var isntLoggedIn = function(req, res, next) {
    if (!req.session.user){
        res.redirect('/');
        return;
    }

    next();
}

var isLoggedIn = function(req, res, next) {
    if(req.session.user) {
        res.redirect('/app');
    }

    next();
}

app.get('/', isLoggedIn, function (req, res) {
    res.render('home');
});

app.get('/app', isntLoggedIn, function (req, res) {
    res.render('app', {
        user: req.session.user,
        users: users
    });
})

app.post('/log-in', function(req, res){
    users.push(req.body.username);
    req.session.user = req.body.username;

    res.redirect('/app')
});

app.get('/log-out', function (req, res) {
    users = _.without(users, req.session.user);

    req.session.destroy();
    res.redirect('/');
});

var server = app.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log('App listening at http://%s:%s', host, port);
})
