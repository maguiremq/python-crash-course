# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.

list_comp_of_10_cubes = []

for i in range(1, 11):
    list_comp_of_10_cubes.append(i ** 3)

print(f"Here's my list of 10 cubes! {list_comp_of_10_cubes}")