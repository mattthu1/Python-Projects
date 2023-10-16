#creates the difference game boards displayed

user_board = [['.' for i in range(5)] for j in range(4)]
comp_board = [['.' for i in range(5)] for j in range(4)]
game_comp_board = [['.' for i in range(5)] for j in range(4)]


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print("\n-----")

print_board(user_board)
print()
print_board(comp_board)


def place_ships(board, num_ships):
    ship_count = 0
    while ship_count < num_ships:
        row = int(input("Please enter a row: "))
        col = int(input("Please enter a column: "))

        if row < 0 or row > 3 or col < 0 or col > 4:
            print("Invalid, try again!")
            continue
        elif board[row][col] == 'S':
            print("Ship already exists in that location.")
            continue

        board[row][col] = 'S'
        ship_count += 1
        print(f"Ship {ship_count} placed.")
    return board


import random

def place_comp_ships(board, num_ships):
    ship_count = 0
    while ship_count < num_ships:
        row = random.randint(0, 3)
        col = random.randint(0, 4)

        if board[row][col] == 'S':
            continue

        board[row][col] = 'S'
        ship_count += 1
    return board

comp_board = place_comp_ships(comp_board, 5)
print()
print_board(comp_board)












print("Let's play!")
print("User’s turn...")
user_board = place_ships(user_board, 5)

print_board(user_board)
print()
print_board(comp_board)


# Define function to check if game is over
def is_game_over(board):
    for row in board:
        if 'S' in row:
            return False
    return True

# Define function for user's turn
def user_turn(comp_board):
    print("User's turn...")
    row = int(input("Please enter a row: "))
    col = int(input("Please enter a column: "))

    while (0 > row) or (row > 3) or (col < 0) or (col > 4) or (user_board[row][col] == 'X') or (user_board[row][col] == 'O'):
        if (user_board[row][col] == 'X') or (user_board[row][col] == 'O'):
            print("You’ve already gone here, please try again.")
        else:
            print("Invalid, try again!")
        row = int(input("Please enter a row: "))
        col = int(input("Please enter a column: "))

    if comp_board[row][col] == 'S':
        print("Hit!")
        game_comp_board[row][col] = 'X'

        print("Computer's board:")
        print_board(game_comp_board)

    else:
        print("Miss!")
        game_comp_board[row][col] = 'O'

        print("Computer's board:")
        print_board(game_comp_board)

# Define function for computer's turn
def comp_turn(user_board):
    print("Computer's turn...")
    row = random.randint(0, 3)
    col = random.randint(0, 4)

    while (user_board[row][col] == 'X') or (user_board[row][col] == 'O'):
        row = random.randint(0, 3)
        col = random.randint(0, 4)

    if user_board[row][col] == 'S':
        print("Hit!")
        user_board[row][col] = 'X'

        print("User's board:")
        print_board(user_board)
    else:
        print("Miss!")
        user_board[row][col] = 'O'

        print("User's board:")
        print_board(user_board)

# Play game
turn_count = 0
while not is_game_over(user_board) and not is_game_over(comp_board):
    print(f"Turn {turn_count+1}:")
    user_turn(comp_board)
    if is_game_over(comp_board):
        print(f"User won in {turn_count}!")
        break
    comp_turn(user_board)
    if is_game_over(user_board):
        print(f"Computer won in{turn_count}")
        break
    turn_count += 1
