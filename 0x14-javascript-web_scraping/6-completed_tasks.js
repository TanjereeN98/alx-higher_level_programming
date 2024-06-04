#!/usr/bin/node

const apiUrl = process.argv[2];
const request = require('request');

request(`${apiUrl}`, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const myData = JSON.parse(body);
  const result = {};
  myData.map(todo => {
    if (todo.completed) {
      result[todo.userId] = (result[todo.userId] || 0) + 1;
    }
    return result;
  });
  console.log(result);
});
