from Modification import *

def display(automaton,writeInText,fileName=""):
    alphabet = [chr(ord('a')+k) for k in range(len(automaton[0][2:]))]
    if writeInText:alphabet[-1]="e"
    else:alphabet[-1]="€"

    bool_=True
    for line in automaton:
        if len(line[-1])>0:
            bool_=False
    if bool_:alphabet=alphabet[:-1]

    # Set header row
    print_(fileName,writeInText,"   " + " "*17,end="|")
    for letter in alphabet:
        print_(fileName,writeInText,"________"+str(letter),end="________|")
    print_(fileName,writeInText,"")
    for line in automaton:
        # Set header column
        if line[0]==0:
            print_(fileName,writeInText,"   ",end="")
        elif line[0]==1:
            print_(fileName,writeInText,"-->",end="")
        elif line[0] == 2:
            print_(fileName,writeInText,"<--",end="")
        else:
            print_(fileName,writeInText,"<->",end="")

        # Print the state concerned
        print_(fileName,writeInText," "*(17-len(line[1]))+line[1],end="|")
        # Print the transitions of the state
        for col in range(2,len(alphabet)+2):
            if not line[col]:
                print_(fileName,writeInText," "*17,end="|")
            else:
                names=",".join([automaton[i][1] for i in line[col]])
                print_(fileName,writeInText," "*(17-len(names))+names,end="|")
        print_(fileName,writeInText,"")
    return

def get_FA_from_file(fileName):
    # reading all lines
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')
    transitionTable=[]

    states=[]

    # putting all different state names in the list states
    # first the ones declared as input and output
    for state in linesOfFile[2].split(" ")[1:]:
        if state not in states: states.append(state)
    for state in linesOfFile[3].split(" ")[1:]:
        if state not in states: states.append(state)

    # then the ones declared in the transitions
    for transi in linesOfFile[4:len(linesOfFile)]:
        # for each letter of the alphabet
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            # if there is a transition for this letter
            if len(transiSplit)==2:
                # for each state in the transition
                for state in transiSplit:
                    if state not in states:
                        # add the state to the list of states if its not already
                        states.append(state)
        # for the empty word
        transiSplit=transi.split(" ")
        if len(transiSplit)==2:
            for state in transiSplit:
                if state not in states:
                    states.append(state)

    # sort the list of states
    states.sort()

    # add them to the transition table
    for state in states:
        transitionTable.append([0, state]+[[] for _ in range(int(linesOfFile[0])+1)])


    # add the type of state (initial, final, both, none)
    # 0 = none, 1 = initial, 2 = final, 3 = both
    for initial in linesOfFile[2].split(" ")[1:]:
        transitionTable[get_index(transitionTable, initial)][0]+=1
    for initial in linesOfFile[3].split(" ")[1:]:
        transitionTable[get_index(transitionTable, initial)][0]+=2

    # add the transitions
    for transi in linesOfFile[4:len(linesOfFile)]:
        # for each letter of the alphabet
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            
            if len(transiSplit)==2:
                transitionTable[get_index(transitionTable, transiSplit[0])][2+i].append(get_index(transitionTable, transiSplit[1]))
        # for the empty word
        transiSplit=transi.split(" ")
        if len(transiSplit)==2:
            transitionTable[get_index(transitionTable, transiSplit[0])][2+i+1].append(get_index(transitionTable, transiSplit[1]))
    return transitionTable

    
def print_(file, writeInText, msg, end="\n"):
    """
    Print the message in the console or in the file "file" based on the argument writeInText
    """
    if writeInText:
        with open("Execution_traces/"+file, "a") as f:
            f.write(msg+end)
    else:
        print(msg, end=end)

def safe_input(sentence, min_, max_):
    """
    Ask the user to input a number between min_ and max_ included
    """
    while True:
        try:
            x = int(input(sentence))
            if x < min_ or x > max_:
                print("The number must be between", min_, "and", max_)
            else:
                return x
        except ValueError:
            print("The input must be a number")