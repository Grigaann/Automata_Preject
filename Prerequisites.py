

def getTransitionTable(fileName):
    linesOfFile=[]
    with open(fileName, "r") as f:
        linesOfFile=f.read().split('\n')

    transitionTable=[[[] for i in range(int(linesOfFile[0])+2)] for _ in range(int(linesOfFile[1]))]

    for i in range(int(linesOfFile[1])):
        transitionTable[i][1]=i
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