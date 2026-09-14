# Make a Right Angle Triangle
for i in range(1, 6):
    print("*" * i)


# Make an upside down Right Angle Triangle
for i in range(1, 6):
    print("*" * (6 - i))


# Make an inverted Right Angle Triangle
for i in range(1, 6):
    print(f"{' ' * (5 - i)}{'*' * i}")    #print(" " * (6 - i) + "*" * i)


# Make an upside down inverted Right Angle Triangle
for i in range(1, 6):
    print(f"{' ' * (i - 1)}{'*' * (6 - i)}")    #print(" " * (i - 1) + "*" * (6 - i))


# Make an Isosceles Triangle
for i in range(1, 6):
    print(f"{' ' * (5 - i)}{'*' * i * 2}")    #print(" " * (5 - i) + "*" * i * 2)


# Make an upside down Isoceles Triangle
for i in range(1, 6):
    print(f"{' ' * (i - 1)}{'*' * (6 - i) * 2}")    #print(" " * (i - 1) + "*" * (6 - i) * 2)


# Make a Diamond without the repeat line in the center
for i in range(1, 6):
    print(f"{' ' * (5 - i)}{'*' * (i * 2 - 1)}")

for i in range(2, 6):
    print(f"{' ' * (i - 1)}{'*' * ((6 - i) * 2 - 1)}")