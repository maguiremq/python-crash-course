# 6-6. Polling: Use the code in favorite_languages.py (page 96).


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.

people_to_poll = [
    'tyler'
    , 'michael'
    , 'john'
    , 'sarah'
    ,
]

# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

for k, v in favorite_languages.items():
    if k.lower() not in people_to_poll:
        print(f"You already took the poll, {k.title()}! Stop wasting my time.")
    else:
        print(f"Hey, {k.title()} - you need to take the poll!")