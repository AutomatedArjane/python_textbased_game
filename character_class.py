##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

# create a character with a name and character title. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, character_title: str, current_quest_day: int, gold: int, animal_xp: int, dex_xp: int, entertainment_xp: int):
        self.name = name
        self.character_title = character_title
        self.current_quest_day = current_quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp

    # print the status of the character
    def __str__(self):
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nYour character's title: {self.character_title}\n\nDay: {self.current_quest_day}\nGold: {self.gold}\n\nAnimal xp: {self.animal_xp}\nDexterity xp: {self.dex_xp}\nEntertainment xp: {self.entertainment_xp}\n" # of {mission_days} quest days" --> add this later

    def get_name(self):
        return self.name

    def get_character_title(self):
        return self.character_title

    def get_current_quest_day(self):
        return self.current_quest_day
    
    def get_gold(self):
        return self.gold
    
    def get_animal_xp(self):
        return self.animal_xp
    
    def get_dex_xp(self):
        return self.dex_xp
    
    def get_entertainment_xp(self):
        return self.entertainment_xp
    
    # increase the xp and amount of gold of the character, based on the job they did
    def gain_gold(self, gained_gold: int):
        self.gold += gained_gold
        print(f"You received {self.gained_gold} gold for your work.")

    def gain_animal_xp(self, gained_animal_xp: int):
        self.animal_xp += gained_animal_xp
        print(f"You received {self.gained_animal_xp} animal xp for your hard work.")

    def gain_dex_xp(self, gained_dex_xp: int):
        self.dex_xp += gained_dex_xp
        print(f"You received {self.gained_dex_xp} dexterity xp for your hard work.")

    def gain_entertainment_xp(self, gained_entertainment_xp: int):
        self.entertainment_xp += gained_entertainment_xp
        print(f"You received {self.gained_entertainment_xp} entertainment xp for your hard work.")



##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Get the gain_gold() function and its fellows to work
# 