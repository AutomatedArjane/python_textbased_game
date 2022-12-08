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
enter_button()
print(character)
print("Good luck!")

enter_button()

for x in range(character.goal.get_total_quest_days()):
    print_greeting(character)
    character.goal.choose_travel_destination(character)
    print("we start here, let's see if we succeed")
    character.increase_gold_and_xp()
    print("\n\nwe succeeded!\n\n------------------------------------------------------------------------------------------\n")
    enter_button()
    print(character)

#game_won(character, goal)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location