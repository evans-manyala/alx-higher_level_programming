#!/usr/bin/node

const args = process.argv.length - 2;
const myVar = 'C is Fun';
const number = parseInt(args[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(myVar);
}
