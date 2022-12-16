#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url, function (err, resualt, body) {
  if (err) throw err;
  const movies = JSON.parse(body).resualt;
  const mv = (movies.filter(movie => movie.characters.includes(url + '/18')));
  console.log(mv.length);
});
