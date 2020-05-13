import math
testcase = int(input())
for z in range(testcase):
    A,B,C = [int(d) for d in input().split()]
    sub  = abs(A+C-2*B)
    if (sub % 2 == 0):
        print(int(sub/2))
    else:
        print(int((sub+1)/2))
