# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number_entered = int(input("Submit an integer:\n"))

if number_entered % 10 == 0:
    print(f"{number_entered} is a multiple of ten!")
else:
    print(f"{number_entered} is not a multiple of ten.")