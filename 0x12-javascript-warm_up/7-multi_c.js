#!/usr/bin/node

const args = process.argv[2];
let number = parseInt(args);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
}

while (number > 0) {
  console.log('C is Fun');
  number++;
}
