from Prerequisites import *

#empty word : `

writeInText=True

if not writeInText:automaton_nb_list = [str(int(input("Enter the number of the test you want to work with (1,2 or 3) : ")))]
else:automaton_nb_list = [str(i+1) for i in range(44)]
for automaton_nb in automaton_nb_list:
    fileName="Int1-3-"+automaton_nb+".txt"
    with open("Execution_traces/"+fileName, "w") as f:
        f.write("This file is the execution trace of the automaton number : "+automaton_nb+"\n")
    
    t=get_FA_from_file("Automata_tests/"+fileName)

    display(writeInText, fileName,t)
    print_(fileName,writeInText,"\nStandardization =============================================================================")

    if is_standard(t): print_(fileName,writeInText,"This automata is already standard")
    else:
        standardization(t)
        display(writeInText, fileName,t)
    print_(fileName,writeInText,"\nDeterminization =============================================================================")
    if is_deterministic(t): print_(fileName,writeInText,"This automata is already deterministic")
    else:
        t_=determinization(t)
        display(writeInText, fileName,t_)
    print_(fileName,writeInText,"\nCompletion ==================================================================================")
    if is_complete(t): print_(fileName,writeInText,"This automata is already complete")
    else:
        t_=completion(t)
        display(writeInText, fileName,t_)
    print_(fileName,writeInText,"\nComplement ==================================================================================")
    t_=complentary(t)
    display(writeInText, fileName,t_)

    print_(fileName,writeInText,"")
    for word in ["a", "b", "c", "ab", "ba", "bc", "cb", "ac", "ca", "abc", "acb", "bac", "bca", "cab", "cba", "abac", "abca", "acba", "bacb", "bcab", "bcba", "cabac", "cabca", "cacba", "cbacb", "cbcab", "cbcba"]:
        if is_word_recognized(t, word):
            print_(fileName,writeInText,"The word :  " +word+ " is recognized")
        else :
            print_(fileName,writeInText,"The word :  "+ word+ " is not")


