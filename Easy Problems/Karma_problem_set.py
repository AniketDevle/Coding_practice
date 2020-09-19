"""
Say the property is whether the word has only alphabets or only numbers
we are trying to determine the first position on which their properties dont
match

This will run in O(ln(n)) run time but this code will give you an error if your
software dosen't generate the  words such that there are only two properties

if there are multiple properties and they are scrambled then this won't work
eg:

S = "AAA AAD GHAH AJNJN 123 123656 898 !@#$%  abc assd"
the properties over here are : Uppercase , lowercase , digits , symbols and we
can never be sure that there wasnt a property change in the middle of the string
so that type of code will have runtime complexity of O(N)

The below code prints an array of strings (with different properties)

Following are the assumption under which this code works fine:
1. Whole word will has same property as first character of word
2. There are only two properties (Alphabets and digits)
3. The change from Alphabet to Digit will only happen once 
"""

S = "AAA AAA ABA ABAAS ATANN KJJOOJ AHGGHG BHBHJB JNJN 123 123 458 48865 45"

Digits = "0123456789"
Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr = S.split()
left = 0
right = len(arr)-1
ans = -1
while(left<right):
    mid = (left+right)//2

    current = arr[mid]
    previous = arr[mid-1]
    if current[0] in Digits and previous[0] in Alphabets:
        ans = mid
        break
    elif current[0] in Alphabets:
        left = mid
    elif current[0] in Digits:
        right = mid

alpha = " ".join(arr[:ans])
digits =" ".join(arr[ans:])

answer = [alpha , digits]
print(answer)
        
