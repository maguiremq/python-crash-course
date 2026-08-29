# 3-8. Seeing the World: Think of at least five places in the world you’d like
# to visit.

places_to_visit = [
    'Germany'
    , 'England'
    , 'Norway'
    , 'Italy'
    , 'Greece'
]

# • Store the locations in a list. Make sure the list is not in alphabetical order.

places_to_visit = [
    'Germany'
    , 'England'
    , 'Norway'
    , 'Italy'
    , 'Greece'
]


# • Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.

print(f"These are the places I want to visit (or already have: {places_to_visit}\n")

# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.

print(f"Now I'm going to print them but not modify the original list: {sorted(places_to_visit)}\n")

# • Show that your list is still in its original order by printing it.

print(f"Make sure the list is still in its own order: {places_to_visit}\n")

# • Use sorted() to print your list in reverse-alphabetical order without changing
# the order of the original list.

print(f"Now let's not change the list but sort it in reverse alphabetical order: {sorted(places_to_visit, reverse = True)}\n")

# • Show that your list is still in its original order by printing it again.

print(f"Make sure the list is still in its own order: {places_to_visit}\n")

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.

places_to_visit.reverse()

print(f"We reversed the original list - check here: {places_to_visit}\n")

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.

places_to_visit.reverse()

print(f"Just using the reverse method again - check here: {places_to_visit}\n")

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.

places_to_visit.sort()

print(f"Should be in alphabetical order now: {places_to_visit}\n")

# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

places_to_visit.sort(reverse = True)

print(f"Should be in reverse alphabetical order: {places_to_visit}\n")