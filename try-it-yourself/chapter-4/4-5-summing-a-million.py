# 4-5. Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers.

list_of_numbers = []

[list_of_numbers.append(i) for i in range(1, 1000001)]

print(f"The minimum of `list_of_numbers` is {min(list_of_numbers)}\n")
print(f"The max, though, of `list_of_numbers` is {max(list_of_numbers)}\n")

list_of_numbers = list(range(1, 1000001))

print("Testing my second method - avoiding list comprehension\n")
print(f"The minimum of `list_of_numbers` is {min(list_of_numbers)}\n")
print(f"The max, though, of `list_of_numbers` is {max(list_of_numbers)}\n")