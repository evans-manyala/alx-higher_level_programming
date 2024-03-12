#!/usr/bin/node

function printWithSpace (arg1, arg2) {
  console.log(`${arg1} \u00A0 is \u00A0 ${arg2}`);
}
printWithSpace(process.argv[2], process.argv[3]);
