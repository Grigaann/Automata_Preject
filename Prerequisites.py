from Verification import *
from Modification import *

def display(automaton):
    alphabet = [chr(ord('a')+k) for k in range(len(automaton[0][2:]))]
    # Set header row
    print("   " + " "*17,end="|")
    for letter in alphabet:
        print("________"+str(letter),end="________|")
    print()

    for line in automaton:
        # Set header column
        if line[0]==0:
            print("   ",end="")
        elif line[0]==1:
            print("-->",end="")
        elif line[0] == 2:
            print("<--",end="")
        else:
            print("<->",end="")

        # Print the transition table
        for col in range(1,len(line)):
            if not line[col]:
                print(" "*17,end="|")
            else:
                print(" "*(17-(2*len(line[col])-1))+",".join([str(i) for i in line[col]]),end="|")
        print()
    return

def get_FA_from_file(fileName):
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')

    transitionTable=[[[] for i in range(int(linesOfFile[0])+2)] for _ in range(int(linesOfFile[1]))]

    for i in range(int(linesOfFile[1])):
        transitionTable[i][1]=str(i)
        transitionTable[i][0]=0
    # 0 = none, 1 = initial, 2 = final, 3 = both
    for initial in linesOfFile[2].split(" ")[1:]:
        transitionTable[int(initial)][0]+=1
    for initial in linesOfFile[3].split(" ")[1:]:
        transitionTable[int(initial)][0]+=2

    for transi in linesOfFile[5:len(linesOfFile)]:
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            
            if len(transiSplit)==2:
                transitionTable[int(transiSplit[0])][2+i].append(int(transiSplit[1]))
    return transitionTable


def get_index_from_letter(letter):
    return ord(letter)-ord('a')

def is_word_recognize_rec(transitionTable, word, state):
    if word=="": 
        if transitionTable[state][0] >=2 : return True
        return False
    index=2+get_index_from_letter(word[0])
    if index <= len(transitionTable[0])-1:
        if len(transitionTable[state][index])>0:
            return is_word_recognize_rec(transitionTable, word[1::], transitionTable[state][index][0])
        return False
    else:
        return False

def is_word_recognize(transitionTable, word):
    if not is_deterministic(transitionTable):
        transitionTable=determinization(transitionTable)


    entry=-1
    for i in range(0,len(transitionTable)):
        if transitionTable[i][0]%2==1:
            entry=i
    if entry==-1 :
        print("error no entry found") 
        return

    return is_word_recognize_rec(transitionTable, word, entry)


def complete(transitionTable):
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
