"""
Euclidian method for finding gcd


def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x

say x = 60 y = 48
after iteration 1: x, y = 48 , 12
after iteration 2: x , y = 12 , 0

say x = 2 y = 5
after iteration 1 : x,y = 5 , 2
after iteration 2 : x,y = 2 , 1
after iteration 3 : x,y = 1 , 0

"""






import math 
testcases = int(input())
for z in range(testcases):
    num = int(input())
    arr = [int(d) for d in input().split()]
    l = arr[0]
    for i in range(1,num):
        l = math.gcd(l , arr[i])
    if (l==1):
        print(num)
    else:
        print(-1)
