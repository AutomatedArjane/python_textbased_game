class Character:

    def __init__ (self, name, gender, char_status):
        self.name = name
        self.gender = gender
        self.char_status = char_status
    
    def __str__(self):
        stats_list = list(self.char_status.values())
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nGender: {self.gender}\nDay: {stats_list[0]}\nGold: {stats_list[1]}\nXP: {stats_list[2]}\nLevel: {stats_list[3]}" # of {mission_days} quest days" --> add this later

def create_character():

    name = input("What is your name? ")
    
    while True:
        gender = input("How do you wish to be known? Choose male/female/other: ")
        if gender not in ("male", "female", "other"):
            print("Please pick one of the available options.")
        else:
            break
        
    char_status = {"day": 0, "gold": 0, "xp": 0, "level": 0}

    mycharacter = Character(name, gender, char_status)
    return mycharacter

mycharacter = create_character() # this goes to the main file
print(mycharacter) # this goes to the main file