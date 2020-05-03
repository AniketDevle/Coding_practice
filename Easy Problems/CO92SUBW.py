"""
The problem is similar to fibonacci sequence

approach:

1. find the first number in fibonacci sequence which is bigger than X
2. add the minimum of the distance between X and (station i and station I-1)

"""
testcase = int(input())
for z in range(testcase):
    X = int(input())
    li = [0]
    nums = 1

    while li[-1] < X:
        li.append(li[nums-1] + nums)
        nums = nums + 1


    if (li[-1] == X):
        print((nums-1))
        continue

    if (li[-1]-X > X-li[-2]):
        print((nums -2 + X - li[-2]))
        
    
    if (li[-1]-X < X-li[-2]):
        print((nums - 1 + li[-1] - X))
        
    if (li[-1]-X == X-li[-2]):
        print(nums -2 + X - li[-2])
