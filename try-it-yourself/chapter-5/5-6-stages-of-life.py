# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage
# of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that the
# person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

ages = [5, 61, 12, 55, 32, 89, 1]

for age in ages:
    if age < 2:
        print("That's a baby. They're expensive.")
    elif age >= 2 and age < 4:
        print("Yep, that's a toddler. Have fun.")
    elif age >= 4 and age < 13:
        print("That's a kid - they're gonna get some attitude, especially around thirteen.")
    elif age >= 13 and age < 20:
        print("That's a teenager. Tough part of life, that's for sure.")
    elif age >= 20 and age < 65:
        print("That's an adult. Welcome to hell.")
    elif age >= 65:
        print("You are an elder. Cash in on your retirment and social security!")
    else:
        print("What age are you even?")