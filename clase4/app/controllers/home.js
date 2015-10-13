var _ = require('underscore');

var homeController = function (app, users) {
    console.log('homeController esta cargado');

    var isLoggedIn = function(req, res, next) {
        if(req.session.user) {
            res.redirect('/app');
        }

        next();
    }

    app.get('/', isLoggedIn, function (req, res) {
        res.render('home');
    });

    app.post('/log-in', function(req, res){
        users.push(req.body.username);
        req.session.user = req.body.username;

        io.emit('log-in', {
            username: req.session.user
        })

        res.redirect('/app')
    });

    app.get('/log-out', function (req, res) {
        users = _.without(users, req.session.user);

        io.emit('log-out', {
            username: req.session.user
        });

        req.session.destroy();
        res.redirect('/');
    });
};

module.exports = homeController;