# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

list_of_toppings = []

while True:
    topping = input("Please enter a pizza topping. Enter 'quit' when complete.\n")
    print(f"I'll go ahead and add {topping} to your pizza!\n")
    list_of_toppings.append(topping)
    if topping.lower() == 'quit':
        print("Done! No more toppings.\n")
        if len(list_of_toppings) > 0:
            print("You selected the following toppings:\n")
            [print("\t" + topping) for topping in list_of_toppings if topping != 'quit']
        break