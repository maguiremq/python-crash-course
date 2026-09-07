# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:

# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

total = 0

active = True

while active:
    age_input = input("What is the age of the person attending the movie? Tell me 'stop' when finished.\n")
    if age_input == 'stop':
        break
    if int(age_input) < 0:
        print("Please enter a valid age.")
        continue
    elif int(age_input) >= 0 and int(age_input) < 3:
        print("That person is free!")
    elif int(age_input) >= 3 and int(age_input) < 13:
        print("That person will cost $10.")
        total += 10
    else:
        print("That person will cost $15.")
        total += 15

print(f"Your total today will be ${total}.00, and I only allow cash for tax purposes.")
print("You can get an additional discount of $15.00 if you pay with gold now.")
print(f"That would mean your total would be ${total - 15} if you pay with gold or bitcoin.")

    