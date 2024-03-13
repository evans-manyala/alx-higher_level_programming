#!/usr/bin/node

const { dict } = require('./101-data.js');
function invertDictionary (originalDict) {
  const invertedDictionary = {};
  for (const userId in originalDict) {
    const occurrences = originalDict[userId];
    if (!(occurrences in invertedDictionary)) {
      invertedDictionary[occurrences] = [];
    }
    invertedDictionary[occurrences].push(userId);
  }
  return invertedDictionary;
}

const newDict = invertDictionary(dict);
console.log(newDict);
