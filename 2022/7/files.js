/*
*/

//import libs
const { readFileSync } = require('fs');
const lines = readFileSync('example.txt', 'utf8').trim().split('\n')

// parse the file system information for movement, dir, file and size
function filesystem(lines) {
  // starting directory
  let system = {
    name: '/',
    isDir: true,
    children: []
  };

  // set to capture all listed items
  let currentCommand = null;

  lines.forEach(line => {
    // if $  
    if(line.contains('$')){
      // split the command for info
      const split = line.split(' ')
      // set current command
      if(split[1] === 'cd'){
        currentCommand = 'cd'
      } else if (split[1] === 'ls'){
        currentCommand = 'ls'
      }
      // if we are changing dir, 
      if (currentCommand = 'cd'){
        // ?
      }
      // if we are listing, go through lines and add files/dir
      if (currentCommand = 'ls'){
        if(line.contains('dir')){
          // add directory to child
        } else {
          // add file to child
        }
      }
    
    }
    // 
  });

  return system;
}

