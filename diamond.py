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

"""
# Suggested by Gemini
# Make a Perfect Pointed Diamond (標準尖銳菱形)

# 上半部 (1 到 5 層)
for i in range(1, 6):
    # 空格數不變，星星數改為奇數公式：(i * 2) - 1
    print(" " * (5 - i) + "*" * (i * 2 - 1))

# 下半部 (從次寬的行遞減)
# 為了對稱，下半部我們印 4 層。這裡提供另一種更直覺的倒數寫法：
for i in range(4, 0, -1):  # 讓 i 依序變為 4, 3, 2, 1
    print(" " * (5 - i) + "*" * (i * 2 - 1))
"""

# Make a Diamond without the repeat line in the center
for i in range(1, 6):
    print(f"{' ' * (5 - i)}{'*' * (i * 2 - 1)}")

for i in range(2, 6):
    print(f"{' ' * (i - 1)}{'*' * ((6 - i) * 2 - 1)}")