#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i = 0;
if (num) {
  for (i; i < num; i++) {
    console.log('x'.repeat(num));
  }
} else {
  console.log('Missing size');
}
