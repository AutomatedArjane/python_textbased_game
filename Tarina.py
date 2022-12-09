from main import (
    create_character,
    print_greeting
)

from intro import (
    enter_button,
    game_intro
)

# starts the introduction of the game
game_intro()

# create a game character called "character" of the class "Character"
character = create_character()
enter_button()

# print the statistics of the character
print(character)
print("Good luck!")

enter_button()

# for the number of days that the chosen quest lasts, this loop will be repeated
for x in range(character.goal.get_total_quest_days()):
    print_greeting(character)
    character.goal.choose_travel_destination()
    character.goal.choose_job(character, character.goal.town_name)
    character.goal.do_job(character, character.goal.job_name)
    enter_button()

character.goal.game_won_or_lost(character)


##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Write a README file
# Complete the program by making sure all functions are called and are in the right location