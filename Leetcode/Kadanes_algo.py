"""
Finding the maximum sum subarray problem

Bruteforce approach : O(N^3) or O(N^2) depending on approach
Kadane's algorithm : O(N)

Sum_array = [1 , 3 , 1 , 4 , 8  , 2]

"""

Arr = [1 , 2 , -2 , 3 , 4 , -6]

Sum_array = []
Sum_array.append(Arr[0])

for i in range(1,len(Arr)):
    if Sum_array[-1] + Arr[i] > Arr[i]:
        Sum_array.append(Sum_array[-1] + Arr[i])
    else:
        Sum_array.append(Arr[i])
        
print(max(Sum_array))    
