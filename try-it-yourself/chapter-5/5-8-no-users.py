# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message
# is printed.

usernames = [
    'michael.maguire'
    , 'maguire.michael'
    , 'maguire.michael.quinn'
    , 'quinn.maguire'
    , 'admin'
]

for user in usernames:
    usernames.remove(user)

if usernames:
    print("The list is empty - need to find some users")
else:
    print("The list has people in it still!")