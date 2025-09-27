# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

#--1--
# def counting_vowels_and_consonants(paragraph):

aha = paragraph.count('a').count('e')
print(aha)

# def counting_vowels_and_consonants(paragraph):
#     a = paragraph.count('a')
#     e = paragraph.count('e')
#     i = paragraph.count('i')
#     o = paragraph.count('o')
#     u = paragraph.count('u')
#     A = paragraph.count('A')
#     E = paragraph.count('E')
#     I = paragraph.count('I')
#     O = paragraph.count('O')
#     U = paragraph.count('U')
#     vowels = a + e + i + o+u+A+E+I+O+U
#     consonants = len(paragraph.replace(' ','')) - vowels
#     return (vowels,consonants )
# counting_vowels_and_consonants(paragraph)

def counting_vowels_and_consonants(paragraph):
    paragraph = paragraph.lower()
    vowels = 'aeiou'
    vowelct = sum(paragraph.count(v) for v in vowels)
    consonants = len(paragraph.replace(' ', '')) - vowelct
    return (vowelct, consonants)
counting_vowels_and_consonants(paragraph)

# --2--
def average_vowels_and_consonants(paragraph):
    import re
    import numpy as np
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())
    vowelct = []
    consonants = []
    for s in sentences:
        v,c = counting_vowels_and_consonants(s)
        avgv = vowelct.append(v)
        avgc = consonants.append(c)
    avgv = np.average(vowelct)
    avgc = np.average(consonants)
    print(len(sentences), avgv, avgc)
average_vowels_and_consonants(paragraph)