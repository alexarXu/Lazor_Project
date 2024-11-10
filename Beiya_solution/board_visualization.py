'''
This file contains the visualization function to generate the image output of the solved board.
The idea is that the function will draw the blocks, lazors, lazor paths, and targets on the image.
*This file took a reference.
'''
from PIL import ImageDraw, Image

def solution_color():
    '''
    This function returns the color of each block in the solution.
    ***Returns***
    A dictionary with the color of each block.
    The format is {block: (R, G, B)}
    '''
    return {
        0: (225, 225, 225),
        'A': (255, 255, 255),
        'B': (0, 0, 0),
        'C': (0, 0, 255),
        'o': (150, 150, 150),
        'x': (75, 75, 75),
    }

def validate_board(solved_board):
    '''
    This function validates the board.
    ***Parameters***
    solved_board: 2D list, the solved board.
    ***Raises***
    ValueError: If an invalid board value is found.
    '''
    valid_colors = set(solution_color().keys())
    if not all(set(row).issubset(valid_colors) for row in solved_board):
        raise ValueError("Invalid board value found!")

def draw_blocks(img, solved_board, block_size, colors):
    '''
    This function draws the blocks on the image.
    ***Parameters***
    img: Image, the image to draw on.
    solved_board: 2D list, the solved board.
    block_size: int, the size of each block.
    colors: dict, the color of each block.
    '''
    n_blocks_y = len(solved_board)
    n_blocks_x = len(solved_board[0])
    for jy in range(n_blocks_y):
        for jx in range(n_blocks_x):
            x = jx * block_size
            y = jy * block_size
            color = colors[solved_board[jy][jx]]
            for i in range(block_size):
                for j in range(block_size):
                    img.putpixel((x + i, y + j), color)

def draw_grid_lines(img_new, dim_x, dim_y, block_size, colors):
    '''
    This function draws the grid lines on the image.
    ***Parameters***
    img_new: ImageDraw, the image to draw on.
    dim_x: int, the width of the image.
    dim_y: int, the height of the image.
    block_size: int, the size of each block.
    colors: dict, the color of each block.
    '''
    for i in range(dim_y // block_size - 1):
        y = (i + 1) * block_size
        img_new.line([(0, y), (dim_x, y)], fill=colors[0], width=5)
    for i in range(dim_x // block_size - 1):
        x = (i + 1) * block_size
        img_new.line([(x, 0), (x, dim_y)], fill=colors[0], width=5)

def draw_lazors(img_new, lazor_info, block_size):
    '''
    This function draws the lazors on the image.
    ***Parameters***
    img_new: ImageDraw, the image to draw on.
    lazor_info: list, the lazor information.
    block_size: int, the size of each block.
    '''
    for lazor in lazor_info:
        x, y = lazor[0] * block_size / 2, lazor[1] * block_size / 2
        img_new.ellipse([x - 10, y - 10, x + 10, y + 10], fill=(255, 0, 0))

def draw_lazor_paths(img_new, answer_lazor, block_size):
    '''
    This function draws the lazor paths on the image.
    ***Parameters***
    img_new: ImageDraw, the image to draw on.
    answer_lazor: list, the lazor paths.
    block_size: int, the size of each block.
    '''
    for path in answer_lazor:
        for point in range(len(path)):
            co_start = (path[point][0] * block_size / 2, path[point][1] * block_size / 2)
            if point + 1 < len(path):
                co_end = (path[point + 1][0] * block_size / 2, path[point + 1][1] * block_size / 2)
            else:
                co_end = co_start
            img_new.line([co_start, co_end], fill=(255, 0, 0), width=5)

def draw_targets(img_new, targets, block_size):
    '''
    This function draws the targets on the image.
    ***Parameters***
    img_new: ImageDraw, the image to draw on.f
    targets: list, the target points.
    block_size: int, the size of each block.
    '''
    for target in targets:
        x, y = target[0] * block_size / 2, target[1] * block_size / 2
        coordinates = (x - 10, y - 10, x + 10, y + 10)
        img_new.ellipse(coordinates, fill=(0, 0, 0), outline="red", width=2)

def image_output(solved_board, answer_lazor, lazor_info, targets, filename, block_size=50):
    '''
    This function generates the image output.
    ***Parameters***
    solved_board: 2D list, the solved board.
    answer_lazor: list, the lazor paths.
    lazor_info: list, the lazor information.
    targets: list, the target points.
    filename: str, the filename of the image.
    block_size: int, the size of each block.
    '''
    validate_board(solved_board)
    n_blocks_x = len(solved_board[0])
    n_blocks_y = len(solved_board)
    dim_x = n_blocks_x * block_size
    dim_y = n_blocks_y * block_size
    colors = solution_color()

    img = Image.new("RGB", (dim_x, dim_y), color=(0, 0, 0))
    draw_blocks(img, solved_board, block_size, colors)
    img_new = ImageDraw.Draw(img)
    draw_grid_lines(img_new, dim_x, dim_y, block_size, colors)
    draw_lazors(img_new, lazor_info, block_size)
    draw_lazor_paths(img_new, answer_lazor, block_size)
    draw_targets(img_new, targets, block_size)

    if not filename.endswith(".png"):
        filename = '.'.join(filename.split(".")[0:-1]) + "_solution_xby.png"

    img.save(filename)
    # img.show()  # Show the image
