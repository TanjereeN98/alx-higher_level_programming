#!/usr/bin/node
const ISquare = require('./5-square.js');

class Square extends ISquare {
  charPrint (c = 'X') {
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
