"""
testcase = int(input())
for _ in range(testcase):

    Num = int(input())
    arr = [int(d) for d in input().split()]

    S = [max(arr[i+1:])-arr[i] for i in range(Num-1)]
    ans = max(S)

    if ans <= 0:
        print("UNFIT")
    else:
        print(ans)

O(n^2) => dosent work
"""

"""
This is the O(n) approach that is mentioned in the editorial
Aniket was too frustrated to think hard today

Aniket Do remember this problem

here we can see that ans is updated only if the difference between current value
and the minimum value yet is greater than the ans itself

eg:
arr = [3  7  1  4  2  4]
before iteration => minn = 100000000 and ans  = -1
iteration 1 => curr = 3 => curr - min => -999999997 => ans = -1 => min = 3
iteration 2 => curr = 7 => curr - min => 4          => ans =  4 => min = 3
iteration 3 => curr = 1 => curr - min => -2         => ans =  4 => min = 1
iteration 4 => curr = 4 => curr - min => 3          => ans =  4 => min = 1
iteration 5 => curr = 2 => curr - min => 1          => ans =  4 => min = 1
iteration 6 => curr = 4 => curr - min => 3          => ans =  4 => min = 1
"""

testcase = int(input())
for _ in range(testcase):

    Num = int(input())
    arr = [int(d) for d in input().split()]

    minn = 100000000
    ans = -1
    for cur in arr:
        ans = max(ans , cur-minn)
        minn = min(minn , cur)

    if (ans<=0):
        print("UNFIT")
    else:
        print(ans)
