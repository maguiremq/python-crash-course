# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.

# • Make a list of five or more usernames called current_users.

current_users = [
    'myles.graham@ufl.edu'
    , 'dallas.wilson@ufl.edu'
    , 'vernell.brown@ufl.edu'
    , 'jadan.baugh@ufl.edu'
    , 'tramell.jones@ufl.edu'
]

# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.

new_users = [
    'myles.graham@ufl.edu'
    , 'dallas.wilson@ufl.edu'
    , 'michael.q.maguire@ufl.edu'
    , 'terry.turntable@ufl.edu'
    , 'dj.lagway@ufl.edu'
]

# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.

print("\n---------------------------------------------------------")
print("Looping through new_users list - see if user already exists")
print("---------------------------------------------------------\n")

for user in new_users:
    if user in current_users:
        print(f"The person named {user.split('.')[0].title()} {user.removesuffix("@ufl.edu").split('.')[1].title()} with username {user}", "needs to enter a new username", sep = " ")

print("\n----------------------------------")
print("End Looping through new_users list")
print("----------------------------------\n")

# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

print("\n-----------------------------------")
print("Making case-insensitive comparisons")
print("-----------------------------------\n")

# Making copy of current_users and making uppercase as it is already in lowercase

current_users_copy = current_users.copy()

[current_users_copy.append(user.upper()) for user in current_users]

print(f"Checking equivalency to ensure I'm not overwriting original list.") 
print(f"`id` will check memory location. True means same; false means not same: {id(current_users_copy) == id(current_users)}")

if (id(current_users_copy) != id(current_users)):
    for user in new_users:
        if user.upper() in current_users_copy:
            print(f"The user {user.upper()} already exists! Please choose another username.")
else:
    print("The memory location of `current_users` and `current_users_copy`")

