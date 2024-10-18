import random  

def print_board(board):  
    print("Current board:")  
    for row in board:  
        print(" | ".join(row))  
        print("-" * 9)  

def check_winner(board):  
    # Check rows and columns  
    for i in range(3):  
        if board[i][0] == board[i][1] == board[i][2] != " ":  
            return board[i][0]  
        if board[0][i] == board[1][i] == board[2][i] != " ":  
            return board[0][i]  

    # Check diagonals  
    if board[0][0] == board[1][1] == board[2][2] != " ":  
        return board[0][0]  
    if board[0][2] == board[1][1] == board[2][0] != " ":  
        return board[0][2]  

    return None  

def is_board_full(board):  
    return all(cell != " " for row in board for cell in row)  

def player_move(board, player):  
    while True:  
        try:  
            move = int(input(f"Player {player}, enter your move (1-9): "))  
            if move < 1 or move > 9:  
                raise ValueError("Invalid input! Please select a number between 1 and 9.")  
            row, col = divmod(move - 1, 3)  
            if board[row][col] != " ":  
                print("Invalid move! The cell is already taken. Try again.")  
            else:  
                board[row][col] = player  
                break  
        except ValueError as e:  
            print(e)  

def computer_move(board, player):  
    available_moves = [i for i in range(9) if board[i // 3][i % 3] == " "]  
    move = random.choice(available_moves)  
    board[move // 3][move % 3] = player  

def main():  
    print("Welcome to Tic Tac Toe!")  
    game_mode = input("Choose game mode: 1 for Single Player, 2 for Two Players: ")  

    if game_mode not in ['1', '2']:  
        print("Invalid choice! Exiting the game.")  
        return  

    board = [[" " for _ in range(3)] for _ in range(3)]  
    current_player = "X"  # Player X starts  

    while True:  
        print_board(board)  

        if game_mode == '1' and current_player == "O":  
            print("Computer's turn:")  
            computer_move(board, current_player)  
        else:  
            player_move(board, current_player)  

        winner = check_winner(board)  
        if winner:  
            print_board(board)  
            print(f"Player {winner} wins!")  
            break  
        
        if is_board_full(board):  
            print_board(board)  
            print("It's a tie!")  
            break  

        # Switch player  
        current_player = "O" if current_player == "X" else "X"  

if __name__ == "__main__":  
    main()