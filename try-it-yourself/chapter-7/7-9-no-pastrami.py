# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = [
    'Caprese'
    , 'Italian'
    , 'Roast Beef'
    , 'Pastrami Sandwich'
    , 'Meat Lovers with Pastrami'
    , 'Pastrami Stromboli'
]

finished_sandwiches = list()

print("Hello, welcome to the deli. Before you order, I just wanted to let you know that we are out of Pastrami.\n")
print("What can I get for you today?")

ordering = True

while sandwich_orders:
    sandwich_iteration = sandwich_orders.pop()
    print(f"Okay, so you want a {sandwich_iteration} sandwich?\n")
    if sandwich_iteration.lower().find('pastrami') == -1:
        finished_sandwiches.append(sandwich_iteration)
    else:
        print(f"The {sandwich_iteration} sandwich has pastrami in it you dummy!\n")
    # while sandwich_iteration.lower().find("pastrami") == 0:
    #     print("We're out of pastrami.")
    #     finished_sandwiches.remove(sandwich_iteration)

[print(f"\tThe {sandwich} sandwich is ready for pickup.") for sandwich in finished_sandwiches]