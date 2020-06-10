testcase  = int(input())
for _ in range(testcase):

    N , K = [ int(d) for d in input().split()]
    arr = [ int(d) for d in input().split()]

    ans = 0
    for i in arr:
        if i > K :
            ans  = ans + i - K

    print(ans)            
