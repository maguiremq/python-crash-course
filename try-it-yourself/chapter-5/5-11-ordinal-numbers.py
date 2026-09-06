# ------------------------------------------------------------------------------
# 5-11. Ordinal Numbers: 
# 
# Ordinal numbers indicate their position in a list, such as
# 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#
# • Store the numbers 1 through 9 in a list.
#
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
# 8th 9th", and each result should be on a separate line.
# ------------------------------------------------------------------------------

list_of_ordinal_numbers = list(range(1, 10))

print(f"The list of ordinal numbers is: {list_of_ordinal_numbers}")

# • Loop through the list.

print("\n----------")
print(f"Loop time!")
print("----------\n")

[print(f"The current iteration returns {i}!") for i in list_of_ordinal_numbers]

print("\n--------------")
print(f"End Loop time!")
print("--------------\n")

# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
# 8th 9th", and each result should be on a separate line.

print(f"Exercise: if-elif-else chain for {list_of_ordinal_numbers}")

print("\n-------------------------")
print("Begin if-elif-else chain!")
print("-------------------------\n")

for number in list_of_ordinal_numbers:
    if number == 1:
        print(f"{number}st!")
    elif number in (2, 3):
        print(f"{number}rd!")
    else:
        print(f"{number}th!")

print("\n---------------------")
print("End if-elif-else chain!")
print("----------------------\n")
