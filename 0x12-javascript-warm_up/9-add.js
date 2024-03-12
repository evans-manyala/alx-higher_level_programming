#!/usr/bin/node

const args = process.argv;
add(args[2], args[3]);

function add (arg1, arg2) {
  if (isNaN(arg1) || isNaN(arg2)) {
    console.log('NaN');
    return;
  }
  arg1 = parseInt(arg1);
  arg2 = parseInt(arg2);
  console.log(arg1 + arg2);
}
