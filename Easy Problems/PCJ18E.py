"""
Trying the largest increasing  solution

if increasing add 1 to previous else append one 

          arr =   4 1 4 3
    increasing=   1 1 2 1

ans = len(arr) - max(increasing)

4 1 4 3 -> 1 4 3 4 -> 1 3 4 4 (2 steps)

"""

"""testcase = int (input())

for z in range(testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    increasing = [1]
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            increasing.append(increasing[-1] + 1)
        else:
            increasing.append(1)
    print(num - max(increasing))       
"""

"""
The other approach that I thought of was comparing the elements of
sorted and unsorted array...But that wont give us correct answer because if the
elements are in order 4 1 2 3 the misplaced elements are 4 but the steps required
are only one 
"""

"""
Infact the solution in the editorial is the mix of both the solutions
find the largest increasing subseuence in sorted and unsorted
"""

"""
arr       =  2 1 4 2
sorted    =  1 2 2 4

j = 0
run on sorted and if arr[i] = sorted[j] then j = j+1


after iteration 0 : i = 1 j = 0 cause (arr[0] != sorted[0])   
after iteration 1 : i = 2 j = 1 cause (arr[1] == sorted[0])    
after iteration 2 : i = 3 j = 1 cause (arr[2] != sorted[1]) 
after iteration 3 : i = 4 j = 2 cause (arr[3] == sorted[1])

so possible moves => 2 1 4 2 -> 1 4 2 2 -> 1 2 2 4 
"""

testcase = int (input())
for z in range(testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    brr = sorted(arr)
    j = 0
    for i in range(num):
        if arr[i] == brr[j]:
            j = j + 1
    print(num - j)        
