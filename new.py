def win_check(gm_mt):
    # Check if any player has won by examining rows, columns, and diagonals
    if (gm_mt[0] == gm_mt[1] and gm_mt[1] == gm_mt[2]):
        if (gm_mt[0] == "o"):
            return 1, 0  # Player 1 (o) won
        else:
            return 1, 1  # Player 2 (x) won
    elif (gm_mt[3] == gm_mt[4] and gm_mt[4] == gm_mt[5]):
        if (gm_mt[3] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[6] == gm_mt[7] and gm_mt[7] == gm_mt[8]):
        if (gm_mt[6] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[0] == gm_mt[3] and gm_mt[3] == gm_mt[6]):
        if (gm_mt[0] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[1] == gm_mt[4] and gm_mt[4] == gm_mt[7]):
        if (gm_mt[1] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[2] == gm_mt[5] and gm_mt[5] == gm_mt[8]):
        if (gm_mt[2] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[0] == gm_mt[4] and gm_mt[4] == gm_mt[8]):
        if (gm_mt[0] == "o"):
            return 1, 0
        else:
            return 1, 1
    elif (gm_mt[2] == gm_mt[4] and gm_mt[4] == gm_mt[6]):
        if (gm_mt[2] == "o"):
            return 1, 0
        else:
            return 1, 1
    else:
        return 0, 0  # No winner yet

def print_mt(gm_mt):
    # Print the tic-tac-toe board
    print("-------------")
    print("|", end=" ")
    for i in range(len(gm_mt)):
        if (gm_mt[i] != "o") and (gm_mt[i] != "x"):
            print(" ", end=" | ")
        else:
            print(gm_mt[i], end=" | ")
        if (i + 1) % 3 == 0:
            print("\n-------------\n|", end=" ")

gm_mt = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Initial tic-tac-toe board
ava = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]  # Availability matrix for user inputs

game_on = 9  # Total number of moves in the game

while (game_on != 0):
    # Player 1's turn
    ava1 = [i + 1 for i in range(len(ava)) if ava[i] == "0"]  # Available positions for player 1
    p1_inp = int(input("player 1 enter position{}: ".format(ava1)))  # Player 1 (o) input
    while (p1_inp not in ava1):
        print("wrong input!! enter again: ")
        p1_inp = int(input("player 1 enter position{}: ".format(ava1)))
    ava[p1_inp - 1] = "1"  # Mark the position as filled
    gm_mt[p1_inp - 1] = "o"  # Update the tic-tac-toe board
    game_on -= 1  # Decrement the total moves

    print_mt(gm_mt)  # Display the current state of the board

    x, y = win_check(gm_mt)  # Check if someone has won

    if x == 1:
        if (y == 0):
            print("player 1 won!!")
        else:
            print("player 2 won!!")
        break  # Exit the loop if there's a winner

    if (game_on == 0):
        print("no one wins the game")
        break  # Exit the loop if there's no winner and no moves left

    # Player 2's turn
    ava1 = [i + 1 for i in range(len(ava)) if ava[i] == "0"]  # Available positions for player 2
    p2_inp = int(input("player 2 enter position{}: ".format(ava1)))  # Player 2 (x) input
    while (p2_inp not in ava1):
        print("wrong input!! enter again: ")
        p2_inp = int(input("player 2 enter position{}: ".format(ava1)))
    ava[p2_inp - 1] = "1"  # Mark the position as filled
    gm_mt[p2_inp - 1] = "x"  # Update the tic-tac-toe board
    game_on -= 1  # Decrement the total moves

    print_mt(gm_mt)  # Display the current state of the board

    x, y = win_check(gm_mt)  # Check if someone has won

    if x == 1:
        if (y == 0):
            print("player 1 won!!")
        else:
            print("player 2 won!!")
        break  # Exit the loop if there's a winner
