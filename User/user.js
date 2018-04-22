// User.js
var mongoose = require('mongoose');

var UserSchema = new mongoose.Schema({
    name: String,
    lat: Number,
    long: Number
});

mongoose.model('User', UserSchema);
module.exports = mongoose.model('User');