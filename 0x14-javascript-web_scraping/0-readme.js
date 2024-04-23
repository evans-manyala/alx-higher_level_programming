#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error('Please provide the file path as an argument.');
  process.exit(1); // Exit with an error code
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error('An error occurred while reading the file:', err);
  } else {
    // Print the content of the file
    console.log('File content:');
    console.log(data);
  }
});
