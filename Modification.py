from Verification import *

def get_index(transitionTable, x):
    for i in range(len(transitionTable)):
        if transitionTable[i][1]==x : return i

def get_transitions(allTransition, transitionTable, listState, vuEmpty):
    for i in range(len(transitionTable)):
        if i in listState:
            for y in range(2,len(transitionTable[i])-1):
                allTransition[y-2]+=transitionTable[i][y]
                if len(transitionTable[i][y])>0:
                    #vuEmpty+=transitionTable[i][y]
                    get_transitions(allTransition, transitionTable, transitionTable[i][y], vuEmpty)

            for ind in transitionTable[i][-1]:
                if ind not in vuEmpty:
                    vuEmpty.append(ind)
                    get_transitions(allTransition, transitionTable, [ind], vuEmpty)

def get_name(listState, transitionTable):
    for name in listState:
        if len(transitionTable[get_index(transitionTable, name)][-1])>0:
            return "'".join(listState)+"'"
    return "_".join(listState)

def get_index_name(name):
    if "_" in name: 
        return name.split("_")
    lst=name.split("'")
    newLst=[]
    for i in lst: 
        if i != "": newLst.append(i)
    return newLst

def fill_table(newTransitionTable, transitionTable, names, listState):
    newLine=[]
    allTransition=[[] for _ in range(len(transitionTable[0])-2)]
    vuEmpty=[]
    get_transitions(allTransition, transitionTable, listState, vuEmpty)

    for y in range(2,len(transitionTable[0])-1):
        allTransition[y-2]=list(set(allTransition[y-2]))
        allTransition[y-2].sort()

    listState=list(map(lambda x: transitionTable[x][1], listState))
    newLine.append(0)
    name=get_name(listState, transitionTable)
    newLine.append(name)
    if name not in names : names.append(name)
    for transition in allTransition: 
        if len(transition)>0:
            tmp=list(map(lambda x: transitionTable[x][1], transition))
            nameTmp=get_name(tmp, transitionTable)
            if nameTmp not in names : names.append(nameTmp)
            newLine.append([names.index(nameTmp)])
        else:
            newLine.append([])


    newTransitionTable.append(newLine)

def standardization(transitionTable):
    if is_standard(transitionTable):
        return transitionTable

# /!\ REMOVED THE +1 ON ALL STATES OF THE TABLE

    # Inserting new entry
    transitionTable.insert(0, [[] for _ in range(len(transitionTable[0]))])
    transitionTable[0][0] = 1
    transitionTable[0][1] = "i"

    # Removing older entries while storing them
    oldEntry = []
    for i in range(1, len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            oldEntry.append(i)
            transitionTable[i][0] = transitionTable[i][0] - transitionTable[i][0] % 2

    for i in oldEntry:
        for y in range(2, len(transitionTable[i])):
            transitionTable[0][y] += transitionTable[i][y]

    # Removing doubles
    for y in range(2, len(transitionTable[0])):
        transitionTable[0][y] = list(set(transitionTable[0][y]))

    for i in range(len(transitionTable)):
        for y in range(2, len(transitionTable[i])):
            transitionTable[i][y] = list(map(lambda x: x+1, transitionTable[i][y]))


    return transitionTable


def determinization(transitionTable):
    if is_deterministic(transitionTable):
        return transitionTable
    newTransitionTable = []
    names = []

    # Dico format :
    # key : state1_state2_stat3_... ascendant order
    # value : index in the new table

    oldEntry = []
    for i in range(0, len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            oldEntry.append(i)
    fill_table(newTransitionTable, transitionTable, names, oldEntry)
    newTransitionTable[0][0] = 1
    
    for name in names:
        if name not in [line[1] for line in newTransitionTable]:
            fill_table(newTransitionTable, transitionTable, names, list(map(lambda x: get_index(transitionTable,x), get_index_name(name))))
    
    oldExit = []
    oldExit_empty=[]
    for i in range(0, len(transitionTable)):
        if transitionTable[i][0] >= 2:
            oldExit.append(transitionTable[i][1])
    for i in oldExit:
        oldExit_empty.append(i)
    bool_=True
    while bool_:
        bool_=False
        for i in range(0, len(transitionTable)):
            if transitionTable[i][1] not in oldExit_empty:
                for state in oldExit_empty:
                    if get_index(transitionTable, state) in transitionTable[i][-1]:
                        bool_=True
                        oldExit_empty.append(transitionTable[i][1])

    for i in range(len(newTransitionTable)):
        for newExit in oldExit_empty:
            if newExit in newTransitionTable[i][1] and newTransitionTable[i][0] < 2:
                newTransitionTable[i][0] += 2

    return newTransitionTable

def completion(transitionTable):
    if is_complete(transitionTable):
        return transitionTable
    bool_=False
    for i in range(len(transitionTable)):
        if len(transitionTable[-1])>0:
            bool_=True
    if bool_ and not is_deterministic(transitionTable):
        transitionTable=determinization(transitionTable)

    for i in range(len(transitionTable)):
        for transi in range(2, len(transitionTable[i])-1):
            if len(transitionTable[i][transi])==0:
                transitionTable[i][transi]=[len(transitionTable)]
    newLine=[0, "p"]
    for _ in range(2, len(transitionTable[0])-1):
        newLine.append([len(transitionTable)])
    newLine.append([])
    transitionTable.append(newLine)
    return transitionTable

def complentary(transitionTable):
    if not is_complete(transitionTable):
        transitionTable= completion(transitionTable)
    
    for i in range(len(transitionTable)):
        if transitionTable[i][0]>=2:transitionTable[i][0]-=2
        else:transitionTable[i][0]+=2

    return transitionTable
