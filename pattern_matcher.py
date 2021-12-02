"""
 # Write a function, get_matches, that takes two arguments, pattern (a string), and words (a list of strings).

 # e.g.: pattern = "aabba", words = ["a", "wwffw", "xxccx", "xxhhi", "aaaaa", "aaaa", "wwccw", "qqffqq"]

 # Matching words will have a one-to-one mapping between characters in the pattern and characters the word.

 # The function should return a list containing words matching the pattern.

 # In the example above, the function would return ["wwffw", "xxccx", "wwccw"]

"""
import re

def get_matches(mypattern,mywords):
    matches = []
    for w in mywords:
        if re.search(mypattern,w):
            matches.append(w)
    if len(matches) > 0:
        return matches
    return None

#
# demo:
#pattern = "aabba"
#words = ["a", "wwffw", "xxccx", "xxhhi", "aaaaa", "aaaa", "wwccw", "qqffqq"]
#
#In [108]: get_matches(pattern,words)
#
#In [109]: print(get_matches(pattern,words))
#None
#
#In [110]: print(get_matches('aaa',words))
#['aaaaa', 'aaaa']
#
#In [112]: print(get_matches('xx',words))
#['xxccx', 'xxhhi']
