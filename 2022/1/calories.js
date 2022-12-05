/*
  Learnings: I have not used reduce before
  Documentation:
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
  https://www.w3schools.com/jsref/jsref_reduce.asp
*/

//import libs
const { readFileSync } = require('fs');

const calories = async () => {
  // read the file, split on double new line
  const elves = readFileSync('input.txt', 'utf8').trim().split('\n\n')
  
  // per elf, split on new line and add the calories together
  const calories = elves.map((elf) => {
    const calories = elf.split("\n").map(Number);
    return calories.reduce((previous, current) => previous + current, 0);
  });

  // return part one, top calories by finding the max number
  console.log(Math.max(...calories));

  // return part two by sorting and taking the first three and adding them together
  calories.sort((a,b) => b-a);
  const topThree = calories.slice(0, 3).reduce((previous, current) => previous + current, 0);
  console.log(topThree)
}

calories();