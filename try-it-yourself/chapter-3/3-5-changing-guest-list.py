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