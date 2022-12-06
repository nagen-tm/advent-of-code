/*
  TODO: 
  - look more into .shift, i understand what i needed but didn't know how
  to implement it.
  - understand Set for the unique values

  Documentation: https://www.w3schools.com/jsref/jsref_shift.asp
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift

  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
  */

//import libs
const { readFileSync } = require('fs');
const lines = readFileSync('input.txt', 'utf8').trim()

const packet = async () => {
    // move the characters to a new array, compare the new character to that arrary
    // if a copy then put that into another array
    // add those lengths of arrays together once first array equals 4
    let unique = [];

    for (let i = 0; i < lines.length; i++){
      unique.push(lines[i]);
      if(unique.length > 4){
        // remove first element of array
        unique.shift();
      } 
      // check that the letters are unique
      if(unique.length === 4 && _uniqueCheck(unique)){
        // return the index plus one
        console.log( i + 1);
        return i + 1
      }
    };
}

const message = async () => {
    let unique = [];

    // part 2
    for (let i = 0; i < lines.length; i++){
      unique.push(lines[i]);
      if(unique.length > 14){
        // remove first element of array
        unique.shift();
      } 
      // check that the letters are unique
      if(unique.length === 14 && _uniqueCheck(unique)){
        // return the index plus one
        console.log( i + 1);
        return i + 1
      }
    };
}

packet();
message();

function _uniqueCheck(array) {
  return (new Set(array)).size == array.length;
}