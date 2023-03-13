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


def fill_table(newTransitionTable, transitionTable, names, listState):
    newLine=[]
    
    allTransition=[[] for _ in range(len(transitionTable[0])-2)]

    for i in range(len(transitionTable)):
        if i in listState:
            for y in range(2,len(transitionTable[i])):
                allTransition[y-2]+=transitionTable[i][y]
            allTransition[y-2]=list(set(allTransition[y-2]))
            allTransition[y-2].sort()

    listState=list(map(lambda x: str(x), listState))
    newLine.append(0)
    newLine.append("_".join(listState))
 
    if "_".join(listState) not in names : names.append("_".join(listState))
    for transition in allTransition: 
        tmp=list(map(lambda x: str(x), transition))
        if "_".join(tmp) not in names : names.append("_".join(tmp))
        newLine.append([names.index("_".join(tmp))])

    newTransitionTable.append(newLine)