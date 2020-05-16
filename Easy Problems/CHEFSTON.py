

def result (arr , brr , K , n):
    ans = 0
    for i in range(n):
        ans = max(ans , (K//arr[i])*brr[i])
    return ans

testcase =int(input())
for _ in range(testcase):
    N , K = [int(d) for d in input().split()]
    arr = [int(d) for d in input().split()]
    brr = [int(d) for d in input().split()]
    print(result(arr , brr, K, N))
