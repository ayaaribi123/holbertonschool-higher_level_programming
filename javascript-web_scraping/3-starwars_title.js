#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + Id;
request.get(url, function (err, resualt, body) {
  if (err) throw err;
  else {
    console.log(JSON.parse(body).title);
  }
});
