"""
Add both string A+B
add all the chaaracters in a dictionary

add ci
all c to dictionary 

"""


def check_this(S , C):
    for i in C:
        if C[i]>S[i]:
            return False
    return True    
    
testcase = int(input())
for _ in range(testcase):
    a,b = [i for i in input().split()]
    s = a+b
    num = int(input())
    S = {}
    C = {}
    for z in range(num):
        c = input()
        for i in c:
            if i not in C:
                C[i] = 0
            C[i] = C[i]+1    
    for i in s:
        if i not in S:
            S[i] = 0
        S[i] = S[i]+1


    try :
        if (check_this(S,C)):
            print("YES")
        else:
            print("NO")
    except:
        print("NO")
        
