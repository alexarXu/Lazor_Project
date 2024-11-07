# Beiya (Alexa) Xu's branch
This is a branch of Beiya (Alexa) Xu for the lazor project.

## Proposal of the project
Step 1: Read .bff file and grab information\
    input - .bff filepath\
    output - \
    1. original board\
    o o o\
    o o o\
    o x o\
    2. fulfilled grid\
    To make the step size be half block, make each block surrounded by nine 'x'.\
    x x x x x x x\
    x o x o x o x\
    x x x x x x x\
    x o x o x o x\
    x x x x x x x\
    x o x x x o x\
    x x x x x x x\
    3. numbers of each kind\
    A_num: number of reflect blocks\
    B_num: number of opaque blocks\
    C_num: number of refract blocks\
    4. the positions of lasers\
    The position of the start point for the laser like (x, y). \
    If there are multiple lasers, store them in a list. [[x1, y1], [x2, y2], ...]\
    5. the direction of lasers\
    The direction of the laser like (1, 1), (1, -1)...\
    If there are multiple lasers, store them in a list. [[1, 1], [-1, 1], ...]\
    6. the position of target points\
    The position of the target points like (x, y).\
    If there are multiple lasers, store them in a list. [[x1, y1], [x2, y2], ...]\
ATTENTION: \
When read a bff file to grab the settings, we should make sure that every value is in a correct format,\
For positions, they should NOT go beyond the boundaries of the board.\
For directions, they should NOT have a value other than [1, 1], [1, -1], [-1, 1], [-1, -1].\
For blocks in the board, they should NOT be a character other than 'A, B, C, o, x'\
For the numbers of usable blocks, they should NOT be zero.\
 \
 \
Step 2: Define the blocks in all kind (done in class)\
    This class simulates the behavior of a laser when it interacts with different types of blocks. \
    The Block class should contain a function which calculate the direction changes when the laser hit different blocks.\
        A: reflect - reflect\
        B: opaque - stop\
        C: refract - reflect + pass\
        o/x: empty/blank - pass\
ATTENTION:\
The reflection and refraction directions are determined depending on whether the x-coordinate of the laser point is even or odd.\
 \
 \
Step 3: Define the grid that can be used to solve (done in class) \
    This class should be able to convert the grid which generate by the bff filethe to a grid only with the usable position. \
    This is done because of the fixed blocks that are already on the board at the start poin.\
 \
 \
Step 4: Define the laser (done in class) (including (1)The specific ways of the for behaviors. \
                                                    (2)A position which the laser now reaches. \
                                                    (3)The path laser has covered.) \
 \
 \
Step 5: Solve the board. \
        Idea: (1) Generate all the possible permutations of the blocks in board. \
              (2) Calculate path of the laser in each board, see if any of the board can satisfy all the demands. \
              (3) If a board could solve the problem, then stop calculating and save this solution. \
              (4) Convert this grid to board and then visualize it in the game format by using images. \