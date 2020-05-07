"""
The  only thing that came to mind is kadanes algorithm

"""


num = int(input())
arr = [int (d) for d in input().split()]
count = []
if arr[0] == 0:
    count.append(0)
else:
    count.append(1)
for i in range( 1 , len(arr)):
    if arr[i] == 0:
        count.append(0)
    else:
        count.append(count[i-1] + 1)

print (max(count))        
        
