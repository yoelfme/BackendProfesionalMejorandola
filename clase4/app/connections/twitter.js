var passport = require('passport');
var passportTwitter = require('passport-twitter');
var TwitterStrategy = passportTwitter.Strategy;

var twitterConnection = function (app) {
    console.log('twitterConnection ready');

    passport.use(new TwitterStrategy({
            consumerKey: 'DSFDP9vemH6hmzhoBvRrxCr1E',
            consumerSecret: 'eO6fBWU5jEiDQ0j54yFzhhgV7kEK0ctqNAwpkE6NIhb7yDDbRu',
            callbackURL: 'http://127.0.0.1:3000/auth/twitter/callback'
        },
        function(token, tokenSecret, profile, cb) {
            // In this example, the user's Twitter profile is supplied as the user
            // record.  In a production-quality application, the Twitter profile should
            // be associated with a user record in the application's database, which
            // allows for account linking and authentication with other identity
            // providers.
            return cb(null, profile);
        }));

    app.get('/auth/twitter', passport.authenticate('twitter'));

    app.get('/auth/twitter/callback', 
        passport.authenticate('twitter', { failureRedirect: '/' }),
        function(req, res) {
            res.redirect('/app');
        });
};

module.exports = twitterConnection;