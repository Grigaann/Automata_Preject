from Prerequisites import *


automaton_nb = str(int(input("Enter the number of the test you want to work with (1,2 or 3) : ")))
t=get_FA_from_file("Automata_tests/Int1-3-"+automaton_nb+".txt")
display(t)

print("\nDeterminization =======================================")
t_=determinization(t)

print("\Completion =======================================")
t_=completion(t)

display(t_)

print("\nStandardization ========================================")
standardization(t)
display(t)

print("\nDeterminization =======================================")
t=determinization(t)

display(t)