#!/usr/bin/node

const myVar = 'C is Fun';
const args = process.argv;
const number = parseInt(args[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(myVar);
  }
}
