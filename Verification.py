from UsefulFunction import *

def is_standard(transitionTable):

    # first check if it as 1 entry or more and get the index of this entry if it has one
    entry = None
    for i in range(len(transitionTable)):
        if transitionTable[i][0]%2 == 1:
            if entry != None :
                return False
            entry=i
            
    if entry is None:
        return False

    # check if there is no transition arriving at the entry
    for line in transitionTable:
        for transition in line[2:len(line)+1]:
            if entry in transition:
                return False

    return True


def is_deterministic(transitionTable):

    # first check if it as 1 entry or more and get the index of this entry if it has one
    entry = None
    for i in range(len(transitionTable)):
        if transitionTable[i][0] % 2 == 1:
            if entry != None:
                return False
            entry = i

    if entry is None:
        return False


    # then check if there is only one transition maximum for each letter of the alphabet on each state
    for line in transitionTable:
        for transition in line[2:len(line)-1]:
            if len(transition) > 1:
                return False
        # if the automaton has an empty word transition then its not deterministic
        if len(line[-1])>0 : return False

    return True

def is_word_recognized_rec(transitionTable, word, state):
    """this recursive function return False if the first letter of the word word is not recognized by the state
    else it returns True if the word is empty and the state is final
    else returns is_word_recognized_rec(transitionTable, word[1:], transitionState ) for the state corresponding to the transition of the letter word[0]
    """
    if word=="":
        if transitionTable[state][0] >=2 :
            return True
        return False

    bool=False

    index=2+get_index_from_letter(word[0])
    if index <= len(transitionTable[0])-1:

        if len(transitionTable[state][index])>0:
            bool= bool or is_word_recognized_rec(transitionTable, word[1::], transitionTable[state][index][0])
    for ind in range(len(transitionTable[state][-1])):
        bool = bool or is_word_recognized_rec(transitionTable, word, transitionTable[state][-1][ind])
    return bool

def is_word_recognized(transitionTable, word):
    # if its not deterministic we determinize it so that its easier to recognize the word
    if not is_deterministic(transitionTable):
        from Modification import determinization
        transitionTable=determinization(transitionTable)

    # get the entry of the automaton
    entry=-1
    for i in range(0,len(transitionTable)):
        if transitionTable[i][0]%2==1:
            entry=i
    
    if entry==-1 :
        print("error no entry found")
        return
    
    return is_word_recognized_rec(transitionTable, word, entry)

def is_complete(transitionTable):
    # check if each state has at least one transition for each letter of the alphabet except the empty word
    for i in range(len(transitionTable)):
        for y in range(2, len(transitionTable[0])-1):
            if len(transitionTable[i][y])==0:return False
    return True