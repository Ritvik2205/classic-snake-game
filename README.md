# Snake Game in Python
#### Video Demo: [Youtube Video Link](https://youtu.be/5CRqRtdqa3w)
#### Description:

##### What the program is about:
This is a version of the classic snake game where the user controls a snake and captures/ eats the food that randomly appears on the display screen.

The snake is one unit length at the beginning and increases by one unit everytime it eats a piece of food.

The game can get over in **2 ways**:
- Either your snake exits the map.
- Or the snake's body touches itself (you are basically eating yourself)

If you lose through one of the 2 ways above, you get prompted with **2 messages**:
- First it says your score for the round.
- Second, it asks you to enter either 'A' or 'Q':
    * The 'A' is if you want to play again.
    * The 'Q' is if you want to quit and it exits the program


##### Included Functions:

###### `the_score(score)`:
- It takes a `score` argument which is a variable that calculates your score.
- It displays the score on the top left corner of the screen.

###### `the_snake(snake_block, snake_list)`:
- It takes 2 arguments `snake_block` and `snake_list`. 
- It displays the user's snake and updates its length everytime the list `snake_list` changes.

###### `message(msg, colour)`:
- It takes 2 arguments: `msg` i.e. the message to display and `colour` i.e. the colour of the message you want to display.
- It first render the font_style for the message.
- It then displays the message at a fixed location on the display.

###### `main()`:
- It first introduces some variables that will be used later on.
- It then uses the function `random.randrange` to randomize the position of the food's x and y coordinates between the display screen.
- It then introduces a loop, which runs only when the `game_over` boolean value is False i.e _when the game is not over_.
- It then introduces another loop, which runs when the `game_close` bool is True i.e. the user lost the round through one of the 2 possible ways.
    * The loop displays the losing message, displays the score and tests for the key press between 'A' and 'Q'.
- It then introduces another loop outside the previous one which tests for keypresses and allows the snake to move using the arrow keys or close the display using the _close button_.
- Next is an **if condition** which checks if the snake out of the display and "closes" the game accordingly.
- Next are some calculations which allow the snake to move by changing its coordinates, draws the food particles, increases the snake length!
- It then has an if statement which checks if the snake _ate_ itself, i.e. if the `snake_head` touched the snake's body.
- It then runs the `the_snake` function to display the snake accordingly, updates the score, and updates the display.
- It then checks whether the snake _ate_ the food and increases the snake's length.
- Then outside the _"main"_ loop, i.e. if the `game_over` bool is True, it quits pygame and the whole program.