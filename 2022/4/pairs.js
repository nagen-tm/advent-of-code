/*
  come back to understand this one
*/

//import libs
const { readFileSync } = require('fs');

const pairs = async () => {
  // read the file, split on double new line
  const lines = readFileSync('input.txt', 'utf8').trim().split('\n')
  
  const partOne = lines.map((line) => {
    const [interval1, interval2] = line
    .split(",")
    .map((interval) => interval.split("-").map(Number))
    .sort((a, b) => {
      const oneSize = a[1] - a[0];
      const twoSize = b[1] - b[0];
      return twoSize - oneSize;
    });

    const oneFullContainsTwo =
    interval1[0] <= interval2[0] && interval1[1] >= interval2[1];

    return oneFullContainsTwo ? 1 : 0;
  })

  console.log(partOne.reduce((a, b) => a + b, 0));

  const partTwo = lines.map((line) => {
    const [first, second] = line
      .split(",")
      .map((interval) => interval.split("-").map(Number))
      .sort((a, b) => {
        const oneSize = a[1] - a[0];
        const twoSize = b[1] - b[0];
        return twoSize - oneSize;
      });

    const overlap = first[1] >= second[0] && second[1] >= first[0];

    return overlap ? 1 : 0;
  });

  console.log(partTwo.reduce((a, b) => a + b, 0));
}

pairs();
