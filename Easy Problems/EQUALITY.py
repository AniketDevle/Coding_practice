"""
There are N linear equations so add them all up

(n-1)x1 + (n-1)x2.......(n-1)Xn = sum(all a's)

x1 = (sum(all a's) - a[1]*(n-1))/(n-1)

"""
import math

testcase = int(input())
for z in range(testcase):
    num = int(input())
    a = [int(d) for d in input().split()]
    s = sum(a)
    stri = ""
    for i in  range(num):
       stri = stri + str(math.floor((s-(a[i]*(num-1)))/(num-1))) + " "
    print(stri)   
