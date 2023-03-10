

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

def isStandard(transitionTable):
    entry=None
    for i in range(len(transitionTable)):
        if transitionTable[i][0]%2==1: 
            if entry!= None :return False
            entry=i
    if entry == None: return False

    for line in transitionTable:
        for transition in line[2:len(line)]:
            if i in transition: return False

    return True



def standardization(transitionTable):
    if isStandard(transitionTable):return transitionTable
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