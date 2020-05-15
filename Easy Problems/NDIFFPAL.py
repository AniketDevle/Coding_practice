"""
just using a b c

using a and b will not work cause
N = 3-> a b a (palindrome)

usinf a b c
n=3->  a b c
n = 4-> a b c a
n = 5-> a b c a b
n = 6 -> a b c a b c
n = 7 -> a b c a b c a
"""

testcase = int(input())

for z in range(testcase):
    num = int(input())
    s = ""
    D = {0 : 'a' , 1: 'b' , 2: 'c'}
    for i in range(num):
        s = s + D[i%3]
    print(s)    
