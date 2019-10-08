const express = require('express');
const app = express();

app.listen(3000, () => console.log('Server started successfully!'));
app.use(express.json());

// cd into the Node.js\APIs\Express.js\Beginner folder, and run 'npm install', then 'npm start' to start the server!

// Simple GET endpoint
app.get('/users', (req, res) => {
    const userList = [
        {name: 'Mike', age: 23},
        {name: 'Jim', age: 41},
        {name: 'Terra', age: 19},
        {name: 'Richard', age: 32},
        {name: 'Alex', age: 56},
    ];

    res.send(userList);
    // GET localhost:3000/users = [{"name": "Mike", "age": 23}, {"name": "Jim", "age": 41},..]
});

// Simple POST endpoint
app.post('/createUser', (req, res) => {
    const userList = [
        {name: 'Mike', age: 23},
        {name: 'Jim', age: 41},
        {name: 'Terra', age: 19},
        {name: 'Richard', age: 32},
        {name: 'Alex', age: 56},
    ];

    userList.push({name: req.body.name, age: req.body.age})

    res.send(userList)
    // POST localhost:3000/createUser using {"name": "Bob", "age": 44} to add him to the list!
});

