
N , M, P = [int(d) for d in input().split()]
arr = [int(d) for d in input().split()]

brr = sorted(arr)

for i in range(P):
    a , b = [int(d) for d in input().split()]
    if a>b:
        a ,b = b , a
    a = a-1
    b = b-1
    print(a)
    print(b)
    ind_a = brr.index(arr[a])
    ind_b = brr.index(arr[b])
    check = True
    for j in range(ind_a + 1 , ind_b+1):
        if (brr[j] - brr[j-1] > M):
            check = False
            break
    if (check):
        print("Yes")
    else:
        print("No")
            
            
        
