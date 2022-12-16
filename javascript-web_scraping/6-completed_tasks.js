#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, resualt, body) {
  if (err) throw err;
  else {
    const content = JSON.parse(body);
    const completed = {};
    for (const i of content) {
      if (i.completed === undefined) {
        if (completed[i.userId] === undefined) {
          completed[i.userId] = 1;
        } else {
          completed[i.userId] = completed[i.userId] + 1;
        }
      }
    }
    console.log(completed);
  }
});
