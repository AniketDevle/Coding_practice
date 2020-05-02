testcase = int(input())

for z in range(testcase):
    num = int(input())
    li = [int(i) for i in input().split()]
    count = 0
    li = sorted(li)
    for i in range(len(li)):
        if li[i] <= i:
            count +=1
        else:
            break
    print(count)        
