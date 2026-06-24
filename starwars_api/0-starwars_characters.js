#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

request(filmUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const names = [];
  let completed = 0;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, response, data) => {
      if (error) {
        console.error(error);
        return;
      }

      names[i] = JSON.parse(data).name;
      completed++;

      if (completed === characters.length) {
        for (let j = 0; j < names.length; j++) {
          console.log(names[j]);
        }
      }
    });
  }
});
