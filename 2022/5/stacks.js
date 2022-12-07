/*
  TODO: the first parsing part is very tedious, find a way to reduce the process?
*/

//import libs
const { readFileSync } = require('fs');

  // read the file, split on double new line
  const input = readFileSync('input.txt', 'utf8').split('\n\n')

function createStacks(){
  let stacks = []
  // read the input, load the arrays
  const info = input[0].split('\n');

  // remove the number of stacks from the information
  let trim = info.pop().trim().split(' ');
  let numberOfArrays = trim[trim.length - 1]
  
  // create the number of arrays needed
  for(let i = 0; i < numberOfArrays; i++ ){
    stacks.push([])
  }
  
  // split the letter information
  for(let i = 0; i < info.length; i++ ){
    let letters = info[i].split(' ');
    // an empty stack is every 4 spaces, remove those spaces and use a dash 
    for(let i = 0; i < letters.length; i++){
      if(letters[i] === ''){
        letters.splice(i, 4, '-')
      }
    }
    // if there are letters, push to the correct array based on index
    for(let i = 0; i < letters.length; i++){
      if(letters[i] != '-'){
        stacks[i].push(letters[i])
      }
    }
  }
  // reverse the arrays for accuracy
  stacks.forEach(element => {
    element.reverse()
  });

  return stacks
}

function stacksOne() {
  stacks = createStacks();

  // parse the directions, logic to move things from arrays
  const moves = input[1].split('\n')
  moves.forEach(move => {
    // split information
    const directions = move.split(' ');
    
    // variabalize move info
    let amount = directions[1];
    let from = directions[3] - 1;
    let to = directions[5] - 1;

    // loop through by amount of times, move the letters
    for (let i = 0; i < amount; i++){
      let remove = stacks[from].pop();
      stacks[to].push(remove);
    }
  });


  // log the last letter in each array
  let result = '';
  stacks.forEach(stack => {
    const end = stack[stack.length-1]
    const grabLetter = end[1];
    result += grabLetter
  })

  console.log(result)
}

function stacksTwo(){
  stacks = createStacks();
  // part 2
  const moves = input[1].split('\n')
  moves.forEach(move => {
    // split information
    const directions = move.split(' ');
    
    // variabalize move info
    let amount = parseInt(directions[1]) ;
    let from = directions[3] - 1;
    let to = directions[5] - 1;

    let remove = stacks[from].splice(-amount, amount);
    stacks[to] = stacks[to].concat(remove);

  });

  let result = '';
  stacks.forEach(stack => {
    const end = stack[stack.length-1]
    const grabLetter = end[1];
    result += grabLetter
  })

  console.log(result)
}

stacksOne();
stacksTwo();
