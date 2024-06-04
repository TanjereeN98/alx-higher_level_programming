#!/usr/bin/node

const urlRequest = process.argv[2];
const request = require('request');

request(urlRequest, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
