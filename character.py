from goal import (
    Goal
)

from intro import (
    enter_button
)

##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################


# create a character with a name and character title. 
# It keeps track of the amount of gold and experience 
# you have, and the current day of your quest 
class Character:

    def __init__ (self, name: str,
    character_title: str,
    current_quest_day: int,
    gold: int,
    animal_xp: int,
    dex_xp: int,
    entertainment_xp: int):

        self.name = name
        self.character_title = character_title
        self.current_quest_day = current_quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp
        self.goal = self.create_goal()

    # print the status of the character
    def __str__(self):
        return (f"Your character's statistics are:\n\nName: {self.character_title} "
        f"{self.name}\n\nDay: {self.current_quest_day}\nGold: {self.gold}\n\n"
        f"Animal xp: {self.animal_xp}\nDexterity xp: {self.dex_xp}\nEntertainment xp"
        f": {self.entertainment_xp}\n\n----------------------------------------------"
        f"--------------------------------------------\n")

    # enable the program to use the player's chosen name
    def get_name(self):
        return self.name

    # enable the program to use the player's chosen title
    def get_character_title(self):
        return self.character_title

    # these methods keep track of the day of the quest
    def get_current_quest_day(self):
        return self.current_quest_day

    def set_current_quest_day(self, current_quest_day):
        self.current_quest_day += current_quest_day

    # set the amount of gained gold
    def set_gained_gold(self, gained_gold):
        self.gold += gained_gold

    # set the amount of gained animal xp
    def set_gained_animal_xp(self, gained_animal_xp):
        self.animal_xp += gained_animal_xp    

    # set the amount of gained dexterity xp
    def set_gained_dex_xp(self, gained_dex_xp):
        self.dex_xp += gained_dex_xp 

    # set the amount of gained entertainment xp
    def set_gained_entertainment_xp(self, gained_entertainment_xp):
        self.entertainment_xp += gained_entertainment_xp   

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

    # ask the user for their preferred goal: this will get the data 
    # from the chosen goal and set it as the goal for the current game
    def create_goal(self):

        while True:
            goal_name = input('You are able to choose between three goals '
            f'in this game: "buy horse", "get own house" and "buy lute".\n'
            f'Each goal takes a certain number of days to achieve, and has '
            f'a set amount of experience points (xp) and gold you need to collect.'
            f'\n\nType the name of the goal you wish to choose here: ')
        
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
        Goal.get_job_name)

        goal.set_goal_values(goal_name)

        print(goal)

        return goal

    # increase the amount of gold and xp the character has, depending on the job they chose.
    def increase_gold_and_xp(self, job_name):
        enter_button()
        print("(Press enter to do the work)")
        enter_button()
        
        print(f"We are very grateful, {self.character_title} {self.name}, "
        f"for your {job_name} help! Here is your reward:\n")

        print(f"Gold after {job_name}: {self.gold}\n")
        print(f"Animal xp after {job_name}: {self.animal_xp}\n")
        print(f"Dexterity xp after {job_name}: {self.dex_xp}\n")
        print(f"Entertainment xp after {job_name}: {self.entertainment_xp}")
        
        enter_button()
        
        self.set_current_quest_day(1)
        print(f"------------------------------------------------------------------------------------------\n"
        f"You spent the night in the town. It is now the next day.\n"
        f"------------------------------------------------------------------------------------------")