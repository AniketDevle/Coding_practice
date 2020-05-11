"""
Input;
T
G
I N Q -->> I and Q =>{'Head': 1 , 'Tail' = 2}

after
HHHHH -> THTHT      &&    TTTTT -> HTHTH
HHHH -> HTHT        &&    TTTT -> THTH
HHH -> THT          &&     TTT -> HTH 


as there can be only two possible values of I and Q

if I == Q   ie(start with head and final count of head is asked)
{
    if n is even: print N/2
    else : print (N-1)/2
}
else
{
    if n is even: print(n/2)
    else : print((N+1)/2)
}

"""

testcase = int(input())
for z in range(testcase):
    G = int(input())
    for y in range(G):
        I , N , Q = [int(d) for d in  input().split()]
        if I == Q:
            if N%2 == 0:
                print(int(N/2))
            else:
                print(int((N-1)/2))
        else:
            if N%2 == 0:
                print(int(N/2))
            else:
                print(int((N+1)/2))
                
