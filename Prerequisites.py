from Modification import *

def display(automaton,writeInText,fileName=""):
    alphabet = [chr(ord('a')+k) for k in range(len(automaton[0][2:]))]
    if writeInText:alphabet[-1]="e"
    else:alphabet[-1]="€"
    # Set header row
    if writeInText:print_(fileName,writeInText,"   " + " "*17,end="|")
    else:print("   " + " "*17,end="|")
    for letter in alphabet:
        if writeInText:print_(fileName,writeInText,"________"+str(letter),end="________|")
        else:print("________"+str(letter),end="________|")
    if writeInText:print_(fileName,writeInText,"")
    else:print()
    for line in automaton:
        # Set header column
        if line[0]==0:
            if writeInText:print_(fileName,writeInText,"   ",end="")
            else:print("   ",end="")
        elif line[0]==1:
            if writeInText:print_(fileName,writeInText,"-->",end="")
            else:print("-->",end="")
        elif line[0] == 2:
            if writeInText:print_(fileName,writeInText,"<--",end="")
            else:print("<--",end="")
        else:
            if writeInText:print_(fileName,writeInText,"<->",end="")
            else:print("<->",end="")

        # Print the state concerned
        if writeInText:print_(fileName,writeInText," "*(17-len(line[1]))+line[1],end="|")
        else:print(" "*(17-len(line[1]))+line[1],end="|")
        # Print the transitions of the state
        for col in range(2,len(line)):
            if not line[col]:
                if writeInText:print_(fileName,writeInText," "*17,end="|")
                else:print(" "*17,end="|")
            else:
                names=",".join([automaton[i][1] for i in line[col]])
                if writeInText:print_(fileName,writeInText," "*(17-len(names))+names,end="|")
                else:print(" "*(17-len(names))+names,end="|")
        if writeInText:print_(fileName,writeInText,"")
        else:print()
    return

def get_index(transitionTable, state):
    for i in range(len(transitionTable)):
        if transitionTable[i][1]==state:
            return i

def get_FA_from_file(fileName):
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')
    transitionTable=[]

    states=[]

    for state in linesOfFile[2].split(" ")[1:]:
        if state not in states: states.append(state)
    for state in linesOfFile[3].split(" ")[1:]:
        if state not in states: states.append(state)

    for transi in linesOfFile[4:len(linesOfFile)]:
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            if len(transiSplit)==2:
                for state in transiSplit:
                    if state not in states:
                        states.append(state)
        transiSplit=transi.split(" ")
        if len(transiSplit)==2:
            for state in transiSplit:
                if state not in states:
                    states.append(state)

    # FIX THE SORT
    states.sort()

    for state in states:
        transitionTable.append([0, state]+[[] for _ in range(int(linesOfFile[0])+1)])


    #0 = none, 1 = initial, 2 = final, 3 = both
    for initial in linesOfFile[2].split(" ")[1:]:
        transitionTable[get_index(transitionTable, initial)][0]+=1
    for initial in linesOfFile[3].split(" ")[1:]:
        transitionTable[get_index(transitionTable, initial)][0]+=2

    for transi in linesOfFile[4:len(linesOfFile)]:
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            
            if len(transiSplit)==2:
                transitionTable[get_index(transitionTable, transiSplit[0])][2+i].append(get_index(transitionTable, transiSplit[1]))
        transiSplit=transi.split(" ")
        if len(transiSplit)==2:
            transitionTable[get_index(transitionTable, transiSplit[0])][2+i+1].append(get_index(transitionTable, transiSplit[1]))

    return transitionTable

    
def print_(file, writeInText, msg, end="\n"):
    if writeInText:
        with open("Execution_traces/"+file, "a") as f:
            f.write(msg+end)

def get_index_from_letter(letter):
    return ord(letter)-ord('a')