# Lazor_Project
This repo contains the codes of the Lazor project from Software Carpentry Class.

## How to use the project?
To get the solutions of the Lazor boards, you just need to input a .bff file,
- Then! The solution will be magically displayed! (in two formats)

## What is a .bff file?
.bff file is a kind of setting files that you need to describe the Lazor settings.\
To input a .bff file, you need to have these settings below: \
part 1: GRID \
The format should be: \
"GRID START"\
"o o o x o o"\
"......" \
"o A o B o o"\
"GRID STOP"\
Here, each character represents a kind of room: o represents empty and available room, while x represents unavailable room, \
A, B, C here represent the fixed blocks that have different functions.\
part 2: Available blocks \
The format should be: \
Block kind_Block num, like "A 7" represents 7 reflect blocks available.\
part 3: Laser settings \
The format should be: \
L_x_y_dx_dy, like "L 2 7 1 -1" represents a laser that starts at (2,7), and direction is (1,-1)\
      __________\ +x \
      |         / \
      | \
      | \
      | \
     \|/ +y \
part 4: Target points \
The format should be: \
P_x_y, like "P 2 5" represents a target point which is at (2,5) \
That's all for .bff file! Put it in then have fun!
## What packages do you need for running this project?
To run this project, here are some packages you may need, please follow the codes to install them: \
sympy 1.13.3 - pip install sympy \
And the project can be played in the environment of Python 3.11.5
## Why we have two results?
Just for fun! \
Haha just kidding. If you have done the project running, you will find that Beiya_solution will have a better performance for the more complex board (such as yarn_5.bff) than Zixi_solution. We think it is because of the trick we played in the program. \
The trick is described in the utlis.py in Beiya_solution folder. Try to find it out!

## Contact
If you have any questions, please contact the authors.
Beiya Xu on 11/09/2024
     

