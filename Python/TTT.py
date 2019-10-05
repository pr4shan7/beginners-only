#from IPython.display import clear_output
row = [0,3,6]       #This list is a "row reference" list which provides the position number of the first column for each row
def intro_mark_choose():
    flag = 0
    temp1 =temp2 = None
    print('Welcome to the amazing game of Tic_Tac-Toe!!')
    print("Let's get started!")
    while temp1 == None:
        if flag==1:
            print('\n\n\n')
            print("Incorrect mark choosen. Please choose another appropriate mark!")
        print('Player 1, choose your mark: X or O ?')
        temp1=input()
        if temp1 == 'X':
            temp2 = 'O'
        elif temp1 == 'O':
            temp2 = 'X'
        else:
            temp1 = None
            flag=1
    print('\n\n\n')
    return temp1,temp2

def check_win(lst):
    if (lst[3]==lst[4]==lst[5] or lst[0]==lst[3]==lst[6]) and lst[3] != ' ':
        return True,lst[3]
    elif (lst[1]==lst[4]==lst[7] or lst[0]==lst[1]==lst[2]) and lst[1] != ' ':
        return True,lst[1]
    elif (lst[2]==lst[5]==lst[8] or lst[6]==lst[7]==lst[8]) and lst[8] != ' ':
        return True,lst[8]
    elif (lst[0]==lst[4]==lst[8] or lst[2]==lst[4]==lst[6]) and lst[4] != ' ':
        return True,lst[4]
    else:
        return False,None

def print_board(lst,mark=' ',row_index=0,col=0):
    go = 0
    if mark != ' ' and row_index in range (1,4) and col in range (1,4):
        if lst[row[row_index-1]+col-1] == ' ':
            lst[row[row_index-1]+col-1] = mark
            return 1
        else:
            return -1
    if (mark==' ' and row_index==0 and col == 0):
        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(lst[0],lst[1],lst[2]))
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(lst[3],lst[4],lst[5]))
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(lst[6],lst[7],lst[8]))
        print('     |     |     ')
        return 1
    else:
        return -2

while True:
    lst = [' ']*9           #This list keeps track of the players' marks on the board
    mark_1 = mark_2 = None # mark_1 and mark_2 are the marks of players 1 and 2 repectively
    moves = 0              # Keeps track of the number of moves
    win = False
    winning_mark = None
    while True:
        mark_1,mark_2 = intro_mark_choose()
        if mark_1 != None:
            print(f'Player 1 is using the mark: {mark_1} \nPlayer 2 is using the mark: {mark_2} \nLet\'s go! \n')
            break
    while True:
        foo = None
        while foo==None or foo==-1 or foo ==-2:
            print('\n\n\n')
            print_board(lst)
            if foo==-1:
                print('A move has already been played at this position. Choose another position')
            elif foo==-2:
                print('Invalid row or/and column numbers provided. Try appropriate valuse row/column = (1,2,3)')
            rowt,colt = input('Player 1,choose your position (row,column): ').split(',')
            foo = print_board(lst,mark_1,int(rowt),int(colt))
        moves += 1
        if moves >=5 and moves < 9:
            win,winning_mark = check_win(lst)
            if win:
                print('\n\n\n')
                print_board(lst) 
                if winning_mark == mark_1:
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
        elif moves == 9:
            print('\n\n\n')
            print_board(lst)
            print('Game tied!')
            break
        foo=None
        while foo==None or foo==-1 or foo==-2:
            print('\n\n\n')
            print_board(lst)
            if foo==-1:
                print('A move has already been played at this position. Choose another position')
            elif foo==-2:
                print('Invalid row or/and column numbers provided. Try appropriate valuse row/column = (1,2,3)')
            rowt,colt = input('Player 2,choose your position (row,column): ').split(',')
            foo = print_board(lst,mark_2,int(rowt),int(colt))
        moves +=1
        if moves >=5:
            win,winning_mark = check_win(lst)
            if win:
                print('\n\n\n')
                print_board(lst) 
                if winning_mark == mark_1:
                    print('Player 1 wins!')
                else:
                    print('Player 2 wins!')
                break
    con = 0
    while True:
        cont = input('Do you want to continue? (Y/N): ')
        if cont=='Y':
            con = 1
            break
        elif cont == 'N':
            break
        else:
            print('Invalid input. Try again!')
            continue
    if con==1:
        print('\n\n\n')
        continue
    else:
        print('Goodbye!')
        break