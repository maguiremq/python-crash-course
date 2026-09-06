# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.

dict_of_rivers = {
    'mississippi': 'louisiana'
    , 'erie': 'new york'
    , 'ohio': 'no idea'
}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

print("I did states instead of countries because my river knowledge sucks.\n")

string_loop = "Loop through name of each river and state"
border_loop = "-" * len(string_loop)

print(border_loop)
print(string_loop)
print(border_loop)

for k, v in dict_of_rivers.items():
    print(f"The {k} runs through (or maybe doesn't) {v}.")

# • Use a loop to print the name of each river included in the dictionary.

string_loop = "Loop through name of each river"
border_loop = "-" * len(string_loop)

print(border_loop)
print(string_loop)
print(border_loop)

for key in dict_of_rivers.keys():
    print(key)

# • Use a loop to print the name of each country included in the dictionary.

string_loop = "Loop through name of each country"
border_loop = "-" * len(string_loop)

print(border_loop)
print(string_loop)
print(border_loop)

for value in dict_of_rivers.values():
    print(value)