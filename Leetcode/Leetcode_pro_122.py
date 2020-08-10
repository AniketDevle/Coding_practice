prices = [ 3,2,6,5,0,3]


if (len(prices) < 2):
    print(0)
           
pc1 = prices[1]

for i in range(1 , len(prices)-1):
    if prices[i] >= prices[i-1] and prices[i+1] >= prices[i]:
        prices[i] = -1

if prices[0] > pc1 :
    prices[0] = -1

print(prices)

odds = []
evens = []

            

num = 0
for i in range(len(prices)):
    if (num % 2 == 0 and prices[i] != -1):
        evens.append(prices[i])
        num = num + 1
        continue 

    if (num % 2 == 1 and prices[i] != -1):
        odds.append(prices[i])
        num = num + 1
        continue

print(odds)
print (evens)

if (len(odds) != len(evens)):
    evens = evens[:-1]

ans = 0
for i in range(len(odds)):
    if (odds[i] > evens[i]):
        ans = ans + odds[i] - evens[i]

print(ans)
"""print(abs(evens-odds))
"""        
