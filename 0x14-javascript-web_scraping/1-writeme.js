#!/usr/bin/node

const filePath = process.argv[2];
const stringtoWrite = process.argv[3];

const fs = require('node:fs');

fs.writeFile(filePath, stringtoWrite, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
