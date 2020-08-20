let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;


// Generate  random target number 0 - 9
const generateTarget = () => {
  return Math.floor(Math.random() * 10);
}

// Calculate the winner
const compareGuesses = (humanGuess, computerGuess, targetNumber) => {
  let humanDiff = getAbsoluteDistance( targetNumber,  humanGuess );
  let computerDiff = getAbsoluteDistance( targetNumber, computerGuess);
  if (humanDiff < computerDiff){
    return true;
  } else if (humanDiff > computerDiff){
    return false;
  } else if (humanDiff === computerDiff){
    return true;
  }
}

//  Update the score whilst playing
const updateScore = (winner) => {
  if(winner === 'human'){
    humanScore++
  } else if (winner === 'computer'){
    computerScore++
  }
}

//  increment current round
function advanceRound() {
  currentRoundNumber++
}

//  
function getAbsoluteDistance(num1, num2){
  return Math.abs(num1 - num2);
}
