# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

# total_people = int(input("Welcome to the movie theater. How many people in your party?"))

# for person in range(0, total_people):
#     total = 0
#     person_age = int(input(f"How old is person #{person + 1}?"))
#     if person_age > 0 and person_age < 3:
#         print(f"A person who is {person_age} is free - no charge!")
#     elif person_age >= 3 and person_age < 13:
#         print(f"A person who is {person_age} costs $10 to enter the movie theater.")
#         total += 10
#     else:
#         print(f"A person who is {person_age} costs $15 to enter the movie theater.")
#         total += 15
#     print(f"The final total is ${total} and I only take cash.")

# print(f"The total charge is: ${total} and I only take cash.")

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

    