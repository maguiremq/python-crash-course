# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
# following:

# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas
# are:, and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

pizzas = [
    'Onions'
    , 'Broccoli'
    , 'Pepperoni'
]

copy_of_my_pizzas = pizzas[:]

print("Adding a new pizza to the original list! Let's add diced pepperoni because it's a different vibe\n")

pizzas.append('Diced Pepperoni')

for za in pizzas:
    print(f"This is my original list! I enjoy {za} pizza!\n")

for za in copy_of_my_pizzas:
    print(f"This is my new copy! I enjoy {za} pizza!\n")

print("I've already done the third part, so not doing it again.")