
from Board import Board
from Blocks import Blocks
from solver import solve_lazor_game
# from solver import solve_lazor_game_1
from read_bff import readf_bff
from compute_lazor_paths import compute_lazor_paths
import os
import time
#-----------------------------test add board--------------------------
# from Board import Board

# # 模拟的初始棋盘
# original_board = [
#     ['o', 'B', 'x', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o'],
#     ['o', 'x', 'o', 'o', 'o'],
#     ['o', 'x', 'o', 'o', 'x'],
#     ['o', 'o', 'x', 'x', 'o'],
#     ['B', 'o', 'x', 'o', 'o']
# ]

# # 创建 Board 实例
# game = Board(original_board)

# # 展示初始化的块布局
# print("Initial Block Layout:")
# game.display_board()

# # 尝试在空位置放置块
# try:
#     game.place_blocks((0, 0), 'A')  # 应该成功
#     game.place_blocks((1, 1), 'C')  # 应该成功
# except ValueError as e:
#     print("Error:", e)

# # 尝试在已占用位置放置块
# try:
#     game.place_blocks((0, 1), 'A')  # 应该报错，因为 (0, 1) 是 'B'
# except ValueError as e:
#     print("Error:", e)

# # 尝试在受限位置放置块
# try:
#     game.place_blocks((0, 2), 'A')  # 应该报错，因为 (0, 2) 是 'x'
# except ValueError as e:
#     print("Error:", e)

# # 展示放置后的块布局
# print("\nBlock Layout After Placement:")
# game.display_board()

#-------------------------------test for get_interact_block-------------------------
# from Board import Board

# def main():
#     # Initialize a sample board layout
#     original_board = [
#         ['o', 'o', 'A'],
#         ['C', 'o', 'o'],
#         ['x', 'C', 'o']
#     ]

#     # Create a Board instance
#     game = Board(original_board)

#     # Define initial lazor source positions and directions
#     lazor_position = [(1, 0)]   # Lazor starts from boundary point (1, 0)
#     lazor_direction = [(1, 1)]  # Lazor moves diagonally down to the right

#     # Initialize lazor segments on the board
#     game.get_original_lazor(lazor_position, lazor_direction)

#     # Display the initial board layout
#     print("Initial Board Layout:")
#     game.display_board()

#     # Push target points (if any)
#     target_positions = [(2, 1), (0, 3)]
#     game.push_target(target_positions)
#     print("\nTarget Positions:", game.target)

#     # Begin tracking the lazor path
#     print("\nTracking Lazor Path:")
#     current_lazor = game.initial_lazor[0]  # Start with the first lazor segment
#     while current_lazor:
#         try:
#             # Determine the block the lazor will interact with
#             interact_block = game.get_interact_block(current_lazor)
#             if interact_block is None:
#                 print("Lazor out of bounds.")
#                 break  # Lazor is out of the board, stop tracking

#             block_x, block_y = interact_block
#             block = game.blocks_[block_x][block_y]

#             # Execute lazor interaction and obtain resulting paths
#             result_paths = block.lazor_interact(current_lazor)

#             # Display interaction result
#             print(f"At Block ({block_x}, {block_y}) - {block.category}:")
#             for path in result_paths:
#                 if path is not None:
#                     print("Lazor Path:", path)

#             # Check if the lazor path is blocked or needs to continue
#             if result_paths and result_paths[0] is None:
#                 print("Lazor is blocked.")
#                 break
#             elif result_paths and result_paths[0] is not None:
#                 current_lazor = result_paths[0]  # Move to the next lazor path
#             else:
#                 break  # No valid path, end tracing
#         except ValueError as e:
#             print(f"Error: {e}")
#             break

#     # Display final board layout with any changes made
#     print("\nFinal Board Layout after Lazor Path Tracking:")
#     game.display_board()

# # Run the main function to test the Board class
# if __name__ == "__main__":
#     main()

#-------------------------test again----------------------------------------------------------
# from Board import Board

# def main():
#     # Initialize a sample board layout
#     original_board = [
#         ['o', 'o', 'A'],
#         ['C', 'o', 'o'],
#         ['x', 'C', 'o']
#     ]

#     # Create a Board instance
#     game = Board(original_board)

#     # Define initial lazor source positions and directions
#     lazor_position = [(0, 1)]   # Lazor starts from boundary point (1, 0)
#     lazor_direction = [(1, 1)]  # Lazor moves diagonally down to the right

#     # Initialize lazor segments on the board
#     game.get_original_lazor(lazor_position, lazor_direction)

#     # Display the initial board layout
#     print("Initial Board Layout:")
#     game.display_board()

#     # Push target points (if any)
#     target_positions = [(2, 1), (0, 2)]
#     game.push_target(target_positions)
#     print("\nTarget Positions:", game.target)

#     # Initialize lazor tracking queue with the initial lazor segments
#     lazor_queue = list(game.initial_lazor)
#     max_steps = 100
#     step_count = 0

#     # Begin tracking the lazor path
#     print("\nTracking Lazor Path:")
#     while lazor_queue and step_count < max_steps:
#         current_lazor = lazor_queue.pop(0)  # Take the next lazor path to process
#         step_count += 1

#         try:
#             # Determine the block the lazor will interact with
#             interact_block = game.get_interact_block(current_lazor)
#             if interact_block is None:
#                 print("Lazor out of bounds.")
#                 continue  # Lazor is out of the board, skip to next lazor

#             block_y, block_x = interact_block
#             block = game.blocks_[block_y][block_x]

#             # Execute lazor interaction and obtain resulting paths
#             result_paths = block.lazor_interact(current_lazor)

#             # Display interaction result
#             print(f"At Block ({block_x}, {block_y}) - {block.category}:")
#             for path in result_paths:
#                 if path is not None:
#                     print("Lazor Path:", path)

#             # Check if the lazor path is blocked or add new paths to queue
#             for path in result_paths:
#                 if path is not None:
#                     lazor_queue.append(path)  # Add each resulting path to the queue
#                 else:
#                     print("Lazor is blocked at", (block_y, block_x))

#         except ValueError as e:
#             print(f"Error: {e}")
#             break

#     # If the loop exits because of max steps, notify the user
#     if step_count >= max_steps:
#         print("\nStopped tracking lazor path after reaching the maximum step count to prevent infinite loop.")

#     # Display final board layout with any changes made
#     print("\nFinal Board Layout after Lazor Path Tracking:")
#     game.display_board()

# # Run the main function to test the Board class
# if __name__ == "__main__":
#     main()

#-------------------------------test compute_lazor_paths-----------------------------------------
# from read_bff import readf_bff
# from Board import Board
# from compute_lazor_paths import compute_lazor_paths  # 确保已导入 compute_lazor_paths 函数

# # 读取 bff 文件中的配置
# original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff(r'bff_files\numbered_6.bff')

# # 输出读取的初始配置信息
# print("Block Counts - A:", A_num, "B:", B_num, "C:", C_num)
# print("Lazor Positions:", lazor_position)
# print("Lazor Directions:", lazor_direction)
# print("Target Positions:", target)

# # 输出棋盘的尺寸
# num_rows = len(original_board)
# num_columns = len(original_board[0])
# print("Board Dimensions:", num_rows, "x", num_columns)

# # 创建 Board 对象并初始化目标
# game = Board(original_board)
# game.push_target(target)
# print("Targets Set:", game.target)

# # 初始化初始激光路径
# game.get_original_lazor(lazor_position, lazor_direction)

# # 使用 compute_lazor_paths 计算所有激光路径
# updated_board = compute_lazor_paths(game)

# # 输出所有计算的激光路径
# print("\nAll Computed Lazor Paths:")
# for path in updated_board.all_lazor:
#     print(path)

# # 最终输出棋盘布局以验证结果
# print("\nFinal Board Layout after Lazor Path Computation:")
# updated_board.display_board()

#-----------------------------------------test check_targets_reached------------------------------
from Board import Board

def test_check_targets():
    # 创建一个简单的棋盘布局
    original_board = [
        ['o', 'o', 'o'],
        ['o', 'A', 'o'],
        ['o', 'o', 'o']
    ]
    
    # 初始化 Board 对象
    game = Board(original_board)

    # 设置目标位置
    target = [(0, 1), (2, 1)]  # 假设目标在 (0, 1) 和 (2, 1)
    game.push_target(target)
    
    # 手动设置激光路径列表
    lazor_list = [
        (0, 0, 1, 1),  # 从 (0, 0) 到 (1, 1)
        (1, 1, 2, 1),  # 从 (1, 1) 到 (2, 1)
        (1, 1, 0, 1)   # 从 (1, 1) 到 (0, 1)
    ]
    
    # 设置 lazor_path 到 all_lazor 中
    game.all_lazor = lazor_list

    # 检查目标是否全部被击中
    if game.check_targets_reached():
        print("All targets are reached!")
    else:
        print("Some targets are still not reached.")

# 运行测试
# test_check_targets()

#-----------------------------test 2-------------------
from Board import Board

def test_check_targets_partial_hit():
    # 创建一个简单的棋盘布局
    original_board = [
        ['o', 'o', 'o'],
        ['o', 'A', 'o'],
        ['o', 'o', 'o']
    ]
    
    # 初始化 Board 对象
    game = Board(original_board)

    # 设置目标位置
    target = [(0, 1), (2, 1)]  # 目标在 (0, 1) 和 (2, 1)
    game.push_target(target)
    
    # 手动设置激光路径列表，使其只击中一个目标
    lazor_list = [
        (0, 0, 1, 1),  # 从 (0, 0) 到 (1, 1)
        (1, 1, 0, 1)   # 从 (1, 1) 到 (0, 1) - 击中 (0, 1)
        # 注意：缺少击中 (2, 1) 的路径
    ]
    
    # 设置 lazor_path 到 all_lazor 中
    game.all_lazor = lazor_list

    # 检查目标是否全部被击中
    if game.check_targets_reached():
        print("All targets are reached!")
    else:
        print("Some targets are still not reached.")

# 运行测试
# test_check_targets_partial_hit()

#---------------------------test solver---------------------------------
# def main():
#     # 读取 .bff 文件数据    
#     original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff("bff_files/mad_1.bff")
    
#     # 创建 Board 实例并设置初始数据
#     game_board = Board(original_board, A_num, B_num, C_num)
#     game_board.get_original_lazor(lazor_position, lazor_direction)
#     game_board.push_target(target)
    
#     # 计算激光路径
#     compute_lazor_paths(game_board)
    
#     # 显示初始棋盘
#     print("Initial Board Layout:")
#     game_board.display_board()
    
#     # 输出所有激光路径
#     print("\nAll Lazor Paths:")
#     for path in game_board.all_lazor:
#         print(f"Lazor segment: {path}")
    
#     # 检查目标是否被击中
#     all_targets_reached = game_board.check_targets_reached()
#     if all_targets_reached:
#         print("\nAll targets have been hit by the lazors!")
#     else:
#         print("\nNot all targets were hit. Try different block placements.")

#     # 清除棋盘上的块状态（如果需要）
#     game_board.clear_blocks()

# if __name__ == "__main__":
#     main()

#--------------------------------------test solver on a single file-----------------------------
# def main():
#     # 读取 .bff 文件并初始化游戏
#     original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff("bff_files/tiny_5.bff")
#     # print(target)
#     game_board = Board(original_board, A_num, B_num, C_num)
#     # game_board.generate_initial_lazor(lazor_position, lazor_direction)
#     game_board.push_target(target)

#     # 求解游戏
#     solved_board = solve_lazor_game(game_board, A_num, B_num, C_num, lazor_position, lazor_direction, target)
    
#     print(solved_board.all_lazor)

#     if solved_board:
#         # print("\nSolved Board Layout:")
#         solved_board.display_board()
#     else:
#         print("No solution could satisfy all target conditions.")

# if __name__ == "__main__":
#     main()

#--------------------------------------solve all the files at once----------------------------------------------
def main():
    # 获取 bff_files 文件夹中的所有 .bff 文件
    folder_path = "bff_files"
    bff_files = [f for f in os.listdir(folder_path) if f.endswith('.bff')]
    
    # 遍历每个 .bff 文件
    for bff_file in bff_files:
        print(f"\nTesting {bff_file}...")
        file_path = os.path.join(folder_path, bff_file)
        
        # 读取 .bff 文件并初始化游戏
        original_board, A_num, B_num, C_num, lazor_position, lazor_direction, target = readf_bff(file_path)
        game_board = Board(original_board, A_num, B_num, C_num)
        game_board.push_target(target)
        
        # 记录开始时间
        start_time = time.time()
        
        # 求解游戏
        solved_board = solve_lazor_game(game_board, A_num, B_num, C_num, lazor_position, lazor_direction, target)
        
        # 记录结束时间并计算总运行时间
        end_time = time.time()
        duration = end_time - start_time
        
        # 输出结果
        if solved_board:
            print(f"\n{bff_file} solved in {duration:.2f} seconds.")
            solved_board.display_board()
        else:
            print(f"{bff_file} could not be solved within the given constraints. Took {duration:.2f} seconds.")
    
if __name__ == "__main__":
    main()

#-------------------test new lazor calculate------------------------
# from Board import Board
# from compute_lazor_paths import compute_lazor_paths

# def test_lazor_path():
#     # Define the board configuration from the grid
#     original_board = [
#         ['A', 'B', 'A'],
#         ['o', 'o', 'o'],
#         ['A', 'C', 'o']
#     ]
    
#     # Define the number of each block type (in this setup, we won’t place any new blocks)
#     A_num, B_num, C_num = 0, 0, 0

#     # Define the laser starting position and direction
#     lazor_position = [(4, 5)]
#     lazor_direction = [(-1, -1)]

#     # Define target positions
#     target = [(1, 2), (6, 3)]

#     # Initialize the board
#     game_board = Board(original_board, A_num, B_num, C_num)
#     game_board.push_target(target)

#     # Compute the laser paths
#     solved_board = compute_lazor_paths(game_board, lazor_position, lazor_direction)

#     # Check results
#     if solved_board.check_targets_reached():
#         print("\nLaser successfully hit all targets.")
#     else:
#         print("\nLaser did not hit all targets.")
    
#     # Display final board layout
#     solved_board.display_board()
#     print("Laser paths traced:", solved_board.all_lazor)

# if __name__ == "__main__":
#     test_lazor_path()
