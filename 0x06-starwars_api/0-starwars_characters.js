#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (const charId of characters) {
    await new Promise((resolve, reject) => {
      request(charId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
