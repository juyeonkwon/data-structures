price = { "콩나물해장국":4500, "갈비탕":9000, "돈가스":8000 }
price["팟타이"] = 7000

print(price)
print(price.keys())
print(price.values())

for i in price:
    price[i] = price[i]+1000
    print(price[i])


def printNum(n):
    if n<1 : return
    printNum(n-1)
    print(n, end=" ")

def printRevNum(n):
    if n<1 : return
    print(n, end=" ")
    printRevNum(n-1)

printNum(10)
print()

printRevNum(10)
print()