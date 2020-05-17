"""
sort in reverse order
add elements where index in even
"""
testcase = int(input())
for _ in range(testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    arr = sorted(arr , reverse = True)
    count = 0
    for i in range(num):
        if(i%2 == 0):
            count = count + arr[i]
        
    print(count)
