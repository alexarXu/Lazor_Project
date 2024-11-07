import copy
import time 
from PIL import ImageDraw, Image
from sympy.utilities.iterables import multiset_permutations


def solution_color():
    return {
        0: (200, 200, 200),
        'A': (255, 255, 255),
        'B': (50, 50, 50),
        'C': (255, 0, 0),
        'o': (150, 150, 150),
        'x': (100, 100, 100),
    }


def image_output(solved_board, answer_lazor, lazor_info, holes, filename, block_size=50):
    n_blocks_x = len(solved_board[0])
    n_blocks_y = len(solved_board)
    dim_x = n_blocks_x * block_size
    dim_y = n_blocks_y * block_size
    colors = solution_color()

    # Define the set of valid colors
    valid_colors = set(solution_color().keys())

    # Check if all the board values are valid colors
    if not all(set(row).issubset(valid_colors) for row in solved_board):
        raise ValueError("Invalid board value found!")

    img = Image.new("RGB", (dim_x, dim_y), color=(0, 0, 0))

    for jy in range(n_blocks_y):
        for jx in range(n_blocks_x):
            x = jx * block_size  # calculate x-coordinate of block
            y = jy * block_size  # calculate y-coordinate of block

            # loop through each pixel within the block
            for i in range(block_size):
                for j in range(block_size):
                    # determine the color of the pixel based on the value in the solved board
                    color = colors[solved_board[jy][jx]]

                    # set the color of the pixel at (x+i, y+j) in the image
                    img.putpixel((x + i, y + j), color)

    img_new = ImageDraw.Draw(img)

    for i in range(n_blocks_y - 1):
        y = (i + 1) * block_size
        shape = [(0, y), (dim_x, y)]
        img_new.line(shape, fill=colors.get(0, 0), width=5)

    for i in range(n_blocks_x - 1):
        x = (i + 1) * block_size
        shape = [(x, 0), (x, dim_y)]
        img_new.line(shape, fill=colors.get(0, 0), width=5)

    for i in range(len(lazor_info)):
        lazor_pos = (lazor_info[i][0], lazor_info[i][1])
        img_new.ellipse([lazor_pos[0] * block_size / 2 - 10, lazor_pos[1] * block_size / 2 - 10,
                         lazor_pos[0] * block_size / 2 + 10, lazor_pos[1] * block_size / 2 + 10], fill=(255, 0, 0))

    for i in answer_lazor:
        for point in range(len(i)):
            co_start = (i[point][0] * block_size / 2,
                        i[point][1] * block_size / 2)
            if point + 1 < len(i):
                co_end = (i[point + 1][0] * block_size / 2,
                          i[point + 1][1] * block_size / 2)
            else:
                co_end = co_start
            img_new.line([co_start, co_end], fill=(255, 0, 0), width=5)

    for hole in holes:
        x, y = hole[0] * block_size / 2, hole[1] * block_size / 2
        coordinates = (x - 10, y - 10, x + 10, y + 10)
        img_new = ImageDraw.Draw(img)
        img_new.ellipse(coordinates, fill=(255, 255, 255), outline="red", width=2)

    # Name the result image
    if not filename.endswith(".png"):
        filename = '.'.join(filename.split(".")[0:-1])
        filename += "_solved.png"

    img.save("%s" % filename)

