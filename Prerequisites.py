from Modification import *

def display(automaton):
    alphabet = [chr(ord('a')+k) for k in range(len(automaton[0][2:]))]
    alphabet[-1]="€"
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

        # Print the state concerned
        print(" "*(17-len(line[1]))+line[1],end="|")
        # Print the transitions of the state
        for col in range(2,len(line)):
            if not line[col]:
                print(" "*17,end="|")
            else:
                print(" "*(17-(2*len(line[col])-1))+",".join([str(i) for i in line[col]]),end="|")
        print()
    return

def get_FA_from_file(fileName):
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')
    print(linesOfFile)
    transitionTable=[[[] for i in range(int(linesOfFile[0])+3)] for _ in range(int(linesOfFile[1]))]

    for i in range(int(linesOfFile[1])):
        transitionTable[i][1]=str(i)
        transitionTable[i][0]=0
    # 0 = none, 1 = initial, 2 = final, 3 = both
    for initial in linesOfFile[2].split(" ")[1:]:
        transitionTable[int(initial)][0]+=1
    for initial in linesOfFile[3].split(" ")[1:]:
        transitionTable[int(initial)][0]+=2

    for transi in linesOfFile[4:len(linesOfFile)]:
        for i in range(int(linesOfFile[0])):
            transiSplit=transi.split(chr(ord('a')+i))
            
            if len(transiSplit)==2:
                transitionTable[int(transiSplit[0])][2+i].append(int(transiSplit[1]))
        transiSplit=transi.split(" ")
        if len(transiSplit)==2:
            transitionTable[int(transiSplit[0])][2+i+1].append(int(transiSplit[1]))
            
    return transitionTable


def get_index_from_letter(letter):
    return ord(letter)-ord('a')