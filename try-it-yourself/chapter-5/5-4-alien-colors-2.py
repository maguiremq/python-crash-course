# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5
# points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.

# alien_color = 'green'
# points = 0

# if alien_color == 'green':
#     print(f"Nice job. The alien's color is in fact {alien_color}!")
#     print("Here's five points for shooting the alien!\n")
#     points += 5
# elif alien_color != 'red':
#     print("Wow, how did you know the alien's color wasn't green?")
#     print("Here's ten points for an unkown reason! The book doesn't say why!\n")
#     points += 10
# else:
#     print("What the hell were you thinking? That isn't a color option.")

points = 0

alien_colors = [
    'green'
    , 'yellow'
    , 'red'
]

print(f"You are starting with {points} points.")

for color in alien_colors:
    points = 0
    if color == 'green':
        print(f"Nice job. The alien's color is in fact {color}!")
        print("Here's five points for shooting the alien!\n")
        points += 5
        print(f"Your points: {points}")
    elif color != 'red':
        print("Wow, how did you know the alien's color wasn't green?")
        print("Here's ten points for an unkown reason! The book doesn't say why!\n")
        points += 10
        print(f"Your points: {points}")
    else:
        print("What the hell were you thinking? That isn't a color option.")
        print(f"Your points: {points}")
        print(f"In fact, let's make you lose points. Bam! {points - 10}")