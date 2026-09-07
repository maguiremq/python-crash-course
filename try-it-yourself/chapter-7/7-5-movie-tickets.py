# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

total = 0

while True:
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

    