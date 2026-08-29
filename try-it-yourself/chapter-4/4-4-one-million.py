# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)

one_million = 1000000

for i in range(1, one_million + 1):
    print(i)
    if i > 25:
        break