# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:

car = 'Hyundai'

print(f"Is the car a hyundai? {car == 'hyundai'}")
print(f"Ok, so is the car a Hyundai? {car == 'Hyundai'}")

list_of_tests = [
    'hyundai'
    , 'BMW'
    , 'pontiac'
    , 'ASTON MARTIN'
    , 'fORD'
    , 'Chevrolet'
    , 'Toyota'
    , 'Honda'
    , 'Kia'
    , 'Polestar'
]

for test in list_of_tests:
    print(f"Is the car in propercase? Let's check: {test.title() == test}")

