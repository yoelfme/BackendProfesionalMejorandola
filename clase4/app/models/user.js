var models = require('./models');
var Schema = models.Schema;

var UserSchema = new Schema({
    username: String,
    twitter: Schema.Types.Mixed
});

var User = models.model('user', UserSchema)

module.exports = User;