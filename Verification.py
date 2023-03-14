def get_index_from_letter(letter):
    return ord(letter)-ord('a')

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
            if entry != None:
                return False
            entry = i
    if entry is None:
        return False

    for line in transitionTable:
        for transition in line[2:len(line)-1]:
            if len(transition) > 1:
                return False

    return True

def is_word_recognized_rec(transitionTable, word, state):
    if word=="":
        if transitionTable[state][0] >=2 :
            return True
        return False

    bool=False

    index=2+get_index_from_letter(word[0])
    if index <= len(transitionTable[0])-1:
        # and transitionTable[state][index]!= state
        if len(transitionTable[state][index])>0:
            bool= bool or is_word_recognized_rec(transitionTable, word[1::], transitionTable[state][index][0])
    for ind in range(len(transitionTable[state][-1])):
        bool = bool or is_word_recognized_rec(transitionTable, word, transitionTable[state][-1][ind])
    return bool

def is_word_recognized(transitionTable, word):
    if not is_deterministic(transitionTable):
        from Modification import determinization
        transitionTable=determinization(transitionTable)
    entry=-1
    for i in range(0,len(transitionTable)):
        if transitionTable[i][0]%2==1:
            entry=i
    if entry==-1 :
        print("error no entry found")
        return
    return is_word_recognized_rec(transitionTable, word, entry)