#!/usr/bin/node

const dict = require('./101-data').dict;

const sorted = {};

for (const id in dict) {
  const n = dict[id];
  if (sorted[n]) {
    sorted[n].push(id);
  } else {
    sorted[n] = [id];
  }
}

console.log(sorted);
