const mongoose = require('mongoose');
const fs = require('fs');
const csv = require('csv-parser');

const { cityCord , stateCord , boundCord} = require('../models/cordSchema');
const { fuelPriceSchema } = require('../models/fuelPriceSchema');

const MONGO_URL = process.env.PORT || "mongodb://127.0.0.1:27017";

const dbConnection = () => {

    mongoose.connect(MONGO_URL)
    .then((conn) => {
        console.log(`Connection established to ${conn.connection.host}`);
    })
    .catch((err) => {
        console.log(err.message);
        process.exit(1);
    });
}

let csvFilePath = "/home/mohitking/Desktop/fuelish-cli/FuelishCLI/src/Citycord.csv"

// now read the csv file and upload the data in mongoDB collection
fs.createReadStream(csvFilePath)
.pipe(csv())
.on('data' , async (row) => {
    try {
        const cityCordData = new cityCord({
            city : row.City,
            state : row.State,
            lat : Number(row.lat),
            long : Number(row.long)
        });

        const savedData = await cityCordData.save();
        console.log(`Data is saved : ${savedData}`);

    } catch (error) {
        console.log(`Error occurred : ${error}`);
    }
})
.on('end' , () => {
    console.log('CSV file is successfully processed');
});

// calling dbConnection here
dbConnection();

module.exports = dbConnection;
