#!/usr/bin/node
const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const count_dict = {};

  for (const item of data) {
    if (item.completed) {
      if (!count_dict[item.userId]) {
        count_dict[item.userId] = 0;
      }
      ++count_dict[item.userId];
    }
  }
  console.log(count_dict);
});
