def print_upper_words(words, must_start_with={}):

    ''' Converts/prints words to upper case and checks to see if words start with params provided.'''

    upper_words = []

    for char in must_start_with:
        for word in words:
            if word[0] == char.lower():
                to_upper = word.upper()
                upper_words.append(to_upper)
        
    new_list = ", ".join(upper_words)
    print(new_list)



# must_start_with = {}
# must_start_with={"h", "y"}

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})