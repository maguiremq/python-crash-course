# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwich_orders = [
    'Caprese'
    , 'Italian'
    , 'Roast Beef'
]

finished_sandwiches = list()

while sandwich_orders:
    sandwich_iteration = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_iteration)

print(f"You ordered a total of {len(finished_sandwiches)} sandwiches.\n")
[print(f"\tYour {sandwich} sandwich is ready at the window.\n") for sandwich in finished_sandwiches]