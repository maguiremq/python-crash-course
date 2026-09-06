# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.

person = dict()

person['first_name'] = 'Jadan'
person['last_name'] = 'Baugh'
person['age'] = 20
person['city'] = 'Gainesville'

print(f"The person I chose was {person.get('first_name')} {person.get('last_name')}.")
print("I don't know them, but they play for the Florida Gators.")
print(f"They are {person.get('age')} and live in {person.get('city')}, Florida.\n")

print("-----------------------------------------------------------")
print("Testing my prior knowledge on `for` loops with a dictionary.")
print("-----------------------------------------------------------\n")
for key, value in person.items():
    print(f"Key is: `{key}`; Value is '{value}'\n")