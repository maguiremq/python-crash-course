# 6-8. Pets: Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1 = {
    'Name': 'Skully'
    , 'Age': 13
    , 'Breed': 'Staffordshire Terrier'
    , 'Color': 'Black'
    , 'Owner': ['Taylor', 'Michael']
}

pet_2 = {
    'Name': 'Makai'
    , 'Age': 11
    , 'Breed': '["Staffordshire Terrier, American Pitbull Terrier"]'
    , 'Color': 'Brown'
    , 'Owner': ['Taylor', 'Michael']
}

pet_3 = {
    'Name': 'Adeline'
    , 'Age': 2
    , 'Breed': 'Boston Terrier'
    , 'Color': ['Brown', 'White', 'Black']
    , 'Owner': ['Taylor', 'Michael']
}

list_of_pets = [
    pet_1
    , pet_2
    , pet_3
]

for pet in list_of_pets:
    for k, v in pet.items():
        print(f"Key: {k}")
        print(f"Value: {v}")