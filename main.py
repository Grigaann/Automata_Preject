from Prerequisites import *

automaton_nb = str(int(input("Enter the number of the test you want to work with (1,2 or 3) : ")))
t=get_FA_from_file("Int1-3-"+automaton_nb+".txt")
display(t)

# print("\nRecognition =======================================")
# print()
# print(is_word_recognize(t, "bbbbbbabaa"))
# print()

print("\nStandardization ========================================")
standardization(t)
display(t)

print("\nDeterminization =======================================")
t=determinization(t)
# print("\nCompletion =======================================")
# t=completion(t)
display(t)