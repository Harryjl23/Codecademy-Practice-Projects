evolutions={
  # Evolution level, Evolved name, New speed stat
    "Charmander":[16, "Charmeleon", 80],
    "Charmeleon":[36, "Charizard",  100],
    "Squirtle":[16, "Wartotle", 58],
    "Wartotle":[36, "Blastoise", 78],
    "Bulbasaur":[16, "Ivysaur", 60],
    "Ivysaur":[36, "Venusaur", 80]
}


class Pokemon:
  def __init__(self, name, level, pokemon_type, speed, special_move = "", exp = 0, is_knocked_out = False, fainted_not_healed = False):
    self.name = name.title()
    self.level = level
    self.max_health = self.level * 4
    self.health = self.max_health
    self.type = pokemon_type.title()
    self.fainted = is_knocked_out
    self.exp = exp
    self.fainted_not_healed = fainted_not_healed
    self.special_move = special_move
    self.speed = speed
    self.next_evolution = -1 #if there's no next evo, keep this at -1 else set it to the level of the next evolution
    if self.name in evolutions:
            self.next_evolution = evolutions[self.name][0]
            
    

  def __repr__(self):
    # Prints name of pokemon, level, Health and Type
      return "Name: {name}\n Level: {level}\n Health: {hp}\n Type: {type}\n".format(name = self.name, level = self.level, hp = self.health, type = self.type)

  def knockout(self):
      #  Once health reaches zero
        self.health = 0
        self.fainted = True
        print("{} with {} health has fainted.".format(self.name, self.health))

  def lose_health(self, damage):
        #Health cannot go below 0
           if self.health - damage <= 0:   
            #  When the pokemon health reaches 0 
             self.knockout()
           else:
            #   If damage doesn't take health to zero
             self.health -= damage
             print("{name} took a hit and has {hp} health left".format(name = self.name, hp = self.health))
    
  def gain_health(self, restore):
    #  Check if Health is already at max
    if self.health == self.max_health:
           print("{} is already at max health.".format(self.name))
    else:
       # Health cannot go past max health
        if self.health + restore > self.max_health:
          self.health = self.max_health
          print("{} was healed to full {} health!".format(self.name, self.max_health))
        else:
          #  Sets Health + restore amount
          self.health += restore 
          print("Regained {} HP {} now has {} health.".format(restore, self.name, self.health))
    
  def revive(self):
      # In game the revived pokemon gets half its health restored
      self.health += self.max_health / 2
      self.fainted = False
      self.fainted_not_healed = False
      print("{} revived. {} health restored".format(self.name, self.health))

  def special_attack(self, opponent):
    # Check  if opp pokemon is already fainted
    if self.fainted:
          print("{} cannot attack, {} is knocked out. Please switch pokemon!".format(self.name, self.name))
    elif self.special_move != "" :
            print("{name} attacks {oppname} with special move {special}!".format(name = self.name, oppname = opponent.name, special = self.special_move))
            #  Conditions for type of pokemon fighting Fire vs Grass, Water and Fire
            if self.type == 'Fire':
              if opponent.type == 'Grass':
                # Extra damage for special move
                    dmg = self.level * 3
                    opponent.lose_health(dmg)
                    print("Super Effective!")
              elif opponent.type == 'Water':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
              else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
    #  Conditions for type of pokemon fighting Water vs Fire, Grass and Water
            if self.type == 'Water':
                if opponent.type == 'Fire':
                  # Extra damage for special move
                    dmg = self.level * 3
                    opponent.lose_health(dmg)
                    print("Super Effective!")
                elif opponent.type == 'Grass':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
                else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
       #  Conditions for type of pokemon fighting Grass vs Water, Fire and Grass
            if self.type == 'Grass':
                if opponent.type == 'Water':
                  # Extra damage for special move
                    dmg = self.level * 3
                    opponent.lose_health(dmg)
                    print("Super Effective!")
                elif opponent.type == 'Fire':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
                else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")


  def attack(self, opponent):
    # Check if opponent pokemon is already fainted
        if self.fainted:
          print("{} cannot attack, {} is knocked out. Please switch pokemon!".format(self.name, self.name))
        else:
          print("{} attacks {}!".format(self.name, opponent.name))
          if self.type == 'Fire':
            if opponent.type == 'Grass':
                    dmg = self.level * 2
                    opponent.lose_health(dmg)
                    print("Super Effective!")
            elif opponent.type == 'Water':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
            else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
          if self.type == 'Water':
                if opponent.type == 'Fire':
                    dmg = self.level * 2
                    opponent.lose_health(dmg)
                    print("Super Effective!")
                elif opponent.type == 'Grass':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
                else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
          if self.type == 'Grass':
                if opponent.type == 'Water':
                    dmg = self.level * 2
                    opponent.lose_health(dmg)
                    print("Super Effective!")
                elif opponent.type == 'Fire':
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
                else:
                    dmg = self.level * .5
                    opponent.lose_health(dmg)
                    print("Not very effective!")
                    
  def evolve(self):
  #Get the evolved pokemon name, change name to that and check if there's any further evolution
        evolution_name = evolutions[self.name][1]
        oldName = self.name 
        if evolution_name in evolutions:
          #store the next evolution level next e.g charmander evolves into Charmeleon
          #now Charmeleon's next evolution var will have 36 as the level for Charizard evo
            self.next_evolution = evolutions[evolution_name][0]
            # New speed stat updated
            self.speed = evolutions[evolution_name][2]
        else:
            self.nextEvolution = -1
        self.name = evolution_name
        print(f"{oldName} evolved into {self.name}!")
        

  def gain_xp(self, opponent):
    # Calculate exp gained from defeating an opponent
        exp_gained =  opponent.level * .25
        self.exp += exp_gained
    # Calculate exp to next level
        level = self.level * 2
        exp_to_level = level - self.exp
        print("{} gained {} experience!".format(self.name, exp_gained))
        # Call level_up if the criteria matches
        if exp_to_level <= 0:
          self.level_up()
        else:
          print("{} needs {} xp to level up!".format(self.name, exp_to_level))

  def level_up(self):
  # Once levelled up is called level increase by 1 and set exp back to zero
    self.level += 1
    self.exp = 0
    print("{name} levelled up! {name2} is now level {lvl}!".format(name = self.name, name2 = self.name, lvl= self.level))
    #  Call evolve if level matches or is greater than self.next_evolution
    if self.next_evolution != -1 and self.level >= self.next_evolution:
            self.evolve()

#  Trainer class definition
class Trainer:
  def __init__(self, name, pokemon, potions, current_active):
    self.name = name
    self.poke_list = pokemon
    self.potions = potions
    self.current_active = 0
    
  def __repr__(self):
        # Prints the name of the trainer, the pokemon/pokemon levels they currently have, and the current active pokemon.
        print("The trainer {name} has the following pokemon:".format(name = self.name))
        for pokemon in self.poke_list:
            print(" " +pokemon.name + " Lvl: " + str(pokemon.level))
        return "The current active pokemon is {name} with {health} health.".format(name = self.poke_list[self.current_active].name, health = self.poke_list[self.current_active].health)
  
  
  #  Use potion on current pokemon
  def use_potion(self, potion):
    if self.potions > 0:
      self.potions -= potion
      print('You used a potion on {pokemon}.'.format(pokemon = self.poke_list[self.current_active].name))
      #Revive Pokemon if it's health is 0
      if self.poke_list[self.current_active].health == 0:
        self.poke_list[self.current_active].revive()
      #Potion cannot increase health beyond health max
      elif self.poke_list[self.current_active].health > self.poke_list[self.current_active].max_health:
        self.poke_list[self.current_active].health = self.poke_list[self.current_active].max_health
      elif self.poke_list[self.current_active].health > 0 :
        self.poke_list[self.current_active].gain_health(20)
    else:
      print('You have no potions to use.')
        
  def other_attack(self, opp_trainer):
    # Get current pokemon ready
      trainer_current_active = self.poke_list[self.current_active]
      opp_current_active = opp_trainer.poke_list[opp_trainer.current_active]
      trainer_current_active.attack(opp_current_active)
    #  Check if opponent pokemon is already knocked out
      if opp_current_active.fainted_not_healed == True:
           print("{} cannot be attacked, {} is knocked out. Opponent must switch pokemon".format(opp_current_active.name, opp_current_active.name))
  #   If knocked opp pokemon knocked out from attack trainer pokemon gains xp
      elif opp_current_active.fainted:
         trainer_current_active.gain_xp(opp_current_active)
         opp_current_active.fainted_not_healed = True

  def special_move_attack(self, opp_trainer):
    # Check if pokemon has a special move
    if self.poke_list[self.current_active].special_move == "": 
      print("{} has not learned a special move".format(self.poke_list[self.current_active].name))
    elif self.poke_list[self.current_active].special_move != "":
     self.poke_list[self.current_active].special_attack(opp_trainer.poke_list[opp_trainer.current_active])
    #  Check if pokemon is still fainted, can't attack until healed 
    if opp_trainer.poke_list[opp_trainer.current_active].fainted_not_healed == True:
           print("{} cannot be attacked, {} is knocked out. Opponent must switch pokemon".format(opp_trainer.poke_list[opp_trainer.current_active].name, opp_trainer.poke_list[opp_trainer.current_active].name))
#  If opp pokemon knocked out from special attack, trainer pokemon gains xp
    elif opp_trainer.poke_list[opp_trainer.current_active].fainted:
         self.poke_list[self.current_active].gain_xp(opp_trainer.poke_list[opp_trainer.current_active])
         opp_trainer.poke_list[opp_trainer.current_active].fainted_not_healed = True
  
 
  #Switch current pokemon to another in your list
  def switch_current_pokemon(self, new_pokemon):
    if new_pokemon <= len(self.poke_list) and new_pokemon >= 0:
      #You cannot switch to a knocked out Pokemon
      if self.poke_list[new_pokemon].fainted:
        print('{pokemon} is knocked out. Choose another Pokemon.'.format(pokemon = self.poke_list[new_pokemon].name))
      #You cannot switch to your current Pokemon
      elif self.poke_list[new_pokemon] == self.poke_list[self.current_active]:
        print('Choose another Pokemon. {pokemon} is already your current Pokemon.'.format(pokemon = self.poke_list[new_pokemon].name))
      #Switch to a new Pokemon in your list
      elif self.poke_list[new_pokemon] != self.poke_list[self.current_active]:
        past_active = self.poke_list[self.current_active].name
        past_active_health = self.poke_list[self.current_active].health
        self.current_active = new_pokemon
        print("{past} returned to backpack with {hp} health. Go {pokemon}, you\'re up!'".format(past = past_active, hp = past_active_health, pokemon = self.poke_list[self.current_active].name))

# Charmander class with evolutions
class Charmander(Pokemon):
  def __init__(self, level = 5, special_move = "Flamethrower"):
    super().__init__("Charmander", level, "Fire", 65, special_move)

# Squirtle class with evolutions
class Squirtle(Pokemon):
  def __init__(self, level = 5, special_move = "Bubble gun"):
    super().__init__("Squirtle", level, "Water", 43, special_move)
   

# Bulbasaur class with evolutions
class Bulbasaur(Pokemon):
  def __init__(self, level = 5, special_move = "Razor leaf"):
   super().__init__("Bulbasaur", level, "Grass", 45, special_move)


#POKEMON TO PLAY
# Charmander, Squirtle and Bulbasaur initilized with level 34 to test evolutions
Charmander = Charmander(level = 34)
Squirtle = Squirtle(level = 34)
Bulbasaur = Bulbasaur(level = 34)
Scorbunny = Pokemon("Scorbunny", 6, "Fire", 69)
Staryu = Pokemon("Staryu", 10, "Water", 85)
Lotad = Pokemon('Lotad', 7, 'Grass', 30)

#TRAINERS TO PLAY
#Initialize two trainers with three pokemon each, ten potions, current active pokemon
harryPoke = [Charmander, Scorbunny, Bulbasaur]
mistyPoke = [Staryu, Squirtle, Lotad]
harry = Trainer("Harry", harryPoke, 10, 0)
misty = Trainer("Misty", mistyPoke, 10, 0)

# Show current trainer with pokemon levels
print(harry)
print(misty)

#Testing normal attacks
misty.other_attack(harry)
harry.other_attack(misty)

# Switch pokemon
misty.switch_current_pokemon(1)
harry.switch_current_pokemon(2)

# Testing special move attack 
harry.special_move_attack(misty)
misty.special_move_attack(harry)

# Testing potions
misty.use_potion(1)
harry.use_potion(1)

# Testing evolutions
Charmander.level_up()
Charmander.level_up()
Bulbasaur.level_up()
Squirtle.level_up()
Squirtle.level_up()

print(Charmander)
print(Squirtle)
print(Bulbasaur)

# check attacks with evolutions
misty.other_attack(harry)
harry.special_move_attack(misty)
