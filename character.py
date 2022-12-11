from goal import (
    Goal
)

from intro import (
    enter_button
)

import os.path

##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################


class Character:
    """ create a character with a name and character title. 
    It keeps track of the amount of gold and experience 
    you have, and the current day of your quest 
    """
    def __init__ (
        self, 
        name: str,
        character_title: str,
        current_quest_day: int,
        gold: int,
        animal_xp: int,
        dex_xp: int,
        entertainment_xp: int,
        file: str):

        self.name = name
        self.character_title = character_title
        self.current_quest_day = current_quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp
        self.goal = self.create_goal()
        self.file = file

    def __str__(self):
        """ print the status of the character """
        return (f"Your character's statistics are:\n\nName: {self.character_title} "
        f"{self.name}\n\nDay: {self.current_quest_day}\nGold: {self.gold}\n\n"
        f"Animal XP: {self.animal_xp}\nDexterity XP: {self.dex_xp}\nEntertainment XP"
        f": {self.entertainment_xp}\n\n----------------------------------------------"
        f"--------------------------------------------\n")

    def get_name(self):
        return self.name

    def get_character_title(self):
        return self.character_title

    def get_current_quest_day(self):
        return self.current_quest_day

    def set_current_quest_day(self, current_quest_day):
        self.current_quest_day += current_quest_day

    def set_gained_gold(self, gained_gold):
        self.gold += gained_gold

    def set_gained_animal_xp(self, gained_animal_xp):
        self.animal_xp += gained_animal_xp    

    def set_gained_dex_xp(self, gained_dex_xp):
        self.dex_xp += gained_dex_xp 

    def set_gained_entertainment_xp(self, gained_entertainment_xp):
        self.entertainment_xp += gained_entertainment_xp   

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

    def create_goal(self):
        """ ask the user for their preferred goal: this will get the data 
        from the chosen goal and set it as the goal for the current game """

        goal_name = ""
        try:
            path = os.path.expanduser("~")
            file = "saved_game.txt"
            filename2 = path + "/" + file

            try:
                file = open(filename2, "r")
            
            except:
                file = open(filename2, "w")

            file = open(filename2, "r")

            while True:
                for item in file:
                    if len(item) > 0:
                        item = item.strip()
                        goal_name = item
                        break
                break

        except:
            print(f"Failed to access file '{file}' while creating your goal.\n\n"
                f"The game has now closed")
            exit()
            
        finally:
            file.close()
        
        while True:
            while True:
                if goal_name == "":
                    goal_name = input('You are able to choose between three goals '
                    f'in this game:\n"buy horse", "get own house" and "buy lute".\n'
                    f'Each goal takes a certain number of days to achieve, and has \n'
                    f'a set amount of experience points (XP) and gold you need to collect.\n'
                    f'\nType the name of the goal you wish to choose here: ')

                    if goal_name == "":
                        pass

                break

            if goal_name not in ("buy horse", "get own house", "buy lute"):
                if goal_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")
            else:
                break
        
        # create a Goal instance called "goal"
        goal = Goal(goal_name,
        Goal.get_town_name,
        Goal.get_total_quest_days,
        Goal.get_gold_goal,
        Goal.get_animal_xp_goal,
        Goal.get_dex_xp_goal,
        Goal.get_entertainment_xp_goal,
        Goal.get_job_name,
        Goal.get_file,
        Goal.get_saved_game_list)

        goal.set_goal_values(goal_name)

        print(goal)

        return goal

    def increase_gold_and_xp(self, job_name):
        """ increase the amount of gold and xp the character has, depending on the job they chose. """
        enter_button()
        print("(Press enter to do the work)")
        enter_button()
        
        print(f"We are very grateful, {self.character_title} {self.name}, "
        f"for your {job_name} help! Here is your reward:\n")

        print(f"- Gold after {job_name}: {self.gold}")
        print(f"- Animal XP after {job_name}: {self.animal_xp}")
        print(f"- Dexterity XP after {job_name}: {self.dex_xp}")
        print(f"- Entertainment XP after {job_name}: {self.entertainment_xp}")
        
        enter_button()
        
        self.set_current_quest_day(1)
        print(f"------------------------------------------------------------------------------------------\n"
        f"You spent the night in the town. It is now the next day.\n"
        f"------------------------------------------------------------------------------------------")