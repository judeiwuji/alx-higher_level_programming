#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = c || 'X';

    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += c;
      }
      console.log(pattern);
    }
  }
}

module.exports = Square;
