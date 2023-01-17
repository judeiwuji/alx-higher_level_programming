#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(filepath, '\ufeff' + body, function (error) {
    if (error) {
      console.log(error);
    }
  });
});
