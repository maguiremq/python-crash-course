# 3-10. Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

things_in_list = [
    'Ioniq 5'
    , 'Camry'
    , 'Mustang'
]

method_of_purchase = [
    'bought'
    , 'stole'
    , 'inherited'
]
print(f"I've owned three cars in my life, and I just bought the {things_in_list[0]}.\n")
print("In fact, I've never bought a car from a dealer until now.\n")
print("I think this exercise seems a little ridiculous and lazy, but I'll do it anyway.\n")

# Accessing items

print(("-" * 5), "| --------------------- |", ("-" * 5))
print(("*" * 5), "| Begin accessing Items |", ("*" * 5))
print(("-" * 5), "| --------------------- |", ("-" * 5), "\n")

for i in range(len(things_in_list)):
    print(f"I {method_of_purchase[i]} the {things_in_list[i]}.")
    print(f"I {method_of_purchase[i].upper()} the {things_in_list[i].lower()}.")
    print(f"I {method_of_purchase[i * -1]} the {things_in_list[i * 1]}.\n")

print(("-" * 5), "| ------------------- |", ("-" * 5))
print(("*" * 5), "| End accessing Items |", ("*" * 5))
print(("-" * 5), "| ------------------- |", ("-" * 5), "\n")

print("Actually, I'm done - kind of over this chapter.\n")

