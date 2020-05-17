"""
find sum of both arrays individually
add(floor of sum / 2) of both arrays 
"""

testcase = int(input())
for _ in range(testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    brr = [int(d) for d in input().split()]
    NO_a = sum([1 for i in arr if i% 2 == 1])
    NO_b = sum([1 for i in brr if i% 2 == 1])

    s = sum(arr)+sum(brr)
    print((s-abs(NO_a -NO_b))//2)
