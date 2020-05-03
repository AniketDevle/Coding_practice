testcase = int (input())
for z in range(testcase):
    N , K = [int(x) for x in input().split()]
    li = [int(x) for x in input().split()]
    total = sum(li)
    count  = 0
    for i in li:
        if (i+K)>(total-i):
            count += 1
    print(count)
