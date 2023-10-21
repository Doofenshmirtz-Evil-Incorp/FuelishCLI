const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const cityCordSchema = new Schema({

    city : {
        type : String,
        require : true
    },

    state : {
        type : String,
        require : true
    },

    lat : {
        type : Number,
        require : true
    },

    long : {
        type : Number,
        require : true
    }
});

const stateCordSchema = new Schema({

    state : {
        type : String,
        require : true
    },

    lat : {
        type : Number,
        require : true
    },

    long : {
        type : Number,
        require : true
    }
});

const cityCord = mongoose.model('cityCordData' , cityCordSchema);
const stateCord = mongoose.model('stateCordData' , stateCordSchema);

module.exports = {cityCord , stateCord};