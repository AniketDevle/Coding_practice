"""
Here the trick is to understand the number of zeros has got no role whatsoever
to the final answer

eg 101 = > ans = 3    and for 10001 => ans = 3

find the number of 1 in the string
print(n*(n+1))/2
"""
testcase = int(input())
for _ in range(testcase):

    Num = int(input())

    S = input()
    count  = 0
    for i in S:
        if i =="1":
            count = count + 1
    print((count*(count+1))//2)
            
        
