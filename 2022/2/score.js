/*
  TODO: look into and understand the usage of maps better
*/

//import libs
const { readFileSync } = require('fs');

const rock = 1;
const paper = 2;
const scissors= 3;

const score = async () => {
  // read the file, split on new line
  const strat = readFileSync('input.txt', 'utf8').trim().split('\n')
  
  const mapInput = {
    A: rock,
    B: paper,
    C: scissors,
    X: rock,
    Y: paper,
    Z: scissors
  };

  // per round, split on space and compare the scores to tally total
  const firstScore = strat.map((round) => {
    const opponent = mapInput[round[0]];
    const mine = mapInput[round[2]];
    return _scoreTally(opponent, mine);
  });

  // part one, the end score
  console.log(firstScore.reduce((a, b) => a +b, 0));

  // part two update the resulting responses
  const updatedMap = {
    A: {
      X: scissors, //lose
      Y: rock, //draw
      Z: paper, //win
    },
    B: {
      X: rock,
      Y: paper,
      Z: scissors,
    },
    C: {
      X: paper,
      Y: scissors,
      Z: rock,
    },
  };

    // per round, split on space and compare the scores to tally total
    const secondScore = strat.map((round) => {
      const opponent = mapInput[round[0]];
      const mine = updatedMap[round[0]][round[2]];
      return _scoreTally(opponent, mine);
    });
  
    // part two, the end score
    console.log(secondScore.reduce((a, b) => a +b, 0));
}

score();

// returns the scor from that round
function _scoreTally(opponent, mine){
  // tie score
  if(opponent === mine){
    return mine + 3;
  }
  // winning score
  if((opponent === rock && mine === paper) ||
  (opponent === paper && mine === scissors) ||
  (opponent === scissors && mine === rock)){
    return mine + 6;
  } else{
    // lose score
    return mine;
  }
}