# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (pages 41–42), use len() to print a message indicating the number
# of people you’re inviting to dinner.

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.

invitees = [
    'Benjamin Franklin'
    , 'George Washington'
    , 'Theodore Roosevelt'
]

print(f"Come to my dinner, {invitees[0]}, because {invitees[1]} tends to bore me.")
print(f"Just kidding, {invitees[1]}, because {invitees[0]} is an asshole.")
print(f"But both {invitees[0]} and {invitees[1]} think {invitees[2]} is an asshole.")
print(f"But now we offended {invitees[2]}, so they can no longer make it.")

new_invitee = 'Jackie Robinson'

print(f"I think we can now add {new_invitee}")

invitees.remove(invitees[2])
invitees.append(new_invitee)

print(f"Ok, {invitees[0]}, you are invited.")
print(f"I might as well invite {invitees[1]}.")
print(f"And we should all be excited for our newest invitee, {invitees[2]}!")

print(f"Hold on, everyone - I found a bigger table. Whether you like it or not, we're inviting more people.")


invitees = [
    'Benjamin Franklin'
    , 'George Washington'
    , 'Jackie Robinson'
]

new_invitees = [
    'Eleanor Roosevelt'
    , 'Tom Hanks'
    , 'Future'
]

print(f"We're adding {new_invitees[0]} since we need a Roosevelt here.")

invitees.insert(0, new_invitees[0])

print(f"Hey, {invitees[0]}, welcome to the party. You're joining the other bozos.")

invitees.insert((int(len(invitees) / 2) + 1), new_invitees[1])

print(f"Go find us a beach ball, {invitees[(int(len(invitees) / 2) + 1)]}")

invitees.append(new_invitees[2])

print(f"We have to have a modern rapper, so I invited {new_invitees[2]}\n")
print("Alright, I'm done - too many people here. I'm not printing a new message for each person.\n")

print(f"Right now, I've invited too many people -- {len(invitees)} to be exact.\n")

print("I've now been commanded to start an entirely new exercise using the same guests.\n")

print("Well, I can only invite two people now, so 2/3 of you have to go, and I'm okay with that.\n")

print("I'm going to use a loop because I'm bored of these exercises.")

for invitee in invitees:
    i = 0
    while (i < len(invitees) - 2):
        invitees.pop(i)
        ++i

print(f"Only two of you left. You are lucky, {invitees[0]} and {invitees[1]}\n")

print(f"Right now, I've got only {len(invitees)} people, so I feel less overwhelmed.\n")


