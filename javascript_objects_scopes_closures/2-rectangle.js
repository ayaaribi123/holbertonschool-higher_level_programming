#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h, width, height) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
