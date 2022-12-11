import os.path

##########################################################################
#                             GOAL CLASS                                 #
##########################################################################


class Goal:
    """ create a goal for the game. In each game you can choose a 
    goal which contains a specific amount of gold and XP you need to collect 
    """
    

    def __init__(
        self, 
        goal_name: str, 
        total_quest_days: int, 
        gold_goal: int, 
        animal_xp_goal: int, 
        dex_xp_goal: int, 
        entertainment_xp_goal: int, 
        job_name: str,
        town_name: str,
        file: str,
        saved_game_list: list
        ):
        
        self.goal_name = goal_name
        self.total_quest_days = total_quest_days
        self.gold_goal = gold_goal
        self.animal_xp_goal = animal_xp_goal
        self.dex_xp_goal = dex_xp_goal
        self.entertainment_xp_goal = entertainment_xp_goal
        self.job_name = job_name
        self.town_name = town_name
        self.file = file
        self.saved_game_list = saved_game_list


    def __str__(self):
        """ print the goal that is chosen """
        return (
        f"\n-------------------------------------------"
        f"-----------------------------------------------\n"
        f"The goal you chose is: {self.goal_name}. In total, "
        f"you have {self.total_quest_days} days to achieve this goal,\n"
        f"and in order to do this you will have to collect a sufficient "
        f"amount of gold,\nand enough XP of various types. This is what "
        f"you need:\n\n- {self.gold_goal} gold\n- {self.animal_xp_goal} "
        f"animal XP\n- {self.dex_xp_goal} dexterity XP\n- "
        f"{self.entertainment_xp_goal} entertainment XP\n"
        f"------------------------------------------------"
        f"------------------------------------------\n"
        )


    def get_goal_name(self):
        return self.goal_name

    def get_total_quest_days(self):
        return self.total_quest_days
    
    def set_total_quest_days(self, total_quest_days):
        self.total_quest_days = total_quest_days

    def set_saved_quest_days(self, saved_quest_days):
        self.set_saved_quest_days = saved_quest_days

    def get_gold_goal(self):
        return self.gold_goal

    def set_gold_goal(self, gold_goal):
        self.gold_goal = gold_goal

    def get_animal_xp_goal(self):
        return self.animal_xp_goal

    def set_animal_xp_goal(self, animal_xp_goal):
        self.animal_xp_goal = animal_xp_goal

    def get_animal_xp(self):
        return self.animal_xp

    def get_dex_xp_goal(self):
        return self.dex_xp_goal        
    
    def set_dex_xp_goal(self, dex_xp_goal):
        self.dex_xp_goal = dex_xp_goal        

    def get_dex_xp(self):
        return self.dex_xp

    def get_entertainment_xp_goal(self):
        return self.entertainment_xp_goal        

    def set_entertainment_xp_goal(self, entertainment_xp_goal):
        self.entertainment_xp_goal = entertainment_xp_goal

    def set_entertainment_xp(self, entertainment_xp):
        self.entertainment_xp = entertainment_xp     

    def get_job_name(self):
        return self.job_name

    def set_job_name(self, job_name: str):
        self.job_name = job_name

    def get_town_name(self):
        return self.town_name
   
    def set_town_name(self, town_name: str):
        self.town_name = town_name

    def get_file(self):
        return self.file

    def set_file(self, file: str):
        self.file = file

    def get_saved_game_list(self):
        return self.saved_game_list

    def set_saved_game_list(self, saved_game_list: list):
        self.saved_game_list = saved_game_list
    

    def set_goal_values(self, goal_name):
        """ after asking the user what goal they want to choose for the game, 
        this method sets the related statistics as the goal of the current game 
        """

        if goal_name == "buy horse":
            self.set_total_quest_days(7)
            self.set_gold_goal(300)
            self.set_animal_xp_goal(30)
            self.set_dex_xp_goal(10)
            self.set_entertainment_xp_goal(0)

        elif goal_name == "get own house":
            self.set_total_quest_days(10)
            self.set_gold_goal(400)
            self.set_animal_xp_goal(0)
            self.set_dex_xp_goal(50)
            self.set_entertainment_xp_goal(0)

        elif goal_name == "buy lute":
            self.set_total_quest_days(9)
            self.set_gold_goal(200)
            self.set_animal_xp_goal(0)
            self.set_dex_xp_goal(10)
            self.set_entertainment_xp_goal(60)


##########################################################################
#                              CHOOSE TOWN                               #
##########################################################################


    def choose_travel_destination(self):
        """ every in-game day, the program asks the user to what town the user wants to go """
        
        while True: 
            town_name = input(
            "\nTo which town would you like to travel today? "
            f"You can choose between Novigrad, Oxenfurt, "
            f"Vengerberg, Brugge and Hengfors: "
            )

            if town_name not in (
            "Novigrad", 
            "Oxenfurt", 
            "Vengerberg", 
            "Brugge", 
            "Hengfors"
            ):
                
                if town_name == "quit":
                    print(
                    "\nYou have quit the game, thank you for playing. "
                    f"Come back soon to play again!\n"
                    )

                    exit()
                
                else:
                    print(
                    "\nPlease pick one of the available options.\n"
                    )
                
            else:
                break

        self.set_town_name(town_name)


##########################################################################
#                               CHOOSE JOB                               #
##########################################################################


    def choose_job(self, character, town_name):
        """ in every town, there are certain jobs available. 
        Each town has a small story. The player can choose a job. 
        Not every town has the same jobs available. 
        """

        while True:
            if town_name == "Novigrad":
                job_name = input(
                f"\n\nBe welcome to {town_name}, {character.character_title} "
                f"{character.name}!\nAny hard worker is greeted warmly here. "
                f"What kind of job would you be interested\nin today? You "
                f"can choose between farming, monster killing, juggling and singing: "
                )
                
                if job_name not in (
                "farming", 
                "monster killing", 
                "juggling", 
                "singing"
                ):
                
                    if job_name == "quit":
                        print(
                        "\nYou have quit the game, thank you for playing. "
                        f"Come back soon to play again!\n"
                        )

                        exit()
                    
                    else:
                        print(
                        "\nPlease pick one of the available options.\n"
                        )

                else:
                    break

            elif town_name == "Oxenfurt":
                job_name = input(
                f"\n\nWelcome to {town_name}! We are famous for our university, "
                f"where you are able\nto study the seven liberal arts. Many a "
                f"famous bard studied here, and it is an excellent\n"
                f"city to learn the craft. Would you like to practice your "
                f"craft and juggle or sing for us?\nOr would you rather "
                f"do something else? We have hunting, farming, juggling and singing: "
                )

                if job_name not in (
                "hunting", 
                "farming", 
                "juggling", 
                "singing"
                ):

                    if job_name == "quit":
                        print(
                        "\nYou have quit the game, thank you for playing. "
                        f"Come back soon to play again!\n"
                        )

                        exit()
                    
                    else:
                        print(
                        "\nPlease pick one of the available options.\n"
                        )

                else:
                    break

            elif town_name == "Vengerberg":
                job_name = input(
                f"\n\nIn {town_name} you can find mysterious witches and "
                f"formidable sorcerers.\nToday we need someone more mundane, "
                f"though we might have monsters roaming around! Are you\n"
                f"perhaps in need of a job, {character.character_title} "
                f"{character.name}?\nWe have hunting, building, monster "
                f"killing and singing\navailable for you, which job would you like? "
                )

                if job_name not in (
                "hunting", 
                "building", 
                "monster killing", 
                "singing"
                ):

                    if job_name == "quit":
                        print(
                        "\nYou have quit the game, thank you for playing. "
                        f"Come back soon to play again!\n"
                        )

                        exit()
                    
                    else:
                        print(
                        "\nPlease pick one of the available options.\n"
                        )

                else:
                    break

            elif town_name == "Brugge":
                job_name = input(
                f'\n\n{town_name} is well-known for its beautiful old buildings and it '
                f'has many temples. In this coastal city\nthey speak an unusual form of '
                f'Nilfgaardian, called “West-Vlaams”. We could use someone to help us '
                f'build more temples, {character.character_title} {character.name},'
                f'\nthough we also have other jobs on offer: farming, building, '
                f'monster killing and juggling. Take your pick: '
                )

                if job_name not in (
                "farming", 
                "building", 
                "monster killing", 
                "juggling"
                ):

                    if job_name == "quit":
                        print(
                        "\nYou have quit the game, thank you for playing. "
                        f"Come back soon to play again!\n"
                        )

                        exit()
                    
                    else:
                        print(
                        "\nPlease pick one of the available options.\n"
                        )

                else:
                    break

            elif town_name == "Hengfors":
                job_name = input(
                f"\n\n{town_name} is a Skelliger city, where they mainly speak Rutsi. "
                f"This hard-to-understand language is\nsomewhat related to Nilfgaardian,"
                f" though it sounds very different. If you happen to know any Hengfors "
                f"sea-shanties,\nbe welcome to sing them for us! If you rather do "
                f"something else, {character.character_title} {character.name}, "
                f"that is also possible.\nYou can choose between hunting, building, "
                f"monster killing and singing: "
                )

                if job_name not in (
                "hunting", 
                "building", 
                "monster killing", 
                "singing"
                ):

                    if job_name == "quit":
                        print(
                        "\nYou have quit the game, thank you for playing. "
                        f"Come back soon to play again!\n"
                        )

                        exit()
                    
                    else:
                        print(
                        "\nPlease pick one of the available options.\n"
                        )
                else:
                    break

        self.set_job_name(job_name)


##########################################################################
#                                 DO JOB                                 #
##########################################################################


    def do_job(self, character, job_name):
        """ once the player has chosen a job, this method determines how much 
        gold and XP the player earned. Each job has a small introduction.
        """
        
        if job_name == "hunting":
            print(
            f"\n----------------------------------------------"
            f"--------------------------------------------\n"
            f"Hello there, hunter {character.name}! I heard you were in need\n"
            f"of a job. We are in dire need of some food, so could you perhaps\n"
            f"hunt us a couple of rabbits, or a nice fat bird? We would reward"
            f" you handsomely!\n-----------------------------------------"
            f"-------------------------------------------------"
            )

            character.set_gained_gold(50)
            character.set_gained_animal_xp(6)
            character.set_gained_dex_xp(4)
            character.set_gained_entertainment_xp(0)
           
            character.increase_gold_and_xp(job_name)            
        
        elif job_name == "farming":
            print(
            f"\n--------------------------------------------------"
            f"----------------------------------------\nBe welcome to "
            f"this humble farm, {character.character_title} "
            f"{character.name}! We could use your help with the\n"
            f"harvest today. Of course it goes without saying that "
            f"you would not work for free!\n------------------------"
            f"------------------------------------------------------------------"
            )

            character.set_gained_gold(40)
            character.set_gained_animal_xp(7)
            character.set_gained_dex_xp(0)
            character.set_gained_entertainment_xp(0)
           
            character.increase_gold_and_xp(job_name)

        elif job_name == "building":
            print(
            f"\n---------------------------------------------------"
            f"---------------------------------------\nWe are looking "
            f"for someone strong that can help us build a new chicken "
            f"coop.\nWould you be able to do that? We would give you "
            f"more than just some nice fried eggs for lunch!\n"
            f"-----------------------------------------------"
            f"-------------------------------------------"
            )
            
            character.set_gained_gold(40)
            character.set_gained_animal_xp(0)
            character.set_gained_dex_xp(7)
            character.set_gained_entertainment_xp(0)
           
            character.increase_gold_and_xp(job_name)

        elif job_name == "monster killing":
            print(
            f"\n--------------------------------------------------------"
            f"----------------------------------\nPlease help us, "
            f"{character.character_title} {character.name}! More than "
            f"10 people have vanished already, there must be\na "
            f"horrible monster hiding in the forest. Are you able to "
            f"kill it for us? All the families\ninvolved put money "
            f"together for a reward.\n----------------------------"
            f"--------------------------------------------------------------"
            )
            
            character.set_gained_gold(60)
            character.set_gained_animal_xp(4)
            character.set_gained_dex_xp(6)
            character.set_gained_entertainment_xp(0)
           
            character.increase_gold_and_xp(job_name)

        elif job_name == "juggling":
            print(
            f"\n----------------------------------------------------"
            f"--------------------------------------\nGood morrow on "
            f"this good morrow! We are in need of a jester, a juggler who jaunts. "
            f"Please come to our\nperfect party tonight and entertain us. For a "
            f"good reward of course!\n----------------------------------------"
            f"--------------------------------------------------"
            )

            character.set_gained_gold(25)
            character.set_gained_animal_xp(0)
            character.set_gained_dex_xp(4)
            character.set_gained_entertainment_xp(5)
           
            character.increase_gold_and_xp(job_name)

        elif job_name == "singing":
            print(
            f"\n----------------------------------------------------"
            f"--------------------------------------\nAre you perhaps"
            f"\na singer who claps\nalong\nwith a song\nand sings a lovely tune\n"
            f"in the merry month of june?\n\nWe would like to invite you to sing "
            f"for us this eve,\n{character.character_title} {character.name},"
            f"\nand we would pay you even before you leave.\n"
            f"---------------------------------------------------"
            f"---------------------------------------"
            )

            character.set_gained_gold(35)
            character.set_gained_animal_xp(0)
            character.set_gained_dex_xp(0)
            character.set_gained_entertainment_xp(9)
           
            character.increase_gold_and_xp(job_name)

        # calculate remaining needed gold and XP, if < 0, value = 0
        gold_still_needed = character.goal.gold_goal - character.gold
        if gold_still_needed < 0:
            gold_still_needed = 0

        animal_xp_still_needed = character.goal.animal_xp_goal - character.animal_xp
        if animal_xp_still_needed < 0:
            animal_xp_still_needed = 0

        dex_xp_still_needed = character.goal.dex_xp_goal - character.dex_xp
        if dex_xp_still_needed < 0:
            dex_xp_still_needed = 0

        entertainment_xp_still_needed = (
            character.goal.entertainment_xp_goal - character.entertainment_xp
        )
        if entertainment_xp_still_needed < 0:
            entertainment_xp_still_needed = 0


        print(
            f"\nYou still need:\n- {gold_still_needed} gold\n"
            f"- {animal_xp_still_needed} animal XP\n"
            f"- {dex_xp_still_needed} dex XP\n"
            f"- {entertainment_xp_still_needed} entertainment XP"
            )


    def save_game_progress(self, character, file):
        """ this method saves the current statistics of 
        the character, thus saving the game 
        """
        
        saved_game_list = [
        character.goal.goal_name,
        character.name,
        character.character_title,
        character.current_quest_day,
        character.gold,
        character.animal_xp,
        character.dex_xp,
        character.entertainment_xp
        ]

        path = os.path.expanduser("~")
        filename2 = path + "/" + file

        try:
            file = open(filename2, "w")
            for item in saved_game_list:
                file.write(f"{item}\n")
        except:
            print(
            f"Failed to save your game progress in file '{file}'.\n\n"
            f"The game has quit automatically, thank you for playing. "
            f"Come back soon to play again!"
            )

            exit()

        finally:
            file.close()


    def game_won_or_lost(self, character):
        """ In this method, the gold and XP acquired by the player are compared to
        the goal values of their chosen goal. The method checks if the goal 
        of the current game has been achieved.
        If yes, it will print a "win" message, otherwise a "lost" message.
        It also prints the statistics of your character at the end of the game 
        """
        
        if  character.gold >= self.gold_goal:
            gold_goal_reached = True
        else:
            gold_goal_reached = False

        if character.animal_xp >= self.animal_xp_goal:
            animal_goal_reached = True
        else:
            animal_goal_reached = False

        if character.dex_xp >= self.dex_xp_goal:
            dex_goal_reached = True
        else:
            dex_goal_reached = False

        if character.entertainment_xp >= self.entertainment_xp_goal:
            entertainment_goal_reached = True
        else:
            entertainment_goal_reached = False

        if (gold_goal_reached == True and 
            animal_goal_reached == True and 
            dex_goal_reached == True and 
            entertainment_goal_reached == True
            ):
            print(
            f'Good morning, {character.character_title} {character.name}! '
            f'Congratulations, you achieved your goal: '
            f'"{character.goal.goal_name}"\n\n'
            )

        else:
            print(
            f'Good morning, {character.character_title} {character.name}! '
            f'I am sorry to say that you did not manage to achieve your '
            f'goal: "{character.goal.goal_name}."\nFeel free to try '
            f'again any time! You are always welcome here.\n\n'
            )
        
        try:
            path = os.path.expanduser("~")
            file = "saved_game.txt"
            filename2 = path + "/" + file
            file_to_delete = open(filename2, "w")

            file_to_delete.close()

        except:
            print(
            f"The file {file_to_delete} could not be deleted. The game now quits."
            )

            exit()


        print(
        f'You gained:\n- {character.gold} of {self.gold_goal} gold\n'
        f'- {character.animal_xp} of {self.animal_xp_goal} animal XP\n'
        f'- {character.dex_xp} of {self.dex_xp_goal} dexterity XP\n'
        f'- {character.entertainment_xp} of {self.entertainment_xp_goal} '
        f'entertainment XP\n\nThank you for playing! Come back soon to '
        f'play again in the wonderful world of Woianzii\n'
        )