"""


"""
"""
def change (arr ,value , L, num):
    for  i in range(L,num):
        arr[i] = value
    return arr    
    
    
testcase = int(input())

for _ in range(testcase):

    num = int(input())
    arr = [int(d) for d in input().split()]

    counter = num-1
    mini = arr[num-1]
    while(counter>=0):
        if( arr[counter] <= mini):
            mini = arr[counter]
            arr = change(arr,arr[counter] , counter , num)
        counter = counter-1    
    print(sum(arr))        
"""
"""
The above is a O(N^2) solution so it worked partially
Now going for O(N)

"""

testcase = int(input())

for _ in range(testcase):

    num = int(input())
    arr = [int(d) for d in input().split()]

    ans = arr[0]
    mini = arr[0]
    for i in range(1,num):
        if(arr[i]<mini):
            mini = arr[i]
            ans = ans + mini
        else:
            ans = ans + mini

    print(ans)
     
