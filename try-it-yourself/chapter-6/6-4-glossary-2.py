# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

word_glossary = {
    'concept_1': 'if-elif-else'
    , 'concept_2': 'for loop'
    , 'concept_3': 'list'
    , 'concept_4': 'dictionary'
    , 'concept_5': 'range'
    , 'concept_6': 'items()'
    , 'concept_7': 'keys'
    , 'concept_8': 'values'
    , 'concept_9': 'title'
    , 'concept_10': 'lower'
}

print("I already did this, just completing the exercise.\n")

for k, v in word_glossary.items():
    print("----------------------------")
    print(f"Iteration {k.split('_')[1]}")
    print("----------------------------\n")
    print(f"The key is: {k}")
    print(f"\tThe value is: {v}\n")