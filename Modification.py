from Verification import *
from UsefulFunction import get_index

def get_transitions(allTransition, transitionTable, listState, vuEmpty):
    """

    function that add to the corresponding transition of allTransition
    the states of all transitions of all states reached with an empty word transition

    """

    for i in range(len(transitionTable)):
        if i in listState:
            for y in range(2,len(transitionTable[i])-1):
                allTransition[y-2]+=transitionTable[i][y]

            for ind in transitionTable[i][-1]:
                if ind not in vuEmpty:
                    # if the state reached by an empty word transition was not handled before we add its transitions states by calling again get_transitions
                    vuEmpty.append(ind)
                    get_transitions(allTransition, transitionTable, [ind], vuEmpty)

def fill_table(newTransitionTable, transitionTable, names, listState):
    
    # will store all the states of the transitions of the new state
    allTransition=[[] for _ in range(len(transitionTable[0])-2)]

    vuEmpty=[]
    get_transitions(allTransition, transitionTable, listState, vuEmpty)

    for y in range(2,len(transitionTable[0])-1):
        allTransition[y-2]=list(set(allTransition[y-2]))
        allTransition[y-2].sort()
    
    listState=list(map(lambda x: transitionTable[x][1], listState))

    # listState is now equal to all the names of the states inside it before
    newLine=[]
    newLine.append(0)
    # the name will be a concatenation of all names in listState with _ or ' between them (_ if not empty transitions else ')
    name=get_name(listState, transitionTable)

    newLine.append(name)
    if name not in names : names.append(name)

    for transition in allTransition: 
        if len(transition)>0:
            # computing in the name manner the name of transitions and getting its index in names (index in names = index in newTransitionTable)
            tmp=list(map(lambda x: transitionTable[x][1], transition))
            nameTmp=get_name(tmp, transitionTable)
            # => 2_4
            if nameTmp not in names : names.append(nameTmp)
            # so we add the new index into the new transition of the new line
            newLine.append([names.index(nameTmp)])
        else:
            newLine.append([])


    newTransitionTable.append(newLine)

def determinization(transitionTable):
    if is_deterministic(transitionTable):
        return transitionTable
    newTransitionTable = []
    # list that store all the new names of the new states
    # the index of the names in names will correspond to the index of the line of this state in newTransitionTable
    names = []

    # put all old entries into the list oldInitialState
    oldInitialState = []
    for i in range(0, len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            oldInitialState.append(i)
    # calling fill table with all the initial states
    fill_table(newTransitionTable, transitionTable, names, oldInitialState)
    # setting the entry
    newTransitionTable[0][0] = 1
    
    # calling fill table for all names in names

    for name in names:
        if name not in [line[1] for line in newTransitionTable]:
            fill_table(newTransitionTable, transitionTable, names, list(map(lambda x: get_index(transitionTable,x), get_all_index_name(name))))
    
    # storing all final states in the list oldFinalState

    oldFinalState = []
    for i in range(0, len(transitionTable)):
        if transitionTable[i][0] >= 2:
            oldFinalState.append(transitionTable[i][1])

    # storing all states that thank's to empty word transition or thank's to normal transition can reach an exit
    
    oldFinalState_empty=[]
    # initializing the list with all the final states
    for i in oldFinalState:
        oldFinalState_empty.append(i)

    bool_=True
    # the loop stop when we didn't find an other state that could reach a final state
    while bool_:
        bool_=False
        for i in range(0, len(transitionTable)):
            if transitionTable[i][1] not in oldFinalState_empty:
                # if a state from oldFinalState is in the empty word transition of a state we add it to oldFinalState
                for state in oldFinalState_empty:
                    if get_index(transitionTable, state) in transitionTable[i][-1]:
                        bool_=True
                        oldFinalState_empty.append(transitionTable[i][1])

    # setting all the states that have an old final state in its name as a final state
    for i in range(len(newTransitionTable)):
        for newExit in oldFinalState_empty:
            if newExit in newTransitionTable[i][1] and newTransitionTable[i][0] < 2:
                newTransitionTable[i][0] += 2

    return newTransitionTable


def standardization(transitionTable):
    if is_standard(transitionTable):
        return transitionTable

    # Inserting new entry
    transitionTable.insert(0, [[] for _ in range(len(transitionTable[0]))])
    transitionTable[0][0] = 1
    transitionTable[0][1] = "i"

    # Removing older initial states while storing them
    oldInitialState = []
    for i in range(1, len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            oldInitialState.append(i)
            transitionTable[i][0] = transitionTable[i][0] - transitionTable[i][0] % 2

    # add all transitions of the old initial states to the new one
    for i in oldInitialState:
        for y in range(2, len(transitionTable[i])):
            transitionTable[0][y] += transitionTable[i][y]

    # Removing doubles
    for y in range(2, len(transitionTable[0])):
        transitionTable[0][y] = list(set(transitionTable[0][y]))

    # adding one to every transitions since we work with index and we just added one line at the begginning
    for i in range(len(transitionTable)):
        for y in range(2, len(transitionTable[i])):
            transitionTable[i][y] = list(map(lambda x: x+1, transitionTable[i][y]))

    return transitionTable

def completion(transitionTable):
    if not is_deterministic(transitionTable):
        transitionTable=determinization(transitionTable)
        
    if is_complete(transitionTable):
        return transitionTable

    # adding the transition to the sink where the state dont have a transition for a letter of the alphabet
    for i in range(len(transitionTable)):
        for transi in range(2, len(transitionTable[i])-1):
            if len(transitionTable[i][transi])==0:
                transitionTable[i][transi]=[len(transitionTable)]
    newLine=[0, "p"]
    # adding the transition from the sink to itself
    for _ in range(2, len(transitionTable[0])-1):
        newLine.append([len(transitionTable)])
    # adding the empty word transition
    newLine.append([])
    # adding the new line containing the sink
    transitionTable.append(newLine)
    return transitionTable

def complentary(transitionTable):
    """just inversing final states"""
    if not is_complete(transitionTable):
        transitionTable= completion(transitionTable)
    
    for i in range(len(transitionTable)):
        if transitionTable[i][0]>=2:transitionTable[i][0]-=2
        else:transitionTable[i][0]+=2

    return transitionTable

def _get_number_group(globalList, state):
    for i, group in enumerate(globalList):
        if state in group: 
            return i

def minimization(transitionTable):
    """
    To minimize an automaton we need:
        - it is complete
        - it is deterministic
        - to gateher non_final_state and final state and compare them respectively
    
    """
    if not is_deterministic(transitionTable):
        transitionTable = determinization(transitionTable)

    # initializing our to first groups
    finalState = []
    nonFinalState = []

    for i in range(0, len(transitionTable)):
        if transitionTable[i][0]<=1:
            nonFinalState.append(transitionTable[i][1])
        else:
            finalState.append(transitionTable[i][1])

    # liste containing the groups
    globalList= [finalState,nonFinalState]

    change=True
    while change:
        newGlobalList = []
        change=False
        # for each group we compare the transitions of the states to group them again
        for i, group in enumerate(globalList):
            temp_group=[]
            for state in group:
                if len(temp_group)==0:
                    temp_group.append([state])
                else:
                    is_added=False
                    for group in temp_group:
                        bool___=True
                        # if at least one of the transitions from one state of the group compared to the state state
                        # go to a different group we don't add the state to the group
                        for z in range(2,len(transitionTable[0])-1):
                            transi1=transitionTable[get_index(transitionTable,state)][z]
                            transi2=transitionTable[get_index(transitionTable,group[0])][z]
                            if len(transi1)==0 and len(transi2)!=0 or len(transi1)!=0 and len(transi2)==0:
                                bool___=False
                            elif len(transi1)!=0 and len(transi2)!=0:
                                if _get_number_group(globalList, transitionTable[transi1[0]][1])!=_get_number_group(globalList, transitionTable[transi2[0]][1]):
                                    bool___=False
                        if bool___:
                            group.append(state)
                            is_added=True
                    # if the state is not added to any group we create a new group with itself
                    if not is_added:
                        temp_group.append([state])
            for g in temp_group:
                newGlobalList.append(g)
        change= globalList!=newGlobalList
        globalList=newGlobalList

    newTransitionTable=[]
    
    # creating the new transition table
    for i, group in enumerate(globalList):
        name=str(i)
        if "p" in group: name="p"
        newLine=[0, name]
        # adding the transitions
        for z in range(2, len(transitionTable[0])):
            transi1=transitionTable[get_index(transitionTable,group[0])][z]
            if len(transi1)==0: newLine.append([])
            else:newLine.append([_get_number_group(globalList, transitionTable[transi1[0]][1])])
        
        # setting the type of the state
        type_=0
        for state in group:
            if transitionTable[get_index(transitionTable, state)][0]==3:type_=3
            elif transitionTable[get_index(transitionTable, state)][0]==1 and type_%2==0:type_+=1
            elif transitionTable[get_index(transitionTable, state)][0]==2 and type_==0 or type_==1:type_+=2
        newLine[0]=type_
        if type_%2==1: newLine[1]="i"

        newTransitionTable.append(newLine)

    return newTransitionTable