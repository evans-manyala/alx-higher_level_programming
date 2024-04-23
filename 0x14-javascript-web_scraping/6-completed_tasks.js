#!/usr/bin/node
//Jscript displays the no. of tasks completed by users id

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
        if (error) {console.log(error);}
        
        const completedTasksByUser ={};
        body.forEach((todo) => {
                if(todo.completed){
                        if(!completedTasksByUser[todo.UserId]){
                                completedTasksByUser[todo.UserId] = 1;
                        }
                        else{
                                completedTasksByUser[todo.UserId]++;
                        }
                }
        });
        console.log(completedTasksByUser);
})
