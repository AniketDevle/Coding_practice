"""
This is a gcd problem 
"""
import math
testcase = int(input())
for _ in range(testcase):
    num = int(input())
    arr = [int(s) for s in input().split()]
    check = []
    for i in range(len(arr)):
        check.append(math.gcd(arr[i] , arr[i-1]))
    print(min(check) * num)    
