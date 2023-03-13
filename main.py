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
print("Standardization :")
print("====================================\n")
automaton = standardization(automaton)
display(automaton)

print()
print("is standard ? ", is_standard(automaton))
print("is deterministic ? ", is_deterministic(automaton))
print()


print("====================================")
print("Determinization :")
print("====================================")
automaton = determinization(automaton)
display(automaton)

print("is standard ? ", is_standard(automaton))
print("is deterministic ? ", is_deterministic(automaton))


# print()
# print("====================================")
# print("Recognition :")
# print("====================================")
# print()

# def a(word):
#     return "recognize" if is_word_recognize(automaton, word) else "not recognize"

# words=["abshdnfndsjn", "z", "a", "ab", "b", "abaa", ""]
# for word in words:
#     print(f"the word '{word}' is {a(word)}")

print()
print("====================================")
print("Completion :")
print("====================================")
print()

automaton = complete(automaton)
display(automaton)