#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (const item of data.results) {
    for (const character of item.characters) {
      if (character.includes('18')) {
        ++count;
      }
    }
  }
  console.log(count);
});
