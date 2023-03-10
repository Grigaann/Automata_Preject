from Prerequisites import *

transitionTable=getTransitionTable("./Int1-3-1.txt")
for line in transitionTable:
    print(line)
print("====================================")
print("standardization : ")
print("====================================")
standardization(transitionTable)
for line in transitionTable:
    print(line)
