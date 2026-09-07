# # 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# # CTRL-C or close the window displaying the output.)

# x = 1

# while x < 5:
#     print(x)

unconfirmed_users = [
    'alice'
    , 'brian'
    , 'candace'
]

confirmed_users = []

while unconfirmed_users:
    print("---")
    print(f"Unconfirmed users is: {unconfirmed_users}\n")
    current_user = unconfirmed_users.pop()
    print(f"\tUnconfirmed users is now: {unconfirmed_users}")
    print(f"Confirmed users length: {len(unconfirmed_users)}")
    print("---")


    print("---")
    print(f"Confirmed users is: {confirmed_users}\n")
    confirmed_users.append(current_user)
    print(f"\tConfirmed users is now: {confirmed_users}")
    print(f"Confirmed users length: {len(confirmed_users)}")
    print("---")

print("--- End ---\n")
print(f"Unconfirmed users: {unconfirmed_users}")
print(f"Confirmed users: {confirmed_users}")