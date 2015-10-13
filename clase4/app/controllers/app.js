var appController = function (app, users) {
    console.log('appController esta cargado');

    var isntLoggedIn = function(req, res, next) {
        if (!req.session.passport.user){
            res.redirect('/');
            return;
        }

        next();
    }    

    app.get('/app', isntLoggedIn, function (req, res) {
        res.render('app', {
            user: req.session.passport.user,
            users: users
        });
    })
};

module.exports = appController;