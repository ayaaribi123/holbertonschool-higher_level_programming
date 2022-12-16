#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url, function (err, resualt, body) {
  if (err) throw err;
  const movies = JSON.parse(body).resualt;
  const mv = (movies.reduce(movie => movie.characters.includes('/18')));
  console.log(mv.length);
});
