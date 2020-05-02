testcase = int(input())

for z in range(testcase):
    nums = [int(i) for i in input().split()]
    count = 0
    for x in range(nums[0] , nums[1]+1):
        if x%10 in [2,3,9]:
            count += 1
    print(count)        
            
    
