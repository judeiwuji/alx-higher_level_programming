#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  for (const character of data.characters) {
    request(character, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }
      const cast = JSON.parse(body);
      console.log(`${cast.name}`);
    });
  }
});
