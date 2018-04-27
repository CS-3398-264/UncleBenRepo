//Drv=iverController.js
var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: true }));
router.use(bodyParser.json());

var Admin = require('./Admin');

// CREATES A NEW USER
router.post('/', function (req, res) {
    Admin.create({
            name : req.body.name,
            password : req.body.password
        },
        function (err, user) {
            if (err) return res.status(500).send("There was a problem adding the information to the database.");
            res.status(200).send(user);
        });
});
// RETURNS ALL THE USERS IN THE DATABASE
router.get('/', function (req, res) {
    Admin.find({}, function (err, users) {
        if (err) return res.status(500).send("There was a problem finding the Admins.");
        res.status(200).send(users);
    });
});

//Gets by ID
router.get('/:id', function (req, res) {
    Admin.findById(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem finding the Admin.");
        if (!user) return res.status(404).send("No Admin found.");
        res.status(200).send(user);
    });
});

// UPDATES A SINGLE USER IN THE DATABASE
router.put('/:id', function (req, res) {

    Admin.findByIdAndUpdate(req.params.id, req.body, {new: true}, function (err, user) {
        if (err) return res.status(500).send("There was a problem updating the Admin.");
        res.status(200).send(user);
    });
});

//Delete user by ID
router.delete('/:id', function (req, res) {
    Admin.findByIdAndRemove(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem deleting the Admin.");
        res.status(200).send("Admin "+ user.name +" was deleted.");
    });
});

module.exports = router;