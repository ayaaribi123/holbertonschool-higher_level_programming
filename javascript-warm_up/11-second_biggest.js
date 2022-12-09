#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const arr = process.argv.map(Number);
  arr.sort((a, b) => a - b);
  arr.shift();
  console.log(arr[arr.length - 2]);
}
