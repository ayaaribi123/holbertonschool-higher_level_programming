#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h, width, height) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
