# all variables and functions needed for the story

from day_tasks import (
    choose_travel_destination,
    choose_job,
    do_job
)

from main import (
    create_character,
    create_goal,
)

from introduction import (
    enter_button,
    game_intro
)

from character import (
    Character
)

from goal import (
    Goal
)


##########################################################################
#                              CHOOSE TOWN                               #
##########################################################################

def choose_travel_destination(self):
    
    while True: # add name and character title
        town_name = input(
            f"Good morning, {self.character_title()} {self.name()}! It is currently day "
            f"{self.current_quest_day()} of {self.total_quest_days()} of your quest {self.goal_name()}"
            f"\nTo which town would you like to travel today? "
            f"You can choose between Novigrad, Oxenfurt, Vengerberg, Brugge and Hengfors: "
        )

        if town_name not in ("Novigrad", "Oxenfurt", "Vengerberg", "Brugge", "Hengfors"):
            if town_name == "quit":
                print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                exit()
            
            else:
                print("\nPlease pick one of the available options.\n")
            
        else:
            break

    self.choose_job(town_name)

##########################################################################
#                               CHOOSE JOB                               #
##########################################################################

def choose_job(self, town_name): # OPTIONAL: add bonus xp depending on city and job!
    while True:
        if town_name == "Novigrad": # Add more explanation abouot the city, add name and character title
            job_name = input(f"\n\nWelcome to {town_name}, {self.character_title()} {self.name()}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between farming, killing monsters, juggling and singing: ")
            
            if job_name not in ("farming", "killing monsters", "juggling", "singing"):
                if job_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")

            else:
                break

        elif town_name == "Oxenfurt":
            job_name = input(f"\n\nWelcome to {town_name}! We are famous for our university, where you are able to study the seven liberal arts.\nMany a famous bard studied here, and it is an excellent city to learn the craft. Would you like to practice your craft and juggle\nor sing for us? Or would you rather do something else? We have hunting, farming, juggling and singing: ")

            if job_name not in ("hunting", "farming", "juggling", "singing"):
                if job_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")
            else:
                break

        elif town_name == "Vengerberg":
            job_name = input(f"\n\nIn {town_name} you can find mysterious witches and formidable sorcerers. Today we need someone more mundane,\nthough we might have monsters roaming around! Are you perhaps in need of a job, {self.character_title()} {self.name()}?\nWe have hunting, building, killing monsters and singing available for you, which job would you like? ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                if job_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")

            else:
                break

        elif town_name == "Brugge":
            job_name = input(f'\n\n {town_name} is well-known for its beautiful old buildings and it has many temples. In this coastal city\nthey speak an unusual form of Nilfgaardian, called “West-Vlaams”. We could use someone to help us build more temples,\nthough we also have other jobs on offer: farming, building, killing monsters and juggling. Take your pick: ')

            if job_name not in ("farming", "building", "killing monsters", "juggling"):
                if job_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")

            else:
                break

        elif town_name == "Hengfors":
            job_name = input(f"\n\n{town_name} is a Skelliger city, where they mainly speak Rutsi. This hard-to-understand language is\nsomewhat related to Nilfgaardian, though it sounds very different. If you happen to know any Hengfors sea-shanties,\nbe welcome to sing them for us! If you rather do something else, that is also possible.\nYou can choose between hunting, building, killing monsters and singing: ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                if job_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")
            else:
                break

    self.do_job(job_name)


##########################################################################
#                                 DO JOB                                 #
##########################################################################


def do_job(self, job_name):
    print(f'\nyou entered the do_job function with the job "{job_name}"\n')
    
    gained_gold = 0
    gained_animal_xp = 0
    gained_dex_xp = 0
    gained_entertainment_xp = 0
    
    
    if job_name == "hunting": # add bonus?
        print(f"\n\nHello there, hunter {self.name()}! I heard you were in need of a job. We are in dire need of some food,\nso could you perhaps hunt us a couple of rabbits, or a nice fat bird? We would reward you handsomely!")
        print(f"------------------------------------------------------------------------------------------")
        enter_button()
        gained_gold = 50
        gained_animal_xp = 6
        gained_dex_xp = 4
    
    elif job_name == "farming ":
        print(f"\n\nBe welcome to this humble farm, {self.character_title()} {self.name()}! We could use your help with the\nharvest today. Of course it goes without saying that you would not work for free!")
        print(f"------------------------------------------------------------------------------------------")
        gained_gold = 40
        gained_animal_xp = 7

    elif job_name == "building":
        print(f"\n\nWe are looking for someone strong that can help us build a new chicken coop.\nWould you be able to do that? We would give you more than just some nice fried eggs for lunch!")
        print(f"------------------------------------------------------------------------------------------")
        gained_gold = 40
        gained_dex_xp = 7

    elif job_name == "killing monsters":
        print(f"\n\nPlease help us, {self.character_title()} {self.name()}! More than 10 people have vanished already, there must be\na horrible monster hiding in the forest. Are you able to kill it for us? All the families involved put money together for a reward.")
        print(f"------------------------------------------------------------------------------------------")
        gained_gold = 60
        gained_animal_xp = 4
        gained_dex_xp = 6

    elif job_name == "juggling":
        print(f"\n\nGood morrow on this good morrow! We are in need of a jester, a juggler who jaunts. Please come to our\nperfect party tonight and entertain us. For a good reward of course!")
        print(f"------------------------------------------------------------------------------------------")
        gained_gold = 25
        gained_dex_xp = 4
        gained_entertainment_xp = 5

    elif job_name == "singing":
        print(f"\n\nAre you perhaps\na singer who claps\nalong\nwith a song\nand sings a lovely tune\nin the merry month of june?\n\nWe would like to invite you to sing for us this eve,\n{self.character_title()} {self.name()}, and we would pay you even before you leave.")
        print(f"------------------------------------------------------------------------------------------")
        gained_gold = 35
        gained_entertainment_xp = 9

    self.gain_gold(gained_gold)
    self.gain_animal_xp(gained_animal_xp)
    self.gain_dex_xp(gained_dex_xp)
    self.gain_entertainment_xp(gained_entertainment_xp)
    print("You gained {gained_gold} gold, {gained_animal_xp} animal xp, {gained_dex_xp} dexterity xp and {gained_entertainment_xp} by {job_name}. The people you helped are very grateful!")
    print(self.mycharacter)



##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Get Character.gain_gold(gained_gold) (and the other versions) working
# Add more comments to the code
# OPTIONAL: add bonuses to towns and/or jobs
# OPTIONAL: make the program print everything into a text file

# Done:
# Add town descriptions to the choose_town() function to make them more interesting and unique
# Add job descriptions to the do_job() function