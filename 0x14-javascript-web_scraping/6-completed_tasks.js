#!/usr/bin/node
//Jscript displays the no. of tasks completed by users id

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
        if (error) {console.log(error);}
        
        const data = JSON.parse(body);
        const completedTasksByUser ={};

        data.forEach(todo => {
                if(todo.completed)
                {
                        completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
                }
        });

        for (const userId in completedTasksByUser)
        {
                console.log(`'${userId}': ${completedTasksByUser[userId]}`);
        }
});
