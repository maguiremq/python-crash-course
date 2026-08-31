# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

fav_fruits = [
    'apple'
    , 'blueberry'
    , 'raspberry'
]

for fruit in fav_fruits:
    if fruit == 'blueberry':
        print(f"Hell yeah, I love a {fruit}!")
    if fruit == 'raspberry':
        print(f"Yeah, a {fruit} is pretty sour, but I like sour things.")
    if fruit == 'apple':
        print(f"An {fruit} a day keeps the doctor away!")
    if fruit == 'pineapple':
        print("That's a teenager. Tough part of life, that's for sure.")
    if fruit == 'pineapple':
        print("Pineapples are good, sometimes hurt my gums.")
    if fruit == 'pear':
        print("Dude, I am not a pear fan, unfortunately.")