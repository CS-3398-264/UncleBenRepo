// User.js
var mongoose = require('mongoose');


var DriverSchema = new mongoose.Schema({
    name: String,
    password: String
})

mongoose.model('Admin', DriverSchema);
module.exports = mongoose.model('Admin');