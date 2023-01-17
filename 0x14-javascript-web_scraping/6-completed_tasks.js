#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const countDict = {};
  for (const item of data) {
    if (item.completed) {
      if (!countDict[item.userId]) {
        countDict[item.userId] = 0;
      }
      ++countDict[item.userId];
    }
  }
  console.log(countDict);
});
