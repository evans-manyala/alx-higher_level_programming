#!/usr/bin/node
// Jscript that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;

    const fetchAndPrintCharacters = (index) => {
      if (index >= characters.length) {
        return;
      }

      request.get(characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          fetchAndPrintCharacters(index + 1);
        }
      });
    };
    fetchAndPrintCharacters(0);
  }
});
