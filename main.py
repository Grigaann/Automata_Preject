from Prerequisites import *

transitionTable=getTransitionTable("./Int1-3-1.txt")
transitionTable[3][0]=1
for line in transitionTable:
    print(line)
# print("====================================")
# print("standardization : ")
# print("====================================")
# standardization(transitionTable)
# for line in transitionTable:
#     print(line)



#print(is_deterministic(transitionTable))
print()
print("is standard ? ", is_standard(transitionTable))
print("is deterministic ? ", is_deterministic(transitionTable))
print()

print("====================================")
print("determinization : ")
print("====================================")



transitionTable=determinization(transitionTable)
for line in transitionTable:
    print(line)
print()
print("is standard ? ", is_standard(transitionTable))
print("is deterministic ? ", is_deterministic(transitionTable))