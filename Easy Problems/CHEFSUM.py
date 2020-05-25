"""
We need to understand how both duntion works

say N = 5
for counter = 1 => sum(arr[0]) + sum(arr[:])
for counter = 2 => sum(arr[:2]) + sum(arr[1:])

we need to understand that only he index element is added twice in the total of
both functions

so just find the index of minimum value of arr
"""
testcase = int(input())
for _ in range(testcase):
    Num = int(input())
    arr = [int(d) for d in input().split()]
    print(arr.index(min(arr))+1)
