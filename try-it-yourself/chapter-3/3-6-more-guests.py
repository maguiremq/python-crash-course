# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

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
print("Alright, I'm done - too many people here. I'm not printing a new message for each person.")