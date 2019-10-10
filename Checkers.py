"""
This is my project of checkers game.
I made it before lessons about classes or even functions so it's really  simple one.
You have to put the exact location of pawn and field
Example: put 32, then 41 and see what's happened
"""

board = []

# Making board 10 per 10
for i in range(10):
    board.append([0] * 10)

# Setup 1, W or B in the right location
for i in range(10):
    for j in range(0, 10, 2):

        if (i % 2 == 0):

            if (i <= 3):
                board[i][j - 1] = "W"

            elif (i >= 6):
                board[i][j - 1] = "B"

            else:
                board[i][j - 1] = 1

        else:

            if (i <= 3):
                board[i][j] = "W"

            elif (i >= 6):
                board[i][j] = "B"

            else:
                board[i][j] = 1

# Clear the top and bottom lines and number the margins
for i in range(len(board)):
    for j in range(i + 1):
        board[0][j] = ""
        board[9][j] = ""
        board[i - 1][0] = str(j - 1) + "|"
        board[i - 1][9] = "|" + str(j - 1)

board[0][0] = "---------------------"
board[9][0] = "---------------------"

for i in board:
    for j in i:
        print(j, end=" ")
    print()

print("Checkers\n")
which_player = 0
pawns_W = 12
pawns_B = 12

# Game start
while (True):
    try:

        if (pawns_W == 0):
            print("Wins B!")
            break

        if (pawns_B == 0):
            print("Wins W!")
            break

        print("W pawns left:", pawns_W)
        print("B pawns left:", pawns_B)

        if(which_player %2 == 0):
            print("Player 'W'")
            player_name = "W"
        else:
            print("Player 'B'")
            player_name = "B"


        pawn = input("Which pawn?: ")

        if (len(pawn) > 2):
            print("Only two digits")

        pawn0 = int(pawn[0])
        pawn1 = int(pawn[1])

        if (board[pawn0][pawn1] == player_name):
            pass

        else:
            print("Move only your pawns")
            continue

        field = input("Which field?: ")

        if (len(pawn) > 2):
            print("Only two digits")

        pawn0 = int(pawn[0])
        pawn1 = int(pawn[1])

        field0 = int(field[0])
        filed1 = int(field[1])

        target_Position = board[field0][filed1]

        if (target_Position is 1):

            # If the target place is 1 square away from the pawn
            if ((field0 == pawn0 + 1 or field0 == pawn0 - 1) and
                (filed1 == pawn1 + 1 or filed1 == pawn1 - 1)):

                # Make move and change player
                player_mark = board[pawn0].pop(pawn1)
                board[pawn0].insert(pawn1, 1)
                board[field0][filed1] = player_mark
                which_player += 1

            # Hit south east
            elif (((board[pawn0 + 1][pawn1 + 1] == "W" and player_name == "B") or
                   (board[pawn0 + 1][pawn1 + 1] == "B" and player_name == "W")) and field0 > pawn0):

                player_mark = board[pawn0].pop(pawn1)
                board[pawn0].insert(pawn1, 1)
                board[field0][filed1] = player_mark
                board[pawn0 + 1][pawn1 + 1] = 1
                which_player += 1

                if (player_name == "W"):
                    pawns_B -= 1

                if (player_name == "B"):
                    pawns_W -= 1

            # Hit north east
            elif (((board[pawn0 - 1][pawn1 + 1] == "W" and player_name == "B") or
                   (board[pawn0 - 1][pawn1 + 1] == "B" and player_name == "W")) and field0 < pawn0):

                player_mark = board[pawn0].pop(pawn1)
                board[pawn0].insert(pawn1, 1)
                board[field0][filed1] = player_mark
                board[pawn0 - 1][pawn1 + 1] = 1
                which_player += 1

                if (player_name == "W"):
                    pawns_B -= 1

                if (player_name == "B"):
                    pawns_W -= 1

            # Hit south west
            elif (((board[pawn0 + 1][pawn1 - 1] == "W" and player_name == "B") or
                   (board[pawn0 + 1][pawn1 - 1] == "B" and player_name == "W")) and field0 > pawn0):

                player_mark = board[pawn0].pop(pawn1)
                board[pawn0].insert(pawn1, 1)
                board[field0][filed1] = player_mark
                board[pawn0 + 1][pawn1 - 1] = 1
                which_player += 1

                if (player_name == "W"):
                    pawns_B -= 1

                if (player_name == "B"):
                    pawns_W -= 1

            # Hit north west
            elif (((board[pawn0 - 1][pawn1 - 1] == "W" and player_name == "B") or
                   (board[pawn0 - 1][pawn1 - 1] == "B" and player_name == "W")) and field0 < pawn0):

                player_mark = board[pawn0].pop(pawn1)
                board[pawn0].insert(pawn1, 1)
                board[field0][filed1] = player_mark
                board[pawn0 - 1][pawn1 - 1] = 1
                which_player += 1

                if (player_name == "W"):
                    pawns_B -= 1

                if (player_name == "B"):
                    pawns_W -= 1

            else:
                print("Your pawn doesn't reach that far")

        else:
            print("Move only on '1'")

        # Display the board
        for i in board:
            for j in i:
                print(j, end=" ")
            print()
    except (ValueError):
        print("Enter numbers only")

    except (IndexError):
        print("Enter only two digits")
