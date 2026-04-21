const express = require('express');
const mongoose = require('mongoose');
const productRoutes = require('./routes/productroutes')

const app = express();
app.use(express.json());
const port = 3000;

mongoose.connect('mongodb+srv://databaseUser:dWlULBIBApO1wB2X@cluster0.omige7m.mongodb.net/?appName=Cluster0').then(() => {
    console.log("Connected to MongoDB");
}).catch(err => {
    console.error("Error connecting to MongoDB", err);
});

app.use('/api', productRoutes);

console.log("Server is starting...");
app.get('/', async(req , res) =>{
    res.send(`
        <div>
        <h1>Student Info:</h1>
        <h2>name: Rohit</h2>
        <h2>Roll No: 12345</h2>
        <h2>Branch: CSE</h2>
        </div>
        `)
})

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

// const express = require('express');
// const app = express();

// const PORT = 8080

// app.get('/', async(req , res)=>{
//     res.send(`
//         <h1>Welcome to my server</h1>
//         <h2>name: Rohit</h2>
//         `)
// })



// app.get("/health", (req, res) => {
//   res.json({
//     status: "UP",
//     service: "devops-test",
//     time: new Date()
//   });
// });

// module.exports = app;

// if(process.env.NODE_env !== "test") {
//   app.listen(PORT, () =>{
//     console.log(`Server is running on port ${PORT}`);
// })
// }