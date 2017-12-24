var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var picSchema = new mongoose.Schema({
    img: { 
        filename: String,
        data: Buffer, 
        contentType: String 
    }
});

mongoose.model('Pic', picSchema);