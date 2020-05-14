"""
find the index of max and then print(max + index)

say             W = [ 1 , 2 , 3 , 4]
    minimum_speed = [ 7 , 6 , 5 , 4]

print(7)


if
            W =  [ 4, 4, 4, 4]
minimum_speed =  [7 , 6 , 5 ,4]


so search for the last occurance of the max value and then print(max + last_index_of_max)

"""
"""
testcase= int(input())
for _ in range(testcase):

    num = int(input())
    arr = [int(d) for d in input().split()]
    maxim = 0
    max_index = -1
    for i in range(num):
        if(arr[i] >= maxim):
            maxim = arr[i]
            max_index = i
    print(maxim + max_index)            
    
"""

"""
The above solution will not work for the cases 1 2 1 1 1

expected answer 5
your answer 3

add value + index then find max
"""

testcase= int(input())
for _ in range(testcase):

    num = int(input())
    arr = [int(d) for d in input().split()]
    arr2 = [arr[i] + i for i in range(num)]
    print(max(arr2))            
