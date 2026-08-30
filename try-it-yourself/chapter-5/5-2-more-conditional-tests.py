# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create
# to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

print("I'm skipping the first two; see 5-1-conditional-tests.py")


print("Is 2 not equal to 2? Check:", 2 != 2)
print("Is 2 equal to 2? Check:", 2 == 2)
print("Is 2 greater than 1? Check:", 2 > 1)
print("Is 2 greater than or equal to 2? Check:", 2 >= 2)
print("Is 5 less than 2? Check:", 5 < 2)
print("Is 5 less than or equal to 7? Check:", 5 <= 7)
print("Is 5 less than 7, and is 2 equal to 2? Check:", (5 < 7) & (2 == 2))
print("Is 5 less than 6, or is 6 greater than 5? Check:", (5 < 6) | (6 < 5))

list_of_random_stuff = [
    'Poetry'
    , 'Books'
    , 'Programming'
]

print("Check if books are in the list. Check:", 'Books' in list_of_random_stuff)
print("Check if socks are in the list. Check:", 'Socks' in list_of_random_stuff)