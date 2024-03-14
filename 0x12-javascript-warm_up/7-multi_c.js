#!/usr/bin/node
const x = 'C is fun';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
}
for (let y = 0; y < parseInt(process.argv[2]); y++) {
  console.log(x);
}
