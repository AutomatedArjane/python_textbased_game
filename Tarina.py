from AllFunctions import *
from character_class import *
from goal_class import *

game_intro()

mycharacter = create_character()
print(mycharacter)

#mycharacter.gain_animal_xp(40)
#mycharacter.get_animal_xp()
#print(mycharacter)

mygoal = create_goal()
print(mygoal)

for x in range(mygoal.get_total_quest_days()):
    choose_travel_destination()

#game_won(mycharacter, mygoal)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location