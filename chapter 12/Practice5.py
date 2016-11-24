user_dictionary = {}
while 1:
    command = raw_input("'a' to add word, 'l' to lookup a word, 'q' to quit ")

    if command == "a":
        word = raw_input("Type the word: ")
        definition = raw_input("Type the definition: ")
        user_dictionary[word] = definition
        print "Word added!"

    elif command == "l":
        word = raw_input("Type the word: ")
        if word in user_dictionary.keys():
            print user_dictionary[word]
        else:
            print "That word isn't in the dictionary yet."

    elif command == 'q':
        break
