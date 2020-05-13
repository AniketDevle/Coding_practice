"""
Reziba -> R
If rating greater than R go left
if rating less than R go right

always stay in limits of left_limit and right_limit
update left_limit and right_in each case


eg1 :
arr = [600 , 300 , 100 , 350 , 200]
iteration 1 : i = 600 => 600>0 and 600<10000000000 && 600>200=> right_limit = 600
iteration 2 : i = 300 => 300>0 and 300<600 && 300>200 => right_limit = 300
iteration 3 : i = 100 => 100>0 and 100<300 && 100<200 => left_limit = 100
iteration 4 : i = 350 => 350>100 but 350>300(right_limit) => return False
 
"""
"""
def check_if_valid(arr , N , R):
    left_limit = 0
    right_limit = 1000000000
    for i in arr:
        if i <= left_limit or i>= right_limit:
            return False

        if i<right_limit and i > R:
            right_limit = i

        if i>left_limit and i < R:
            left_limit = i
    return True       

testcase = int(input())
for z in range(testcase):
    N , R = [int(d) for d in input().split()]
    arr = [int(d) for d in input().split()]
    if(check_if_valid(arr, N , R)):
        print("YES")
    else:
        print("NO")

This solution was partially accepted         
"""

def check_if_valid(arr , N , R):
    left_limit = 0
    right_limit = 100000000000
    for i in range(N-1):
        if (i == 0):
            if (arr[i] > R):
                right_limit = arr[i]
            elif(arr[i] <R):
                left_limit = arr[i]
        else:
            if(arr[i]>left_limit and arr[i]<right_limit):
                if arr[i] > R:
                    right_limit = arr[i]
                elif arr[i]< R:
                    left_limit = arr[i]
            else:
                return False
    return True            
                
                  

testcase = int(input())
for z in range(testcase):
    N , R = [int(d) for d in input().split()]
    arr = [int(d) for d in input().split()]
    if(check_if_valid(arr, N , R)):
        print("YES")
    else:
        print("NO")
