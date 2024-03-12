#!/usr/bin/node

const firstArg = process.argv[2];

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return undefined;
  } else if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(firstArg);
const result = factorial(num);

if (result === undefined) {
  console.log('Factorial is undefined for non-positive numbers and NaN');
} else {
  console.log(`${num}! = ${result}`);
}
