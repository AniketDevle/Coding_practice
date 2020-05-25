"""

"""
"""
N , K  = [int(s) for s in input().split()]
arr = [int(s) for s in input().split()]

while(K>0):
    M = max(arr)
    arr = [M - i for i in arr]
    K = K -1

S = ""
for i in arr:
    S = S+ str(i) + " "
print(S)

I knew this was going to give a TLE

"""    
"""
I think i may have got the solution this time around

say N = 3 and K = 3

                    arr =  1   100  3
after iteration 1:  arr =  99  0    97
after iteration 2:  arr =  0   99   2
after iteration 3:  arr =  99  0    97
after iteration 4:  arr =  0   99   2
after iteration 5:  arr =  99  0    97



"""

"""
Did I just get a TLE for O(n) solution .....I dont know what the fuck is happening
Maybe I need to sleep now 
"""

N , K  = [int(s) for s in input().split()]
arr = [int(s) for s in input().split()]
    
if K ==0:
    s = ""
    for i in arr:
        s = s + str(i)+" "
    print(s)
else:
    brr = [max(arr)-i for i in arr]
    
    if K>1:
        crr = [max(brr)-i for i in brr]
    
    if (K%2 == 1):
        s = ""
        for i in brr:
            s = s + str(i) +" "
        print(s)
    else:
        s = ""
        for i in crr:
            s = s + str(i)+" "
        print(s)
