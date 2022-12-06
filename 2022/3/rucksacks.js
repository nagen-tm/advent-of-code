/*
TODO: how do i compare priority without typing out an array?
      understand how part two works, comparing 3 arrays
*/

//import libs
const { readFileSync } = require('fs');

const priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const total = async () => {
  // read the file, split on new line
  const compartments = readFileSync('input.txt', 'utf8').trim().split('\n')
  
  const number = compartments.map((rucksack) => {
    // finding the halfway points
    const half = Math.ceil(rucksack.length / 2);
    const firstHalf = rucksack.slice(0, half);
    const secondHalf = rucksack.slice(half);
    
    // compare and find the same letter
    const letter = _compareLetters(firstHalf, secondHalf);

    // get priority number
    return _priority(letter);
  })

  // part one
  console.log(number.reduce((a, b) => a +b, 0));

  let total = 0;

  // grab the rucksacks by threes
  for(let i = 0; i < compartments.length; i+=3){
    const packs = [[...compartments[i]], [...compartments[i + 1]], [...compartments[i + 2]]]
    // compare those three
    let set = new Set(packs[0]);
    let intersection = packs[1].filter((x) => set.has(x));

    set = new Set(intersection);
    intersection = packs[2].filter((x) => set.has(x));

    const dedup = [...new Set(intersection)];

    const number = _priority(dedup[0]);
    total += number;
 
  }

  // part 2 
  console.log(total);
}

total();

function _compareLetters(firstHalf, secondHalf){
  for (let i = 0; i < firstHalf.length; i++){
    if(secondHalf.includes(firstHalf[i])){
      return firstHalf[i];
    }
  }
}

function _priority(letter){
  for (let i = 0; i < priority.length; i++){
    if(priority[i] == letter){
      return i + 1
    }
  }
}
