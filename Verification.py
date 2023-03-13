def is_standard(transitionTable):
    entry = None
    for i in range(len(transitionTable)):
        if transitionTable[i][0]%2 == 1:
            if entry != None :
                return False
            entry=i
    if entry is None:
        return False

    for line in transitionTable:
        for transition in line[2:len(line)]:
            if i in transition:
                return False

    return True


def is_deterministic(transitionTable):
    entry = None
    for i in range(len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            if entry != None:return False
            entry = i
    if entry is None: return False

    for line in transitionTable:
        for transition in line[2:len(line)]:
            if len(transition) > 1: return False

    return True