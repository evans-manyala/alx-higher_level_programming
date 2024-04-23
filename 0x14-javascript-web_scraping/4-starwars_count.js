#!/usr/bin/node
// JScript Prints the number of films with a given character ID

const request = require('request');

let filmCount = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  if (!data.results || !Array.isArray(data.results)) {
    console.error('Invalid data format.');
    return;
  }
  data.results.forEach((film) => {
    if (film.characters && Array.isArray(film.characters)) {
      if (film.characters.some((character) => character.includes('/18/'))) {
        filmCount++;
      }
    }
  });
  console.log(filmCount);
});
