#!/usr/bin/node

const NewSquare = require('./5-square.js');
const Square = class extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

module.exports = Square;
