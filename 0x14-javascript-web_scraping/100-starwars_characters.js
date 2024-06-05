#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  data.characters.forEach(element => {
    request(element, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    }
    );
  });
});
