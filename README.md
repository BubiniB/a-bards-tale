# A Bard's Tale - A text adventure game

A Bard's Tale is a text adventure game created in Python. The game is a self written fantasy story about the bard Esmond Covendown and his adventure to rescue a beautiful princess. Players get to make choices throughout the game and will impact the story in their own way. The game features different endings as well, depending on player choices, creating some replayability. The game is played in the Code Institute mock terminal on Heroku and can be enjoyed on any device or operative system. 

This game aims to convey the nostalgic feeling of playing "old school" games. I have added a "text typing" effect, which also helps players to read and follow the story better. There are traps and decisions, which lead to a "Game Over" and will force players to restart their adventure. Overall the target group of this game would be either old school gamers, wanting to experience a little bit of nostalgia or "new school" players, who are curious about experiencing how games were "back in the days".

The game has several rooms or also called scenes, and each scene is its own function. For the game to run, the game flow/story appears in reverse order in the code, which means that the last scene of the game appears first in the code and the first one at the bottom.

One of the things I would like to add in the future is ASCII art to make the game come a little bit more to life and let players be more immersed visually.

![Responsivness Mockup]()

## Features 

The game has several features, such as an introduction and tutorial to the game, input fields for players to make choices, choice validations, different story outcomes and a text typing effect for better readability of the story.

I will go in depth of every feature and some of the code used in this game in this section.

### Existing Features

- __Game structure__

  Before coding the game, a basic flowchart over the game's flow and structure was created on [Lucidchart](https://www.lucidchart.com/). This allowed me to see, which functions, rooms/scenes and outcomes were necessary for the game to feel alive and at the same time not forgetting, which other story elements I wanted to include.

  ![Flowchart from Lucidchart]() 

- __Game start__

  The players will be greeted by the game title. For first time players the tutorial will appear, giving simple instructions on how to play and progress in the game. This is achieved by having a function called tutorial and a global variable called tutorial_shown, which is set to False per default. As long as this variable is set to False the tutorial function will be called, by calling the tutorial function however, the variable will be set to True, which will skip the tutorial for players who already have seen the tutorial before.

  How it looks in the game
  ![Beginning of game]()

  The function
  ![Tutorial function]()

- __Text typing effect__

  When playtesting the game I noticed that it was difficult to follow the story of the game when using print statements as big chunks of text would suddenly appear. I found helpful code on [101computing](https://www.101computing.net/python-typing-text-effect/) for creating this effect. I decided to move the function to a different file to save on code lines, since I had already exceeded the limit of 1000 lines due to story telling. The function was then imported into the main run.py file.
  
  How it looks in the game
  ![Text typing effect]()

  The function
  ![Text typing function]()

  Import
  ![Import]()

- __Game Over and clear console__

  The game_over and clear_console functions are vital parts of this game, since there are many ways for players to reach the end of the game due to the main character dying. It was important to let players be able to choose to restart their adventure, in order to give it another go immediatly or to end the game properly. When restarting the game, the console is cleared, so that it doesn't feel cluttered and overwhelming for players. I found useful help for coding the clear_console function on [TutorialsPoint](https://www.tutorialspoint.com/how-to-clear-python-shell). This function was moved to another file as well in order to save on code lines, and then imported to run.py.

  Game Over ingame
  ![Game Over]()

  The function
  ![Clear console function]()

- __Player inputs__
 
  A vital part of the game are the player choices, affecting the flow and progress of the story, and also the ending. In order to make it easier for players to understand, which choices are to be made, they are prompted before the input field. The input fiel is highlighted by ">>" signs so that players understand that this is where they are supposed to write their answer. All choices are validated and when players choose an option, which isn't prompted they will get a message saying that their choice was invalid. After that the same prompt appears again, reminding the players of the available options. All functions that require player input are based on try statements and if/else statements. Some are nested, since they require checks for if global variables are True or False (depending on previous player choices).

  ![Player input ingame]()

  ![Example function]()

  ![Example 2 function]()

### Features Left to Implement

- I would like to add ASCII art for a visually more appealing experience
- Move story text to (a) different file(s) so that the core code is more legible and not disrupted by all the print statements.

## Testing 

- __Responsiveness__

  Since the game is played in the Code Institute mock up terminal on Heroku, I did not test for how it would work on devices other than desktop.

- __Bugs__

  Bugtesting has been done directly on GitPod, since the console shows error messages immediatly. I have also made use of the "Problems" module on GitPod to eliminate unwanted extra whitespaces and keep track on code line length and amount of used characters per line.

  These bugs were found during testing and have been removed:
  - I forgot to add .lower() after inputs, which resulted in that if I did not spell the valid input choice in lowercase, then it would not accept the input.
  - There was an indentation error in the treasure() function, which meant that the game would crash at that point.
  - I misspelled the global variable two_sisters (forgot to add the letter s at the end), which meant that the game crashed when getting to room_four().
  - I forgot to add a choice variable and the input command with it in evil_witch(), which made the game crash.
  - In game_over() I called upon the variable choice, when it actually was called choice_continue, crashing the game.
  

- __Browser Compatibility__

  - I tested the page on Chrome, Edge, Firefox and Opera. I do not have access to Safari and can therefore not test it on that browser.
  - Everyting is running as expected.

  ![Browser compatibility](/assets/images/readme-img/browser-compatibility-bazinga.png)

- __Lighthouse__

Performance test for desktop 
![Lighthouse desktop index.html](/assets/images/readme-img/lighthouse-desktop.png)   

### Validator Testing 

I used the [PEP8 Code Institute](https://pep8ci.herokuapp.com/#) validator and no error or warnings were found.

![PEP8 testresult]()

### Unfixed Bugs

There are no unfixed bugs. 

## Deployment 

The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - Select "Pages" on the left side bar.
  - Source should be set to "Deploy from a branch" and branch should be set to "main" and folder to "/root".
  - Click on save and wait for page to be deployed (can take several minutes).
  - Refresh page and the link should appear on the top of the 'GitHub pages' page.

The live link can be found here - 


## Credits 

### Code - Coding help

- I found useful help for coding the clear_console function on [TutorialsPoint](https://www.tutorialspoint.com/how-to-clear-python-shell).
- I found useful help for coding the text_typing function on [101computing](https://www.101computing.net/python-typing-text-effect/).
- I generated my GitHub and GitPod from the [Code Institute GitPod template](https://github.com/Code-Institute-Org/p3-template)
- I looked at the ["Love Sandwiches"](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) project for the try statements and validating user input.
- I looked at [W3School's example](https://www.w3schools.com/python/python_variables_global.asp) to refresh my memory on how to use global variables.

### Content 

- I used [Code Institutes template](https://github.com/Code-Institute-Solutions/readme-template) for creating this README.

### Media

- I used [Lucidchart](https://www.lucidchart.com/) for creating my flowchart.