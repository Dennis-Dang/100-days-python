# US State name game
Provided a political map of the United States, the user will try to guess as many states as they can.
The more states the user can correctly enter, the higher they will score.

## Specifications:
- `50_states.csv` includes data of 50 states in the USA. The X and Y corresponding values are turtle coordinates where the origin is at the center of the map.
- `blank_states_img.gif` is the map of the USA. There are no labels within the states borders. 
  - The image must be a `.gif` format to be compatible with the turtle module.
- Because of the provided csv file, the screen is constrained to a fixed size of the image itself.
- After starting the program, the game will continuously prompt the user in a pop-up panel to type in their guesses.
  - If their guess is spelled correctly, the user will gain a point and the corresponding state label will be marked on the map.
- Conditions to stop the game:
  - When users enters all 50 states.
  - When the user enters "exit"
    - The game will also generate a csv file `states_to_study.csv` containing all states the user failed to enter. 