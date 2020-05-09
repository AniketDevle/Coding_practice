"""
def is_overlucky(num):
    num = str(num)
    for i in num:
        if i in ['4','7']:
            return True
    return False

testcase = int(input())

for z in range(testcase):
    num = int(input())
    count = 0
    for i in range(1 , num+1):
        if(num% i == 0):
            if (is_overlucky(i)):
                count = count + 1
    print(count)           
        
"""

"""
The above  brute force approach excedes the time limit

Aniket you made such a simple mistake dude you dont neeed to check all elements
checkig till root of n will work wine as well

It will reudce the complexity from O(n) to O(n**0.5)
"""
 
def is_overlucky(num):
    num = str(num)
    for i in num:
        if i in ['4','7']:
            return True
    return False

testcase = int(input())

for z in range(testcase):
    num = int(input())
    count = 0
    for i in range(1 , int(num**0.5)+1):
        if(num% i == 0):
            if (is_overlucky(i)):
                count = count + 1
            complement = num / i      ## for num = 28 -> num**0.5 = 5 -> i = 4 then complement = 7
            if complement != i:
                if (is_overlucky(complement)):
                    count = count + 1
    print(count)           
