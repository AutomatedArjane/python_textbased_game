from main import (
    create_character,
    print_greeting
)

from introduction import (
    enter_button,
    game_intro
)

from goal import (
    Goal
)

game_intro()

character = create_character()
enter_button()
print(character)
print("Good luck!")

enter_button()

for x in range(character.goal.get_total_quest_days()):
    print_greeting(character)
    character.goal.choose_travel_destination(character)
    enter_button()
    print(character)
    enter_button()
    #print(Goal.goal)

#game_won(character, goal)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location