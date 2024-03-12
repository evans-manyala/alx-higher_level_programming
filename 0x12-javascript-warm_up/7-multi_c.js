#!/usr/bin/node

const myVar = "C is Fun";
const numArgs = process.argv.length - 2;
const number = parseInt(args[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(myVar);
}