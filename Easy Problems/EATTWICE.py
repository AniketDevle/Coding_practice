"""
Bundle tastiness and Days in a tuple
sort them in reverse order

iterate through the sorted array and then
"""
testcase = int(input())
for _ in range(testcase):
    N , M = [int(s) for s in input().split()]
    arr = []
    for z in range(N):
        d , v = [int(s) for s in input().split()]
        arr.append((v,d))
    arr = sorted(arr , reverse = True)
    dish1_taste = arr[0][0]
    dish2_taste = 0
    for i in range(1,N):
        if (arr[i][1] != arr[i-1][1]):
            dish2_taste = arr[i][0]
            break
    print(dish1_taste + dish2_taste)        
