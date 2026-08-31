# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

points = 0

# Avoiding writing three versions - just using the same for loop

alien_colors = [
    'green'
    , 'yellow'
    , 'red'
    , 'blue'
]

print(f"You are starting with {points} points.")

for color in alien_colors:
    points = 0
    if color == 'green':
        print(f"You guessed: {color}!")
        print("Here's five points for shooting the alien!\n")
        points += 5
        print(f"Your points: {points}")
    elif color == 'yellow':
        print(f"You guessed: {color}!")
        print("Yellow? Hell of a guess! It is in fact yellow!")
        points += 10
        print(f"Your points: {points}")
    elif color == 'red':
        print(f"You guessed: {color}!")
        print("Red is the color of the alien. You're a genius.")
        points += 15
        print(f"Your points: {points}")
    else:
        print(f"You guessed: {color}!")
        print("What the hell were you thinking? That isn't a color option.")
        print(f"Your points: {points}")
        print(f"In fact, let's make you lose points. Bam! {points - 10}")