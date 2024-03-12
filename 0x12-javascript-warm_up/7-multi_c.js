#!/usr/bin/node

const myVar = 'C is Fun';
const args = process.argv;
const number = parseInt(args[2]);
let i = 0;

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
	while(i < number) {
		console.log(myVar);
		i++;
	}
}
