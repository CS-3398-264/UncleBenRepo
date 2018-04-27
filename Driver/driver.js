// User.js
var mongoose = require('mongoose');


var DriverSchema = new mongoose.Schema({
    name: String,
    lat: Number,
    long: Number,
    available: Boolean
})

mongoose.model('Driver', DriverSchema);
module.exports = mongoose.model('Driver');