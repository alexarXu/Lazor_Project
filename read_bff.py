
from Board import Board

def readf_bff(file_path):
    '''
    This function reads the .bff file and returns an initialized Board object.
    
    ***Parameters***
    file_path: str, the path of the .bff file.
    
    ***Return***
    Board: An initialized Board object with board, block numbers and type, laser positions, directions, and targets.
    '''
    with open(file_path) as f:
        board = []
        original_board = []
        A_num = 0
        B_num = 0
        C_num = 0
        lazor_position = []
        lazor_direction = []
        target = []

        bff = f.read().splitlines()

        for i in range(len(bff)):
            if bff[i] == "GRID START":
                for j in range(i+1, len(bff)):
                    if bff[j] == "GRID STOP":
                        break
                    else:
                        board.append(bff[j])
            elif len(bff[i]) == 3 and bff[i][0] == "A":
                A_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0] == "B":
                B_num = int(bff[i][2])
            elif len(bff[i]) == 3 and bff[i][0] == "C":
                C_num = int(bff[i][2])
            elif len(bff[i]) != 0 and bff[i][0] == "L":
                lazor = bff[i].split(" ")
                lazor_position.append((int(lazor[1]), int(lazor[2])))
                lazor_direction.append((int(lazor[3]), int(lazor[4])))
            elif len(bff[i]) != 0 and bff[i][0] == "P":
                target.append((int(bff[i][2]), int(bff[i][4])))

    for x in board:
        lists = x.split()
        original_board.append(lists)
    
    # Initialize and return the Board object
    return Board(original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target)
