from Prerequisites import *
from Modification import *

automaton = get_FA_from_file("./Int1-3-1.txt")
#transitionTable[3][0]=1
display(automaton)
print()
print("is standard ? ", is_standard(automaton))
print("is deterministic ? ", is_deterministic(automaton))

print()
print("\n====================================")
print("Standardization : ")
print("====================================\n")
automaton = standardization(automaton)
display(automaton)

print()
print("is standard ? ", is_standard(automaton))
print("is deterministic ? ", is_deterministic(automaton))
print()


print("====================================")
print("Determinization : ")
print("====================================")
automaton = determinization(automaton)
display(automaton)

print("is standard ? ", is_standard(automaton))
print("is deterministic ? ", is_deterministic(automaton))