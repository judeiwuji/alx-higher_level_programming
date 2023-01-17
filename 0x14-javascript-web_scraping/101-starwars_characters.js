#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  for (const url of data.characters) {
    try {
      const cast = await getCharacter(url);
      console.log(cast.name);
    } catch (error) {
      console.log(error);
    }
  }
});

function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
