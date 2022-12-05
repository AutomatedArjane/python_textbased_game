# all variables, functions and classes needed for the story

##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

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

    # increase the xp of the character, and level up if needed
    def gain_xp(self, xp_increase: int):
        self.char_status["xp"] += xp_increase
        if self.char_status["xp"] % 8 == 0: # check if level-up is needed
            self.char_status["level"] = round(self.char_status["xp"] / 8) # level up with the correct amount of levels

##########################################################################
#                           CHARACTER CREATION                           #
##########################################################################

# create a character using the class "Character"
def create_character():

    name = input("What is your name? ") # ask the user for the name of their character
    
    while True: # ask the user for the character's gender, only specific replies are allowed
        gender = input("How do you wish to be known? Choose male/female/other: ")
        if gender not in ("male", "female", "other"):
            print("Please pick one of the available options.")
        else:
            break
        
    char_status = {"day": 0, "gold": 0, "xp": 0, "level": 0} # create the statistics of the character

# create a character "mycharacter"
    mycharacter = Character(name, gender, char_status)
    return mycharacter

##########################################################################
#                           NEXT FUNCTION                                #
##########################################################################
