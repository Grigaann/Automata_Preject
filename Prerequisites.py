

def getTransitionTable(fileName):
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')

    transitionTable=[[[] for i in range(int(linesOfFile[0])+2)] for _ in range(int(linesOfFile[1]))]

    for i in range(int(linesOfFile[1])):
        transitionTable[i][1]=str(i)
        transitionTable[i][0]=0
    # 0 rien, 1 = initial, 2 = final
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

def is_standard(transitionTable):
    entry=None
    for i in range(len(transitionTable)):
        if transitionTable[i][0]%2==1: 
            if entry!= None :return False
            entry=i
    if entry == None: return False

    for line in transitionTable:
        for transition in line[2:len(line)]:
            if entry in transition: return False

    return True



def standardization(transitionTable):
    if is_standard(transitionTable):return transitionTable
    for i in range (len(transitionTable)):
        for y in range (2,len(transitionTable[i])):
            for z in range(len(transitionTable[i][y])):
                transitionTable[i][y][z]+=1
            
    #inserting new entry
    transitionTable.insert(0, [[] for _ in range(len(transitionTable[0]))])
    transitionTable[0][0]=1
    transitionTable[0][1]="i"
    
    #removing olders entrys while storing them
    oldEntry=[]
    for i in range(1,len(transitionTable)):
        if transitionTable[i][0]%2==1:
            oldEntry.append(i)
            transitionTable[i][0]=transitionTable[i][0]-transitionTable[i][0]%2

    for i in oldEntry:
        for y in range (2,len(transitionTable[i])):
            transitionTable[0][y]+=transitionTable[i][y]

    # removing doubles
    for y in range(2,len(transitionTable[0])):
        transitionTable[0][y]=list(set(transitionTable[0][y]))

    return transitionTable

def is_deterministic(transitionTable):
    entry=None
    for i in range(len(transitionTable)):
        if transitionTable[i][0]%2==1: 
            if entry!= None :return False
            entry=i
    if entry == None: return False

    for line in transitionTable:
        for transition in line[2:len(line)]:
            if len(transition)>1:return False
        
    return True

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


def determinization(transitionTable):
    newTransitionTable=[]
    names=[]
    
    # format du dico : 
    # clef : state1_state2_stat3_... dans lordre croissant
    # valeur : index dans le nv tableau

    oldEntry=[]
    for i in range(0,len(transitionTable)):
        if transitionTable[i][0]%2==1:
            oldEntry.append(i)
    fill_table(newTransitionTable, transitionTable, names, oldEntry)
    newTransitionTable[0][0]=1
    for name in names:
        if name not in [line[1] for line in newTransitionTable]:
            fill_table(newTransitionTable, transitionTable, names, list(map(int, name.split("_"))))
    
    oldExit=[]
    for i in range(0,len(transitionTable)):
        if transitionTable[i][0]>=2:
            oldExit.append(str(i))

    for i in range(len(newTransitionTable)):
        for exit in oldExit:
            if exit in newTransitionTable[i][1] and newTransitionTable[i][0]<2:
                newTransitionTable[i][0]+=2
    

    return newTransitionTable
