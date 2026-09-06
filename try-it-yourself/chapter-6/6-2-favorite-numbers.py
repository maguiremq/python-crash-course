# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

fav_numbers = {
    'taylor': '37'
    , 'michael': '21'
    , 'john': '24'
    , 'matt': '13'
    , 'tyler': '00'
}

for k, v in fav_numbers.items():
    print(f"{k.title()}'s favorite number is: {v}\n")