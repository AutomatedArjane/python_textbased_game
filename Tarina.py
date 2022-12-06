from AllFunctions import *
from character_class import *
from goal_class import *

mycharacter = create_character() # this goes to the main file
print(mycharacter) # this goes to the main file
mycharacter.gain_animal_xp(40)
mycharacter.get_char_status()
print(mycharacter)

game_won(mycharacter)