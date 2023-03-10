from Prerequisites import *

transitionTable=getTransitionTable("./Int1-3-1.txt")
for line in transitionTable:
    print(line)
print("====================================")
print("standadization : ")
print("====================================")
standardization(transitionTable)
for line in transitionTable:
    print(line)
