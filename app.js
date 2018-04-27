// app.js
var express = require('express');
var app = express();

var db = require('./db');

var UserController = require('./User/UserController');
app.use('/users', UserController);

var DriverController = require('./Driver/DriverController');
app.use('/drivers', DriverController);

var AdminController = require('./Admin/AdminController');
app.use('/admins', AdminController);

module.exports = app;