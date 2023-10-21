const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const fuelPriceSchema = new Schema({
    city :{
        type : String,
        require : true
    },

    Price : {
        type : Number,
        require : true
    },
    
    Change : {
        type : Number,
        require : true
    },
    
    Price: {
        type : Number,
        require : true
    },
    
    Change: {
        type : Number,
        require : true
    }
});

const fuelPriceWithChange = mongoose.model('fuelPriceWithChange' , fuelPriceSchema);

module.exports = fuelPriceSchema;