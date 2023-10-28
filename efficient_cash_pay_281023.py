#denominations 
us = {'papers': [100, 50, 20, 10, 5, 2, 1], 
      'coins': [100, 50, 25, 10, 5, 1]}

# amount = float(input("Enter amount:\n"))
amount = 20.14
whole_original = int(amount)
decimal_original = int((amount - whole_original)*100)

whole, decimal = whole_original, decimal_original

paper = []
coin = []

for i in us["papers"]:
    if i <= whole:
        number = whole // i
        whole -= number*i
        paper.append([i, number])

for i in us["coins"]:
    if i <= decimal:
        number = decimal // i
        decimal -= number*i
        coin.append([i, number])

# print((sorted(us["papers"], reverse=1)))
print(us)
print(f"paper: {paper}")
print(f"coin: {coin}", "\n")
print(amount, whole_original, decimal_original)
print("\n\n\n")

for i in paper:
    print(f"{i[1]} of {i[0]} dollars")
for i in coin:
    print(f"{i[1]} of {i[0]} cents")
