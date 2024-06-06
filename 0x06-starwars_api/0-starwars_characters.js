#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
*/

const request = require('request');
const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.alx-tools.com/api/films/';

request(filmURL + filmNum, async (err, res, body) => {
  if (err) return console.error(err);

  const charactersURLList = JSON.parse(body).characters;
  for (const chracterURL of charactersURLList) {
    await new Promise((resolve, reject) => {
      request(chracterURL, (err, res, body) => {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
