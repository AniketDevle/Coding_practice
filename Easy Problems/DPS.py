"""

This is a good problem
Moves allowed:
1. permute the string
2. change one character

As we are allowed to make any permutation we can use dictionary to save the
occurrance of each character in the sequence

If we have more than 3 chaaracters with odd value then we cant make it a palindrome
in one swap

3 characters with odd:

XXXCCCDDD-> {'X':3 , 'C':3 , 'D':3} -> change one X to D -> XDDCCCDDX : possible

4 character with odd:
ABCDFF-> {'A': 1 , 'B': 1 , 'D': 1 , 'C': 1 , 'F': 2}

Change one A to D -> (DBCDFF)->(DFCBFD): impossible

"""
"""
Solved it in the first attempt good one aniket 

"""
testcase = int(input())
for z in range(testcase):
    S = input()
    char_occur = {}
    for i in S:
        if i not in char_occur:
            char_occur[i] = 0
        char_occur[i] = char_occur[i] + 1

    arr_odd_occur = [key for key in char_occur if char_occur[key]%2 == 1]
    length_arr = len(arr_odd_occur)
    if(length_arr > 3 or length_arr == 0 ):
        print("!DPS")
    else:
        print("DPS")
            
