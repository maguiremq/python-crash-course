fav_numbers = {
    'taylor': [
        '37'
        , '22'
        , '95'
    ]
    , 'michael': [
        '21'
        , '14'
        , '22'
        , '55'
        , '5'
    ]
    , 'john': [
        '24'
        , '42'
        , '33'
        , '42'
    ]
    , 'matt': [
        '13'
        , '22'
    ]
    , 'tyler': [
        '00'
        , '11'
        , '22'
    ]
    ,
}

for person, numbers in fav_numbers.items():
    print(f"Let's go ahead and talk to {person.title()} and get their favorite numbers.")
    print(f"They listed a total of {len(numbers)} numbers.")
    for number in numbers:
        print(f"Number is: {number}")
    print("\n")