import tic_tac_toe_result as result
import tic_tac_toe_minimax as move 

def Game():
    print("You cannot beat me :)")
    win = False
    turn = 0
    options = [1,2,3,4,5,6,7,8,9]
    l1 = [' . ',' . ',' . ']
    l2 = [' . ',' . ',' . ']
    l3 = [' . ',' . ',' . ']
    while len(options) > 0:
        print("\n")
        print(print_line(l1))
        print(print_line(l2))
        print(print_line(l3))
        if turn == 0:
            next_move = int(input("Type in your next move: "))
        else:
            next_move = move.optimal(l1,l2,l3)
            #next_move = options[0]
        if next_move not in options:
            print("Place is already occupied")
            continue
        options.remove(next_move)
        insert_func(l1,l2,l3,next_move,turn)
        if turn == 0: turn = 1
        else: turn = 0
        if result.check_win(l1,l2,l3,' X '):
            win = ' X '
            break
        if result.check_win(l1,l2,l3,' O '):
            win = ' O '
            break
    print("\n")
    print(print_line(l1))
    print(print_line(l2))
    print(print_line(l3))
    if win == ' X ':
        return " You won "
    if win == ' O ':
        return " Computer won"
    return str ("Its a draw!!!")

# Places X-or-O in a given index in the tic-tac-toe grid
def insert_func(l1,l2,l3,index,turn):
    if turn == 1:
        next_play = " O "
    else:
        next_play = " X "
    if index < 4:
        replace(l1,index - 1,next_play)
    elif index < 7:
        replace(l2,index - 4 ,next_play)
    else:
        replace(l3,index - 7,next_play)
    return l1,l2,l3

# Converts a list into a string
def print_line(List):
    string = ""
    for ele in List:
        string += ele
    return string

# Replaces a given element from a given index in a list 
def replace(List,index,ele):
    del List[index]
    List.insert(index,ele)
    return List

print(Game())
