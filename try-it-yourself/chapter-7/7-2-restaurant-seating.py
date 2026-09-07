# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

number_dinner_group = int(input("Please tell me how many people are in your dinner party?\n"))

if number_dinner_group > 8:
    print("Look, you need to wait for a table. Make a reservation next time.")
else:
    print(f"Nice! {number_dinner_group} is something we can accomodate. Your table is ready.")