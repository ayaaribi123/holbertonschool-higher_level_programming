#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    let i = 0;
    let j = 0;
    if (c === undefined) {
      for (j; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (i; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
