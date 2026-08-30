# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing, to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

tired_of_list_of_foods = [
    'Wrench'
    , 'Socket Wrench'
    , 'Ratcheting Wrench'
    , 'Monkey Wrench'
    , 'Impact Wrench'
]

another_tool_list = [
    'Impact Driver'
    , 'Drill'
    , 'Flathead Screwdriver'
    , 'Multimeter'
    , 'Phillips Head Screwdriver'
]

print("Begin car tool loop")
print("-" * 20, "\n")

for car_tool in tired_of_list_of_foods:
    print(f"On my car, I prefer to use a(n) {car_tool}")

print("\n", "-" * 20)
print("End car tool loop\n")

print("Begin house tool loop")
print("-" * 20, "\n")

for house_tool in another_tool_list:
    print(f"On my car, I prefer to use a(n) {house_tool}")

print("\n", "-" * 20)
print("End house tool loop")
