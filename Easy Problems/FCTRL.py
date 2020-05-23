testcase = int(input())
for _ in range(testcase):

    num = int(input())

    k = num
    count = 0
    while(k>=5):
        count = count + 1
        k = k/5

    ans = 0
    for i in range(1,count+1):
        ans = ans + num//(5**i)

    print(ans)        
