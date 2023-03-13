from Prerequisites import *

transitionTable=getTransitionTable("./Int1-3-1.txt")
#transitionTable[3][0]=1
for line in transitionTable:
    print(line)
# print("====================================")
# print("standardization : ")
# print("====================================")
# standardization(transitionTable)
# for line in transitionTable:
#     print(line)



#print(is_deterministic(transitionTable))
# print()
# print("is standard ? ", is_standard(transitionTable))
# print("is deterministic ? ", is_deterministic(transitionTable))
# print()

print("====================================")
print("determinization : ")
print("====================================")



transitionTable=determinization(transitionTable)
for line in transitionTable:
    print(line)
print()
print("is standard ? ", is_standard(transitionTable))
print("is deterministic ? ", is_deterministic(transitionTable))


print()
print("====================================")
print("recognition : ")
print("====================================")
print()

def a(word):
    return "recognize" if is_word_recognize(transitionTable, word) else "not recognize"

words=["abshdnfndsjn", "z", "a", "ab", "b", "abaa", "", "bbbbbbabaa"]
for word in words:
    print(f"the word '{word}' is {a(word)}")

print()
print("====================================")
print("completion : ")
print("====================================")
print()

transitionTable = complete(transitionTable)

for line in transitionTable:
    print(line)