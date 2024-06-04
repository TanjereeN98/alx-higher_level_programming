#!/usr/bin/node

const requestedUrl = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('node:fs');

request(`${requestedUrl}`, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.error(err);
    }
  });
});
