"""
The customer is adequate if all the notes are required to make a purchase

say imput is

6 10
2 16 16 16 16 7 => 73 purchase(7 of 10 each)
                   if you throw 2 rs note=> purchase still possible

algo:
add all numbers
find mod = sum % X
check if all number are greater than mod

"""

def res(arr , num):
    for i in arr:
        if i <= num:
            return False
    return True

testcase = int(input())
for _ in range(testcase):
    N,X = [int(d) for d in input().split()]
    arr = [int(d) for d in input().split()]
    S = sum(arr)
    mod = S%X
    if(res(arr , mod)):
        print(S//X)
    else:
        print(-1)
