var express = require('express');
var router = express.Router();
var db = require( 'mongoose' );
var Pic = db.model('Pic');

router.route('main/picture').get(function(req, res, next) {

    console.log("Get Picture");

    Pic.findOne({ filename: 'Portrait.jpg'}), (function (err, pic) {

        if (err) return next("Failed");
        var base64 = (pic[0].img.data.toString('base64'));
        res.send(base64);        
    });
});

router.route('Solitaire/Header').get(function(req, res, next) {

    db.findOne( {filename: 'Header.h'}, 
        function(error, record) {

            if (record != null) {
                console.log(record.filename + " found in DB");
                return res.status(200).send(record);
            }

            if (error || record == null) { return console.log("Failed to search DB"); }
        }
    );
});

module.exports = router;