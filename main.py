from play import (
    create_character,
    print_greeting,
    get_old_character_if_it_exists
)

from intro import (
    enter_button,
    game_intro
)

##########################################################################
#                    PLAY THE GAME FROM THIS FILE                        #
##########################################################################

# starts the introduction of the game
game_intro()

# check if the player has saved a previous game
character = get_old_character_if_it_exists()

if character is None:
    character = create_character()

# set the file name for the data of the saved game
character.goal.set_file(character.file)
enter_button()

# print the statistics of the character
print(character)
print("Good luck!")

enter_button()

# for the number of days that the chosen quest lasts, this loop will be repeated
for x in range(character.goal.get_total_quest_days() - character.get_current_quest_day() + 1):
    print_greeting(character)
    character.goal.choose_travel_destination()
    character.goal.choose_job(character, character.goal.town_name)
    character.goal.do_job(character, character.goal.job_name)
    character.goal.save_game_progress(character, character.file)
    enter_button()

# after all the days of the quest have passed, check if the game is won or lost
character.goal.game_won_or_lost(character)