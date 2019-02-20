#Goods and price

goods = { "Apple": 4.5,
           "Orange": 6.2,
           "Pineapple": 10.0,
           "Mango":7.5,
           "Banana":3.8}

for good, price in goods.items():
    print(good, "-", price)

cost =0
while True:
    good = input("What? (n - nothing) ")
    if good == 'n':
        break
    qty = int(input("How many? "))
    cost += goods[good] * qty
print("Price: ", cost)