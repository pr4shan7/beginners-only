//Setting up express by importing it and running the function
const express = require('express');
const app = express();

//Setting up express server on port 3000, and configuring it to run with JSON.
app.listen(3000, () => console.log('Server started successfully!'));
app.use(express.json());

// cd into the Node.js\APIs\Express.js\Beginner folder, and run 'npm install', then 'npm start' to start the server!

// Single data array for both Get and POST requests.
const userList = [
    {name: 'Mike', age: 23},
    {name: 'Jim', age: 41},
    {name: 'Terra', age: 19},
    {name: 'Richard', age: 32},
    {name: 'Alex', age: 56},
];


// Simple GET endpoint
app.get('/users', (req, res) => {  
    res.send(userList);
    // GET localhost:3000/users = [{"name": "Mike", "age": 23}, {"name": "Jim", "age": 41},..]
});

// Simple POST endpoint
app.post('/createUser', (req, res) => {
    userList.push({name: req.body.name, age: req.body.age})
    res.send(userList)
    // POST localhost:3000/createUser using {"name": "Bob", "age": 44} to add him to the list!
});

