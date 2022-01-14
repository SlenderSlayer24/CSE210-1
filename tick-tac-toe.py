# Name: Tick-tac-toe
# Author, Tyler Sparks
def main():
    win = 0
    full = False
    rows = [1,2,3,4,5,6,7,8,9]
    player = "o"
    count = 0
    while win == 0:
        table(rows)
        rows = anwser(player,rows)
        player = playerswitch(player)
        win = checkrow(rows,win)
        count = count + 1
        if count == 9:
            win = "d"
    else:
        if win == "o":
            table(rows)
            print()
            print("*** os win!! ***")
        elif win == "x":
            table(rows)
            print()
            print("*** xs win!! ***")
        elif win == "d":
            table(rows)
            print("*** It is a draw ***")


def anwser(player,rows):
    #process the anwser and check if it's a valid space before adding an o or x
    valid = False
    anwser = input(f"It is {player}'s turn, plase pick the number of an open space: ")
    while valid == False:
        if anwser == "1" or anwser == "2" or anwser == "3" or anwser == "4" or anwser == "5" or anwser == "6" or anwser == "7" or anwser == "8" or anwser == "9":
            anwser = int(anwser) - 1
            if rows[anwser] == "x" or rows[anwser] == "o":
                print ("that space has been selected")
                table(rows)
                anwser = input(f"please input the number of an open space.: ")
            else:
                rows[anwser] = player
                valid = True
        else:
            print("please use a valid space by inputing the corrisponding number")
            table(rows)
            anwser = input(f"please input the number of an open space.:")
    return rows

def table(rows):
    #print out the current board and each x or o
    row1 = f"{rows[0]} | {rows[1]} | {rows[2]}"
    print(row1)
    print("----------")
    row2 = f"{rows[3]} | {rows[4]} | {rows[5]}"
    print(row2)
    print("----------")
    row3 = f"{rows[6]} | {rows[7]} | {rows[8]}"
    print(row3)

def checkrow(rows,winrow):
    #check each row
    ocount = 0
    xcount = 0
    row1 = [rows[0], rows[1], rows[2]]
    row2 = [rows[3], rows[4], rows[5]]
    row3 = [rows[6], rows[7], rows[8]]
    column1 = [rows[0], rows[3], rows[6]]
    column2 = [rows[1], rows[4], rows[7]]
    column3 = [rows[2], rows[5], rows[8]]
    diag1 = [rows[0], rows[4], rows[8]]
    diag2 = [rows[6], rows[4], rows[2]]
    #top row
    for x in row1:
        if x == "o":
            ocount += 1
        elif x == "x":
            xcount += 1
    if ocount == 3:
        winrow = "o"
    elif xcount == 3:
        winrow = "x"
    if winrow == 0:
    #middle row
        ocount=0
        xcount=0
        for x in row2:
            if x == "o":
                ocount += 1
            elif x == "x":
                xcount += 1
        if ocount == 3:
            winrow = "o"
        elif xcount == 3:
            winrow = "x"
    #bottom row
        if winrow == 0:
            ocount=0
            xcount=0
            for x in row3:
                if x == "o":
                    ocount += 1
                elif x == "x":
                    xcount += 1
            if ocount == 3:
                winrow = "o"
            elif xcount == 3:
                winrow = "x"
    #left colum
            if winrow == 0:
                ocount=0
                xcount=0
                for x in column1:
                    if x == "o":
                        ocount += 1
                    elif x == "x":
                        xcount += 1
                if ocount == 3:
                    winrow = "o"
                elif xcount == 3:
                    winrow = "x"
    #middle colum
                if winrow == 0:
                    ocount=0
                    xcount=0
                    for x in column2:
                        if x == "o":
                            ocount += 1
                        elif x == "x":
                            xcount += 1
                    if ocount == 3:
                        winrow = "o"
                    elif xcount == 3:
                        winrow = "x"
    #right colum
                    if winrow == 0:
                        ocount=0
                        xcount=0
                        for x in column3:
                            if x == "o":
                                ocount += 1
                            elif x == "x":
                                xcount += 1
                        if ocount == 3:
                            winrow = "o"
                        elif xcount == 3:
                            winrow = "x"
    #top left diagnal
                        if winrow == 0:
                            ocount=0
                            xcount=0
                            for x in diag1:
                                if x == "o":
                                    ocount += 1
                                elif x == "x":
                                    xcount += 1
                            if ocount == 3:
                                winrow = "o"
                            elif xcount == 3:
                                winrow = "x"
    #top right diagnal
                            if winrow == 0:
                                ocount=0
                                xcount=0
                                for x in diag2:
                                    if x == "o":
                                        ocount += 1
                                    elif x == "x":
                                        xcount += 1
                                if ocount == 3:
                                    winrow = "o"
                                elif xcount == 3:
                                    winrow = "x"
    return winrow

def playerswitch(player):
    #switch the players
    if player == "o":
        player = "x"
    else:
        player = "o"
    return player

main()