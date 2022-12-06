##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

# create a character with a name and gender. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, gender: str, char_status: dict):
        self.name = name
        self.gender = gender
        self.char_status = char_status

    # print the status of the character
    def __str__(self):
        stats_list = list(self.char_status.values())
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nGender: {self.gender}\nDay: {stats_list[0]}\nGold: {stats_list[1]}\nXP: {stats_list[2]}\nLevel: {stats_list[3]}" # of {mission_days} quest days" --> add this later

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_char_status(self):
        return self.char_status
    
    # increase the xp of the character, and level up if needed
    def gain_animal_xp(self, animal_xp_increase: int):
        self.char_status["Animal xp"] += animal_xp_increase
        if self.char_status["Animal xp"] % 8 == 0: # check if level-up is needed # IS THIS STILL RELEVANT?????? <--------------------^^^*******ÄÄÄÄ
            self.char_status["Level"] = round((self.char_status["Animal xp"] + self.char_status["Dex xp"] + self.char_status["Entertainment xp"]) / 8) # level up with the correct amount of levels

    def gain_dex_xp(self, dex_xp_increase: int):
        self.char_status["Dex xp"] += dex_xp_increase
        if self.char_status["Dex xp"] % 8 == 0: # check if level-up is needed
            self.char_status["Level"] = round((self.char_status["Animal xp"] + self.char_status["Dex xp"] + self.char_status["Entertainment xp"]) / 8) # level up with the correct amount of levels

    def gain_entertainment_xp(self, entertainment_xp_increase: int):
        self.char_status["Entertainment xp"] += entertainment_xp_increase
        if self.char_status["Entertainment xp"] % 8 == 0: # check if level-up is needed
            self.char_status["Level"] = round((self.char_status["Animal xp"] + self.char_status["Dex xp"] + self.char_status["Entertainment xp"]) / 8) # level up with the correct amount of levels                        
