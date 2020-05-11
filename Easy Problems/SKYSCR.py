"""

This probleem looks awfully simple cause I am using python
If I were using language like java i would have to use big integer to subtract both values


"""

testcase = int(input())
for z in range (testcase):
    N,M = [int(d) for d in input().split()]
    print(abs(N-M))
