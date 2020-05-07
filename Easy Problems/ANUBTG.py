def calculate(arr):
    if len(arr)<2:
        return arr[0]
    else:
        return arr[0]+arr[1]

testcase = int(input())
for z in range (testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    arr = sorted(arr , reverse = True)
    count = 0
    i = 0
    while (i+4 < len(arr)):
        count = count + calculate(arr[i:i+4])
        i = i+4
    count  = count + calculate(arr[i:])
    print(count)
        
        
