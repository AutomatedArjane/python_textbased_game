from day_tasks import (
    choose_travel_destination,
    choose_job,
    do_job
)

from main import (
    create_character,
    create_goal,
)

from introduction import (
    enter_button,
    game_intro
)

game_intro()

mycharacter = create_character()
print(mycharacter)

#mycharacter.gain_animal_xp(40)
#mycharacter.get_animal_xp()
#print(mycharacter)

mygoal = create_goal()
print(mygoal)

enter_button()

for x in range(mygoal.get_total_quest_days()):
    mygoal.choose_travel_destination()

#game_won(mycharacter, mygoal)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location