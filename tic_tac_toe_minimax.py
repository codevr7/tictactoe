import tic_tac_toe_result as result

def optimal(l1,l2,l3):
    res = []
    indices = result.locations([l1,l2,l3],' . ')
    for i in indices:
        if i < 4:
            curr = l1.copy()
            replace(curr,i-1,' O ')
            res.append([minimax(curr,l2,l3,' X ',' O '),i])
        elif i < 7:
            curr = l2.copy()
            replace(curr,i-4,' O ')
            res.append([minimax(l1,curr,l3,' X ',' O '),i])
        else:
            curr = l3.copy()
            replace(curr,i-7,' O ')
            res.append([minimax(l1,l2,curr,' X ',' O '),i])
    game = [-1,0]
    for i in res:
        if i[0] == 1:
            game = i
        if game[0] != 1:
            if i[0] == 0:
                game = i
    return game[1]

def minimax(l1,l2,l3,val,opp):
    mov = []
    res = []
    indices = result.locations([l1,l2,l3],' . ')
    if result.check_win(l1,l2,l3,opp):
        return 1
    if next_win(l1,l2,l3,val):
        if val == ' O ':
            return 1
        else:
            return -1
    if len(indices) == 0:
        return 0
    for i in indices:
        if i < 4:
            curr_1 = l1.copy()
            replace(curr_1,i-1,val)
            res.append(minimax(curr_1,l2,l3,opp,val))
        elif i < 7:
            curr_2 = l2.copy()
            replace(curr_2,i-4,val)
            res.append(minimax(l1,curr_2,l3,opp,val))
        else:
            curr_3 = l3.copy()
            replace(curr_3,i-7,val)
            res.append(minimax(l1,l2,curr_3,opp,val))
    if val == ' O ':
        return max(res)
    if val == ' X ':
        return min(res)

def next_win(l1,l2,l3,val):
    indices = result.locations([l1,l2,l3],' . ')
    for i in indices:
        if i < 4:
            swp = l1.copy()
            replace(swp,i-1,val)
            if result.check_win(swp,l2,l3,val):
                return i
        elif i < 7:
            swp = l2.copy()
            replace(swp,i - 4,val)
            if result.check_win(l1,swp,l3,val):
                return i
        else:
            swp = l3.copy()
            replace(swp,i - 7,val)
            if result.check_win(l1,l2,swp,val):
                return i
    return False

def replace(List,index,ele):
    del List[index]
    List.insert(index,ele)
    return List


#print(optimal([' . ',' X ',' X '],[' X ',' X ',' O '],[' O ',' . ',' O ']))
#print(minimax([' . ',' X ',' X '],[' X ',' X ',' O '],[' O ',' . ',' O '],' X ',' O '))
