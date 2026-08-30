# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.

# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.

animals = [
    'American Staffordshire Terrier'
    , 'American Bulldog'
    , 'Boston Terrier'
    , 'Red-shouldered Hawk'
    , 'Deer'
    , 'Koala Bear'
]

for animal in animals:
    print(f"A {animal} is a silly pet\n")

print("I own all three (or they do me), and they are all goofy in their own ways.\n")

print("Now we're going to move to exercise 4-10\n")

print("-" * 5, "Show First Three Items", "-" * 5)
print(f"The first three items in the list are: {animals[:2]}")
print("-" * 5, "End First Three Items", "-" * 5, "\n")

middle_position = (len(animals) // 2) - 1
three_from_middle = (len(animals) // 2) + 2

print("-" * 5, "Show Middle Three Items", "-" * 5)
print(f"The middle three items in the list are: {animals[middle_position:three_from_middle]}")
print("-" * 5, "End Middle Three Items", "-" * 5, "\n") 

print("-" * 5, "Show Last Three Items", "-" * 5)
print(f"The last three items in the list are: {animals[-3:]}")
print("-" * 5, "End Last Three Items", "-" * 5, "\n") 




