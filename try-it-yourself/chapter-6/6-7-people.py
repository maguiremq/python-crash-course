# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

person = dict()

person1 = {
    'first_name': 'Jadan'
    , 'last_name': 'Baugh'
    , 'age': 20
    , 'city': 'Gainesville'
    ,
}

person2 = {
    'first_name': 'Michael'
    , 'last_name': 'Maguire'
    , 'age': 34
    , 'city': 'Gainesville'
    ,
}

person3 = {
    'first_name': 'Abraham'
    , 'last_name': 'Lincoln'
    , 'age': 100
    , 'city': 'Philadelphia'
    ,
}


people = [
    person1
    , person2
    , person3
]

for person in people:
    print("-------------------")
    for k, v in person.items():
        print(f"The key is: {k.title()}, and the value is: {v}")
