from Verification import *

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

    return transitionTable


def determinization(transitionTable):
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
            fill_table(newTransitionTable, transitionTable, names, list(map(int, name.split("_"))))

    oldExit = []
    for i in range(0, len(transitionTable)):
        if transitionTable[i][0] >= 2:
            oldExit.append(str(i))

    for i in range(len(newTransitionTable)):
        for newExit in oldExit:
            if newExit in newTransitionTable[i][1] and newTransitionTable[i][0] < 2:
                newTransitionTable[i][0] += 2

    return newTransitionTable

def completion(transitionTable):
    if not is_deterministic(transitionTable):
        transitionTable=determinization(transitionTable)

    for i in range(len(transitionTable)):
        for transi in range(2, len(transitionTable[i])):
            if len(transitionTable[i][transi])==0:
                transitionTable[i][transi]=[len(transitionTable)]
    newLine=[-1, "p"]
    for _ in range(2, len(transitionTable[0])):
        newLine.append([len(transitionTable)])
    transitionTable.append(newLine)
    return transitionTable