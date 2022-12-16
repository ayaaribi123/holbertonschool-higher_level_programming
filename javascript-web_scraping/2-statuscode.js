#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, resualt) {
  if (err) throw err;
  else {
    console.log('code:', resualt.statusCode);
  }
});
