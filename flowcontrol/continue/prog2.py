cart = [10, 20, 700, 30, 600, 60, 70]
for item in cart:
    if item > 500:
        print("We cannot process this item :", item)
        continue
    print(item)
