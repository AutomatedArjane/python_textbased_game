# TTC2010-3033 Web-tekniikat

# This project is completed
##########################################################################
#                                 READ ME                                #
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

    Here is the introduction I use in the game:

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


Installation of Pyton:
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




## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.labranet.jamk.fi/AD1945/ttc2010-3033-web-tekniikat.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.labranet.jamk.fi/AD1945/ttc2010-3033-web-tekniikat/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
