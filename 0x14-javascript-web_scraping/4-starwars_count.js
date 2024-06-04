#!/usr/bin/node

const apiUrl = process.argv[2];
const request = require('request');

request(`${apiUrl}`, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const myData = JSON.parse(body).results;
  const data = myData.filter(f => f.characters.find(c => c.includes('18')));
  console.log(data.length);
});
