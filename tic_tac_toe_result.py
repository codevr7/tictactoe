def check_win(l1,l2,l3,val):
    loc_1 = locations([l1],val)
    loc_2 = locations([l2],val)
    loc_3 = locations([l3],val)
    indices = locations([l1,l2,l3], val)

    # Checks if value has won horizontally
    if HOM_list(l1, val) or HOM_list(l2, val) or HOM_list(l3, val):
        return True
    
    # Checking if value has won vertically
    vert_1,vert_2,vert_3 = 0,0,0
    for i in indices:
        if i % 3 == 0:
            vert_1 += 1
        if i % 3 == 1:
            vert_2 += 1
        if i % 3 == 2:
            vert_3 += 1
    if vert_1 == 3 or vert_2 == 3 or vert_3 == 3:
        return True
    
    # Checking if value has won diagonally
    if 1 in indices and 5 in indices and 9 in indices:
        return True
    if 3 in indices and 5 in indices and 7 in indices:
        return True
    return False

def locations(List,val):
    index = []
    list_no = -3
    for i in range(0,len(List)):
        list_no += 3
        for j in range(0,len(List[i])):
            if List[i][j] == val:
                index.append(j + list_no + 1)
    return index 

def HOM_list(List, val):
    for i in List:
        if i != val:
            return False
    return True

#print(locations([[' . ',' O ',' X '],[' . ',' X ',' . '],[' . ',' . ',' . ']],' . '))
#print(check_win([' X ',' O ',' X '],[' X ',' O ',' O '],[' X ',' O ', ' X '],' X '))
