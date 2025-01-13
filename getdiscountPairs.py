n = 3
x = 5
price = [1,6,11]
def getdiscountPairs(n,x,price):
    pairs = 0
    pairs_map = {}
    for i in range(n):
        
        pairs_map[price[i]] = pairs_map.get(price[i],0) + 1
    return pairs
print(getdiscountPairs(n,x,price))
    

