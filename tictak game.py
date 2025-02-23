# Simple Python Tic Tac Toe (No Extra Libraries)

# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check winner
def check_winner():
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Return 'X' or 'O'
    return None

# Function to check if the board is full
def is_draw():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"
    
    while True:
        display_board()
        
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
            else:
                print("Invalid move! Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1-9.")
            continue
        
        winner = check_winner()
        if winner:
            display_board()
            print(f"Player {winner} wins! 🎉")
            break

        if is_draw():
            display_board()
            print("It's a draw! 😐")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
