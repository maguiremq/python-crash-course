# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

alien_color = 'green'
points = 0

if alien_color == 'green':
    print(f"Nice job. The alien's color is in fact {alien_color}!")
    print("Here's five points for your extremely smart guess!")
    points += 5

print(f"Here's to show that you have five points! Your have {points} points.")

# It says to make it fail, but that's not fun. Let's throw an `else` in there

if alien_color == 'red':
    print(f"You are actually an idiot! You said it was something other than {alien_color}!")
    print("In fact, I'm going to take five points away from you!")
    points -= 5
    print(f"Here's to show that you lost five points, loser! Your have {points} points.")

print("Now we're going to just set alien_color to red for fun")

alien_color = 'red'

if alien_color == 'red':
    print(f"You are actually an idiot! You said it was something other than {alien_color}!")
    print("In fact, I'm going to take five points away from you!")
    points -= 5
    print(f"Here's to show that you lost five points, loser! Your have {points} points.")
