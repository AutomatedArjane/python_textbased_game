from main import (
    create_character,
    print_greeting
)

from introduction import (
    enter_button,
    game_intro
)

game_intro()

character = create_character()
print(character)

# somehow print goal

enter_button()

for x in range(character.goal.get_total_quest_days()):
    print_greeting(character)
    character.goal.choose_travel_destination()
    print(character)

#game_won(character, goal)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location