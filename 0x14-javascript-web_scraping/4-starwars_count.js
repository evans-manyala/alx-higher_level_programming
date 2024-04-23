#!/usr/bin/node
// JScript Prints the number of films with given ID

const request = require('request');
let ID = 0;

request.get(process.argv[2], (erro, response, body) => {
  if (error) { console.log(error); } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character, includes(18)) {
          ID = +1;
        }
      });
    });
    console.log(ID);
  }
});
