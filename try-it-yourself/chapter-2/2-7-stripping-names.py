# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

x = "Michael\n"

print("Testing with a newline separator")
print("The original name was" + x, sep = " ")
print("Removing the whitespace with `strip` results in:",  x.strip(), "|", sep = " ")
print("Removing the whitespace with `rstrip` results in:", x.rstrip(), sep = " ")
print("Removing the whitespace with `lstrip` results in:", x.lstrip(), sep = " ")

x = "Michael\n"

print("Testing with a tab separator")
print("The original name was" + x, sep = " ")
print("Removing the whitespace with `strip` results in:",  x.strip(), sep = " ")
print("Removing the whitespace with `rstrip` results in:", x.rstrip(), sep = " ")
print("Removing the whitespace with `lstrip` results in:", x.lstrip(), sep = " ")