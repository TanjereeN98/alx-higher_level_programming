#!/usr/bin/node
function fact (number) {
  if (number === 1 || number === 0) { return 1; }
  return number * fact(number - 1);
}
if (isNaN(process.argv[2])) { console.log(1); } else { console.log(fact(parseInt(process.argv[2]))); }
