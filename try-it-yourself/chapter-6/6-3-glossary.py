# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

programming_words = [
    'if-elif-else'
    , 'for loop'
    , 'list'
    , 'dictionary'
    , 'range'
]

word_glossary = {
    'concept_1': 'if-elif-else'
    , 'concept_2': 'for loop'
    , 'concept_3': 'list'
    , 'concept_4': 'dictionary'
    , 'concept_5': 'range'
}

# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

for k, v in word_glossary.items(): 
    print(f"The key is: {k}")
    print(f"\tThe value is: {v}\n")