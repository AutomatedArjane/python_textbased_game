# TTC2010-3033 Web-tekniikat

### This project is completed
##########################################################################
###             Woianzii: a text-based pick-your-own-story game
##########################################################################

- A general description of my game:

    - My program is a text-based game, in which you can collect XP 
    and gold in order to achieve a goal you choose. The point of the game
    is to entertain people, and give them some small and fun challenge to do.
    Since it’s quite different from regular games, I think people would be curious
    to play it. There are many choices the player can make, from the name of 
    the character they create and the goal they want to achieve, to the locations 
    they travel to and the job they want to do on each in-game day. The game 
    contains customised greetings for each character, and if a player decides 
    to quit the game at any time, their character and progress are saved automatically.
    When they start the game again, it automatically starts the saved game.

    - Here is the introduction I use in the game:

        ------------------------------------------------------------------------------------------
        WELCOME TO THE FANTASY GAME “WOIANZII"

        This game was completed by Arjane Kerkhoven on 11.12.2022,
        as part of the Ohjelmoinnin Perusteet course at JAMK in Jyväskylä.

        ------------------------------------------------------------------------------------------

        You can play this game with your keyboard. The program will prompt 
        you with a question, and you can type the answer into the console.
        During the game, you go on a quest that you can choose yourself. 
        In order to fulfill this quest, you have to gain enough gold and experience 
        points (divided over 3 categories). Each quest has different end goals.

        ------------------------------------------------------------------------------------------
            
        At the beginning of the game, you are asked to provide some information
        about your character (you can make that up yourself). The game then shows
        you your character and the amount of gold and XP they have (zero is default).
        It also shows you what the current day is. After this, you choose a goal.

        ------------------------------------------------------------------------------------------

        The goal's requirements are shown, and this is where the main part
        of the game starts. For each day of your quest, you can choose a 
        city to visit. Each city has various jobs on offer that can gain you gold and XP.
        Try to choose the jobs that bring you closer to your goal.

        ------------------------------------------------------------------------------------------

        Once the days are up, you have either achieved your goal,
        or you have not. If you did not succeed, you can always try again.

        Good luck!
        Ps. If you want to quit at any time, please type "quit" as a reply
        to any question. Your progress will be saved automatically!

        ------------------------------------------------------------------------------------------
        
        [end of game introduction]

- Installation of Pyton:
    - For this game to run, you need a computer that is capable of running Python, and a terminal to read the text prompts, nothing more.
    - If you don’t have Python on your computer, you can download it here: [download Python](https://www.python.org/downloads/)
    - If you are a mac-user, your computer probably has Python pre-installed. Check this link for instructions: [Python for Mac OS](https://legacy.python.org/download/mac/#:~:text=Python%20comes%20pre-installed%20on%20Mac%20OS%20X%20so,and%20install%20newer%20versions%20alongside%20the%20system%20ones)

- How to download and start the game:
    - Create a folder on your computer in the location you choose, with any name (example name: “Woianzii_game”)
    - You can find the repo from this link: [arjanen-harjoitustyo](https://gitlab.labranet.jamk.fi/AD1945/arjanen-harjoitustyo)
    - Get the HTTPS-link for cloning the repo
    - Open a terminal window by right-clicking on your newly created folder and open it in a terminal window from the menu that appears
    - Type the command “git clone” and paste the HTTPS-link after it, and press enter
    - After the command has been processed, type the command “ls -a” to check if cloning was successful. You should see a folder called “arjanen-harjoitustyo”
    - Open all the files from the folder in Visual Studio Code or another IDE. Start the game by running the file called “main.py” (note: don’t start the game from “game.py” or any other file, this won’t work).
    - The game will be saved automatically in a file called “saved_game.txt”, in your home directory. You don’t need to do anything with this file, it will be created automatically and is emptied after each completed game. You can delete it at any time if you want to.