"""
find the max that profit in last N-i days
if profit is more in chefbad shift else dont shif

Crr = profit_after_this_day_in_chefland
drr = profit_after_this_day_in_chefbad

We get Crr[i] by add all elements of arr from i-> Num
ie crr[0] = arr[0] + arr[1]....+arr[n-1]

Similarly find Drr

"""

"""
arr = [10 , 12 , 13 , 15]
brr = [20  , 2 , 13 , 15]

crr = [50 , 40 , 28 , 15]
drr = [50 , 30 , 28 , 15]

ans after iteration 1: 50


if
arr = [10 ,  1]
brr = [1  , 10]

crr = [11 ,  1]
drr = [11 , 10]

ans after iteration 1: 10
ans after iteration 2 : 20

"""

testcase = int(input())
for _ in range(testcase):

    num = int(input())
    arr = [int(d) for d in input().split()]
    brr = [int(d) for d in input().split()]

    crr = [arr[num-1]]
    drr = [brr[num-1]]

    for i in range(0,num-1):
        crr.append(crr[i] + arr[num-2-i])
        drr.append(drr[i] + brr[num-2-i])

    
    crr = crr[::-1]
    drr = drr[::-1]
    ans = 0
    for i in range(num):
        if(arr[i]>=brr[i]):
            ans = ans + arr[i]
        else:
            
            if(drr[i]>=crr[i]):
                ans = ans + drr[i]
                break
            else:
                ans =ans + arr[i]
    print(ans)    
