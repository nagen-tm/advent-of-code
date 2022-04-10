/* 
  Day 1: use the day one input file and find every day that the depth increased
  Notes: started with reading the file as this:  const readFile = fs.readFileSync('day_one_input.txt', 'utf8').split('\n')
    This got me to 1138
    Need to look up the .filter and .map to understand why it gives the extra 1 to get the correct answer.
*/

//import libs
const fs = require('fs');

// placeholder for count
let count = 0;

// read the file
const readFile = fs.readFileSync('day_one_input.txt', 'utf8').split('\n').filter((x) => Boolean(x)).map((x) => parseInt(x));

// loop through, compare last to present
for(let i = 1; i < readFile.length; i++){
  if(readFile[i] > readFile[i-1]){
    count++;
  }
}
console.log(count);