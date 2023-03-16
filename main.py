from Prerequisites import *

#empty word : `

automaton_nb = str(int(input("Enter the number of the test you want to work with (1,2 or 3) : ")))
t=get_FA_from_file("Automata_tests/Int1-3-"+automaton_nb+".txt")
display(t)
#print(is_word_recognized(t, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

# print("\nDeterminization =======================================")
# t_=determinization(t)

# print("\Completion =======================================")
# t_=completion(t)

# display(t_)

# print("\nStandardization ========================================")
# standardization(t)
# display(t)
print()
print()
print()
print()
print("\nDeterminization =======================================")
print("is deterministic ? ", is_deterministic(t))
t=determinization(t)
display(t)


with open("correct.txt") as file:
    for line in file:
        if not is_word_recognized(t, line[:-1]):
            print("error", line[:-1])
            break

with open("false.txt") as file:
    for line in file:
        if is_word_recognized(t, line[:-1]):
            print("error", line[:-1], is_word_recognized(t, line[:-1]))
            break

