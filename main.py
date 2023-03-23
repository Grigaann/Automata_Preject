from Prerequisites import *

debugger_mode = int(input("Enter 1 if you want to create the execution traces or 0 if you want to use an automaton : "))
if debugger_mode==0: writeInText=False
else: writeInText=True

if writeInText:
    automata_list = [str(i+1) for i in range(44)]
    for automaton_nb in automata_list:
        fileName="Int1-3-"+automaton_nb+".txt"
        with open("Execution_traces/"+fileName, "w") as f:
            f.write("This file is the execution trace of the automaton number : "+automaton_nb+".\n")

        t=get_FA_from_file("Automata_tests/"+fileName)
        display(t,writeInText, fileName)

        print_(fileName,writeInText,"\nStandardization =============================================================================")
        if is_standard(t):
            print_(fileName,writeInText,"This automaton is already standard.")
        else:
            standardization(t)
            display(t,writeInText, fileName)

        print_(fileName,writeInText,"\nDeterminization =============================================================================")
        if is_deterministic(t):
            print_(fileName,writeInText,"This automaton is already deterministic.")
        else:
            t=determinization(t)
            display(t,writeInText, fileName)

        print_(fileName,writeInText,"\nCompletion ==================================================================================")
        if is_complete(t):
            print_(fileName,writeInText,"This deterministic automaton is already complete.")
        else:
            t=completion(t)
            display(t,writeInText, fileName)

        print_(fileName,writeInText,"\nComplement ==================================================================================")
        t=complentary(t)
        display(t,writeInText, fileName)

        print_(fileName, writeInText, "The empty word is recognized.")if is_word_recognized(t, "")else print_(fileName, writeInText, "The empty word is not recognized.")

        for word in ["a", "b", "c", "ab", "ba", "bc", "cb", "ac", "ca", "abc", "acb", "bac", "bca", "cab", "cba", "abac", "abca", "acba", "bacb", "bcab", "bcba", "cabac", "cabca", "cacba", "cbacb", "cbcab", "cbcba"]:
            if is_word_recognized(t, word):
                print_(fileName,writeInText,"The word : " +word+ " is recognized.")
            else :
                print_(fileName,writeInText,"The word : " +word+ " is not recognized.")
    print("The execution traces have been created with success!")


else:
    while True:
        automaton_nb = str(int(input("Enter the number of the automaton you want to work with : ")))
        automaton = get_FA_from_file("Automata_tests/Int1-3-"+automaton_nb+".txt")
        print("\n\nBelow is the automaton you are using :\n")
        display(automaton,writeInText)
        looping = True
        while looping:
            answer = int(input("What do you want to do with this automaton ?\n"
                               "\tEnter 1 if you want to see it.\n"
                               "\tEnter 2 if you want to reinitialise the automaton\n"
                               "\tEnter 3 if you want to standardize it.\n"
                               "\tEnter 4 if you want to determinize it.\n"
                               "\tEnter 5 if you want to complete it.\n"
                               "\tEnter 6 if you want to work with its complementary language.\n"
                               "\tEnter 7 if you want to check a word recognition.\n"
                               "\tEnter 0 if you want to change the automaton you work with.\n"
                               "Your answer : "))

            if answer==0:
                looping=False

            if answer==1:
                print("Here it is :\n")
                display(automaton,writeInText)

            if answer==2:
                automaton = get_FA_from_file("Automata_tests/Int1-3-" + automaton_nb + ".txt")
                print("\nThe automaton has been reinitialised based on the according file.")

            if answer==3:
                print("\nStandardization =============================================================================")
                if is_standard(automaton):
                    print("This automaton is already standard.")
                else:
                    automaton=standardization(automaton)
                    display(automaton,writeInText)

            if answer==4:
                print("\nDeterminization =============================================================================")
                if is_deterministic(automaton):
                    print("This automaton is already deterministic.")
                else:
                    automaton=determinization(automaton)
                    display(automaton,writeInText)

            if answer==5:
                print("\nCompletion ==================================================================================")
                if is_complete(automaton):
                    print("This automaton is already complete.")
                else:
                    automaton=completion(automaton)
                    display(automaton,writeInText)

            if answer==6:
                print("\nComplement ==================================================================================")
                automaton=complentary(automaton)
                display(automaton,writeInText)

            if answer==7:
                word = str(input("Enter a word to be checked by the automaton : "))
                if word == "":
                    print("The empty word is recognized.") if is_word_recognized(automaton, word) else print("The empty word is not recognized.")
                else:
                    if is_word_recognized(automaton, word):
                        print("The word \"" +word+ "\" is recognized.")
                    else:
                        print("The word \"" +word+ "\" is not recognized.")
            print("================================================================================================")