var User = require('../models/user');
var Post = require('../models/post');

var appController = function (app, users) {
    console.log('appController esta cargado');

    var isntLoggedIn = function(req, res, next) {
        if (!req.session.passport.user){
            res.redirect('/');
            return;
        }

        next();
    };

    var getUser = function (req, res, next) {
        User.findOne({username: req.session.passport.user.username}, function (err, user) {
            req.user = user;

            next();
        });
    };

    app.get('/app', isntLoggedIn, function (req, res) {
        res.render('app', {
            user: req.session.passport.user,
            users: users
        });
    });

    app.post('/app/create-post', isntLoggedIn, getUser, function (req, res) {
        var post = new Post({
            content: req.body.content,
            user: req.user
        });

        post.save(function (err) {
            debugger;
            if (err) {
                res.send(500, err);
            }

            res.redirect('/app');
        });

    });
};

module.exports = appController;