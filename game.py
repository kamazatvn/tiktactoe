BOARD = [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]

PLAYER_1 = "X"
PLAYER_2 = "O"

# Game functions
def drawing():
    row = int(input("Enter the row number: "))
    columns = int(input("Enter the column number: "))
    return (row - 1, columns - 1)


def main():
    # Game intro
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O")
    print("The board is as follows:")
    while True:
        count = 0
        for i in BOARD:
            for j in i:
                print(j, end=" ")
                count += 1
            if count == 3:
                print()
                count = 0
        print("Player 1 goes first")

        p1_turn = drawing()
        BOARD[p1_turn[0]][p1_turn[1]] = PLAYER_1
        for i in BOARD:
            for j in i:
                print(j, end=" ")
                count += 1
            if count == 3:
                print()
                count = 0
        if BOARD[0][0] == BOARD[0][1] == BOARD[0][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[0][1] == BOARD[0][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[1][0] == BOARD[1][1] == BOARD[1][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[1][0] == BOARD[1][1] == BOARD[1][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[2][0] == BOARD[2][1] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[2][0] == BOARD[2][1] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        # Win by columns
        if BOARD[0][0] == BOARD[1][0] == BOARD[2][0] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[1][0] == BOARD[2][0] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][1] == BOARD[1][1] == BOARD[2][1] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][1] == BOARD[1][1] == BOARD[2][1] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][2] == BOARD[1][2] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][2] == BOARD[1][2] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        # Win by diagonals
        if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == PLAYER_2:
            print("Player 2 wins!")
            break
        print("Player 2's turn")
        p2_turn = drawing()
        BOARD[p2_turn[0]][p2_turn[1]] = PLAYER_2
        for i in BOARD:
            for j in i:
                print(j, end=" ")
                count += 1
            if count == 3:
                print()
                count = 0
        # Win by rows
        if BOARD[0][0] == BOARD[0][1] == BOARD[0][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[0][1] == BOARD[0][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[1][0] == BOARD[1][1] == BOARD[1][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[1][0] == BOARD[1][1] == BOARD[1][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[2][0] == BOARD[2][1] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[2][0] == BOARD[2][1] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        # Win by columns
        if BOARD[0][0] == BOARD[1][0] == BOARD[2][0] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[1][0] == BOARD[2][0] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][1] == BOARD[1][1] == BOARD[2][1] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][1] == BOARD[1][1] == BOARD[2][1] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][2] == BOARD[1][2] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][2] == BOARD[1][2] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        # Win by diagonals
        if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == PLAYER_2:
            print("Player 2 wins!")
            break
        if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == PLAYER_1:
            print("Player 1 wins!")
            break
        elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == PLAYER_2:
            print("Player 2 wins!")
            break
        # Tie
        if (
            BOARD[0][0] != "o"
            and BOARD[0][1] != "o"
            and BOARD[0][2] != "o"
            and BOARD[1][0] != "o"
            and BOARD[1][1] != "o"
            and BOARD[1][2] != "o"
            and BOARD[2][0] != "o"
            and BOARD[2][1] != "o"
            and BOARD[2][2] != "o"
        ):
            print("It's a tie!")
            break


main()
