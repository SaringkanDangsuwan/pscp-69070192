"""ผสมสี"""

x = input()
y = input()
col1 = x.lower()
col2 = y.lower()

if col1 == "red" and col2 == "yellow":
    print("Orange")

elif col1 == "yellow" and col2 == "red":
    print("Orange")

elif col1 == "red" and col2 == "blue":
    print("Violet")

elif col1 == "blue" and col2 == "red":
    print("Violet")

elif col1 == "yellow" and col2 == "blue":
    print("Green")

elif col1 == "blue" and col2 == "yellow":
    print("Green")

elif col1 == col2 and col1 in ("red", "yellow", "blue"):
    print(x)

else:
    print("Error")
