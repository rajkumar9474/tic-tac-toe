# Tic-Tac-Toe Game Documentation

## Overview

This Python script implements a simple command-line tic-tac-toe game for two players. Players take turns entering their moves, and the game continues until one player wins or there are no more moves left. The game board is displayed after each move.

## Functions

### `win_check(gm_mt)`

This function checks the tic-tac-toe game board to determine if any player has won. It examines rows, columns, and diagonals to find matching symbols ('o' or 'x').

- Returns a tuple `(1, 0)` if Player 1 ('o') wins.
- Returns a tuple `(1, 1)` if Player 2 ('x') wins.
- Returns a tuple `(0, 0)` if there is no winner yet.

### `print_mt(gm_mt)`

This function prints the current state of the tic-tac-toe game board. It uses a 3x3 grid and displays 'o' and 'x' for player moves.

## Usage

1. Initialize the tic-tac-toe game board and availability matrix:

    ```python
    gm_mt = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ava = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
    ```

2. Start the game loop:

    ```python
    game_on = 9  # Total number of moves in the game

    while game_on != 0:
        # Player 1's turn
        # ...

        # Player 2's turn
        # ...
    ```

3. Players take turns entering their moves. The game board is displayed after each move.

4. The game ends when one player wins or there are no more moves left.

## Example Gameplay

1. Player 1 enters position:
    ```
    player 1 enter position[1, 2, 3, 4, 5, 6, 7, 8, 9]: 1
    ```

2. The game board is updated and displayed.

3. Players continue taking turns until one player wins or the game ends.

## Notes

- If you see a warning about line endings during Git operations, ensure your Git configuration is set appropriately for your operating system.

- If switching branches, commit or stash your changes to avoid conflicts.

- Customize the game loop or functions as needed for your specific requirements.
