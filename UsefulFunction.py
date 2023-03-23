def get_index_from_letter(letter):
    """Return the index of a letter in the alphabet of the automaton"""
    return ord(letter)-ord('a')

def get_index(transitionTable, name):
    """get the index of the state of name name"""
    for i in range(len(transitionTable)):
        if transitionTable[i][1]==name:
            return i
        
def get_all_index_name(name):
    """get all the index (in the basic transition table) of the state of name name"""
    if "_" in name: 
        return name.split("_")
    lst=name.split("'")
    newLst=[]
    for i in lst: 
        if i != "": newLst.append(i)
    return newLst

def get_name(listState, transitionTable):
    """get the new name of the state when determinizing"""
    for name in listState:
        if len(transitionTable[get_index(transitionTable, name)][-1])>0:
            return "'".join(listState)+"'"
    return "_".join(listState)