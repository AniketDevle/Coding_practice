
testcase = int(input())
for z in range(testcase):

    num = int(input())
    costs = [int(d) for d in input().split()]
    left_rate = -1
    right_rate = 1

    initial_cost = costs[0]
    month_gain = costs[1:][::-1]
    mid_found = False

    while(abs(left_rate-right_rate)>0.00000001):

        mid = (left_rate+right_rate)/2
        Error = - (initial_cost * ((1+mid)**num))
        for i in range(len(month_gain)):
            Error = Error + month_gain[i]* ((1+mid)**i)

        if Error > 0:
            left_rate = mid
        elif Error == 0:
            print("{:.7f}".format(mid))
            mid_found = True
            break
        else:
            right_rate = mid
            
    if mid_found == False:
        print(round(left_rate , 8))       
                   
