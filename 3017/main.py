"""Bill"""

price = int(input())
charge = price * 0.1

if charge < 50:
    charge = 50

elif charge > 1000:
    charge = 1000

total = (price + charge) * 1.07

print(f"{total:.2f}")
