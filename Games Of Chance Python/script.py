import random

money = 100

#Write your game of chance functions here

# Validate bet
def valid_bet(bet):
    if bet < 0:
      print("Bet cannot be less than zero.")
    elif bet > money:
      print("Bet cannot exceed the money you have.")
    

# Coin Toss simulation
def flip(guess, bet):
  global money
  coin_toss = random.randint(0,1)
  print("Heads or Tails?")
  print("Coin flipped")
  guess = str.lower(guess)
  #  Validate bet
  valid_bet(bet)
  if guess != "heads" and guess != "tails":
    print("Guess must be Heads or Tails")
  else:
    # generate coin toss result
    coin_toss = random.randint(0,1)
    if coin_toss == 0:
     result = "heads"
    elif coin_toss == 1:
     result = "tails"
    # winning condition
    if guess == result:
      # Winning outcome
      print("The outcome is {}, you guessed {} the bet is won. ${} has been added to your account.".format(result, guess, bet))
      money += bet
      print("Account balance: $" + str(money))
    else:
      # Losing outcome
      print("The outcome is {}, you guessed {} the bet is lost. ${} has been subtracted from your account.".format(result, guess,  bet))
      money -= bet 
      print("Account balance: $" + str(money))


# Cho-Han simulation
def cho_han (guess, bet):
  global money
  print ("Cho-Han'")
  print("Even or odd?")
  guess = str.lower(guess)
  # Validate bet
  valid_bet(bet)
  if guess != "even" and guess != "odd":
    print("Guess must be Even or Odd")
  else:
    # Generate dice rolls
    dice_Roll1 = random.randint(1,6)
    dice_Roll2 = random.randint(1,6)
    roll_Sum = dice_Roll1 + dice_Roll2
    # Check if result is even
    is_Even = roll_Sum
    print ("You rolled a total of " + str(roll_Sum))
    if is_Even % 2 == 0:
      result = "Even"
    else:
      result = "Odd"
      #  Winning condition
    if guess == str.lower(result):
      # Winning outcome
      print ("The outcome is {}, the bet matches! YOU WIN!. ${} has been added to your account.".format(result, bet))
      money += bet
      print ("Account balance: $" + str (money))
    else:
      # Losing outcome
      print("The outcome is {}, the bet doesn't match. ${} has been subtracted from your account.".format(result, bet))
      money -= bet
      print ("Account balance: $" + str (money))

# 
  
def highest_card_wins(bet):
  global money
  print ("Highest card wins")
  # Validate bet
  if bet < 0:
    print("Bet cannot be less than zero.")
  elif bet > money:
    print ("Bet cannot exceed the money you have.")
  else:
    # Deck of cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    cards.sort()
    player1 = random.choice(cards)
    print("You have drawn " + str(player1))
    cards.remove(player1)
    opponent = random.choice(cards)
    print("The opponent has drawn " + str(opponent))
    cards.remove(opponent)
    #  Winning / losing condition
    if(player1 == opponent):
      print("The game is tied! The ${} is returned".format(bet))
    elif(player1 > opponent):
      # Winning outcome
      print("You have won with {} being the highest card! ${} has been added to your account.".format(player1, bet))
      money += bet
      print("Account balance: $" + str(money))
    else:
      # Losing outcome
      print("Your opponent has won with {} being the highest card! The bet is lost, ${} has been subtracted from your account.".format(opponent, bet))
      money -= bet
      print("Account balance: $" + str(money))


# Roulette table

def roulette (guess, bet):
  global money
  print ("Roulette")
  if bet < 0:
    print("Bet cannot be less than zero.")
  elif bet > money:
    print ("Bet cannot exceed the money you have.")
  else:
    # make the roulette wheel
    roulette_numbers = [00] + list(range(37))
    spin = random.choice (roulette_numbers)
    # guess is even or odd
    if spin == 0 or spin == 00:
      result = 'Loss'
    elif spin % 2 == 0:
      result = "Even"
    else:
      result = "Odd"
    print ("The spin landed on " + str(spin))
    #  winning condition integer
    if isinstance (guess, int) and guess == spin:
      money  += 35 * bet
      print ("You won $" + str(35 * bet))
      print ("Account balance: $" + str(money))
  #  Losing condition integer
    elif isinstance (guess, int) and guess != spin:
      money -= bet
      print ("You lost $" + str(bet))
      print ("Account balance: $" + str(money))
      # Winning condition "even" or "odd"
    if isinstance (guess, str) and guess.lower() == result.lower():
      money += bet
      print ("You won $" + str(bet))
      print ("Account balance: $" + str(money))
      # Losing condition "even" or "odd"
    elif isinstance (guess, str) and guess.lower() != result.lower():
      money -= bet
      print ("You lost $" + str(bet))
      print ("Account balance: $" + str(money))
        

#Call your game of chance functions here

flip("Heads", 10)
flip("Tails", 10)
cho_han("Even", 10)
cho_han("Odd", 10)
highest_card_wins(10)
roulette(2, 10)
roulette("even", 10)
roulette("odd", 10)