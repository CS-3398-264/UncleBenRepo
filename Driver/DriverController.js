//Drv=iverController.js
var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: true }));
router.use(bodyParser.json());

var Driver = require('./Driver');

// CREATES A NEW USER
router.post('/', function (req, res) {
    Driver.create({
            name : req.body.name,
            lat: req.body.lat,
            long : req.body.long,
            available: req.body.available
        },
        function (err, user) {
            if (err) return res.status(500).send("There was a problem adding the information to the database.");
            res.status(200).send(user);
        });
});
// RETURNS ALL THE USERS IN THE DATABASE
router.get('/', function (req, res) {
    Driver.find({}, function (err, users) {
        if (err) return res.status(500).send("There was a problem finding the drivers.");
        res.status(200).send(users);
    });
});


//Gets by ID
router.get('/:id', function (req, res) {
    Driver.findById(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem finding the driver.");
        if (!user) return res.status(404).send("No driver found.");
        res.status(200).send(user);
    });
});


router.get('/:available', function (req, res) {
    Driver.findByAvail(req.params.available, function (err, user) {
        if (err) return res.status(500).send("There was a problem finding the driver.");
        if (!user) return res.status(404).send("No driver found.");
        res.status(200).send(user);
    });
});

// UPDATES A SINGLE USER IN THE DATABASE
router.put('/:id', function (req, res) {

    Driver.findByIdAndUpdate(req.params.id, req.body, {new: true}, function (err, user) {
        if (err) return res.status(500).send("There was a problem updating the driver.");
        res.status(200).send(user);
    });
});

//Delete user by ID
router.delete('/:id', function (req, res) {
    Driver.findByIdAndRemove(req.params.id, function (err, user) {
        if (err) return res.status(500).send("There was a problem deleting the driver.");
        res.status(200).send("Driver "+ user.name +" was deleted.");
    });
});

module.exports = router;