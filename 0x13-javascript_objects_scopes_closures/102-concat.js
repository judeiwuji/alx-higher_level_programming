#!/usr/bin/node
const fs = require('fs');

const source = process.argv[2];
const source1 = process.argv[3];
const destination = process.argv[4];

const content =
  fs.readFileSync(source, 'utf-8') + fs.readFileSync(source1, 'utf-8');
fs.writeFileSync(destination, content, { encoding: 'utf-8' });
