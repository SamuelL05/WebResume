var mongoose = require('mongoose');

// May be redudant
var Schema = mongoose.Schema;

// establish MongoDB connection
mongoose.connect("mongodb://Resume:password12@ds241895.mlab.com:41895/test-db", {
    useMongoClient: true
});

var conn = mongoose.connection;
var path = require('path');
// Require GridFS
var Grid = require('gridfs-stream');
// Require filesystem module
var fs = require('fs');
require('../models/models');
var Pic = mongoose.model('Pic');

// Where to find video that will be stored in DB

var picturePath = path.join(__dirname, "../Images/Portrait.jpg");
var headerPath = path.join(__dirname, "../Programs/Solitaire/Header.h");
var mainPath = path.join(__dirname, "../Programs/Solitaire/Main.cpp");
var methodsPath = path.join(__dirname, "../Programs/Solitaire/Methods.cpp");

// Connect GridFS and Mongo
Grid.mongo = mongoose.mongo;

conn.once('open', function() {

    var gfs = Grid(conn.db);

    let pictureStream = gfs.createWriteStream({
            filename: 'Portrait.jpg'
        })
        headerStream = gfs.createWriteStream({
            filename: 'Header.h'
        })
        mainStream = gfs.createWriteStream({
            filename: 'Main.cpp'
        })
        methodsStream = gfs.createWriteStream({
            filename: 'Methods.cpp'
        });

    gfs.findOne({filename: 'Portrait.jpg'}, 
        function(error, record) {

            if (record == null) {

                fs.createReadStream(picturePath).pipe(pictureStream);
                return console.log('Portrait.jpg wrote to DB');
            }
            if (record != null) {
                return console.log(record.filename + " found in DB");
            }
            if (error) { return console.log("Failed to search DB");}
    })

    gfs.findOne( {filename: 'Header.h'}, 
        function(error, record) {

            if (record == null) {
                fs.createReadStream(headerPath).pipe(headerStream);
                return console.log('Header.h wrote to DB');
            }
            if (record != null) {
                return console.log(record.filename + " found in DB");
            }
            if (error) { return console.log("Failed to search DB");}
        }
    );

    gfs.findOne( {filename: 'Main.cpp'}, 
        function(error, record) {

            if (record == null) {
                fs.createReadStream(mainPath).pipe(mainStream);
                return console.log('Main.cpp wrote to DB');
            }
            if (record != null) {
                return console.log(record.filename + " found in DB");
            }
            if (error) { return console.log("Failed to search DB");}
        }
    );
    
    gfs.findOne( {filename: 'Methods.cpp'}, 
        function(error, record) {

            if (record == null) {
                fs.createReadStream(methodsPath).pipe(methodsStream);
                return console.log('Methods.cpp wrote to DB');
            }
            if (record != null) {
                return console.log(record.filename + " found in DB");
            }
            if (error) { return console.log("Failed to search DB");}
        }
    );
});
