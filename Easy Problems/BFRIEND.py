"""
1.find best floor to change his clothes
2. total_time = time to reach from bobs floor to optimal floor  + time to  change  + time to reach alices floor

"""






testcases = int(input())
for z in range(testcases):
    Num_friends,Alice_floor,Bob_floor,Min_to_change = [int(d) for d in input().split()]
    friends_floor = [int(d) for d in input().split()]
    optimal_floor = sorted(friends_floor , key= lambda x : (abs(x-Alice_floor) + abs(x-Bob_floor)))[0]
    time_to_reach_optimal = abs(optimal_floor - Bob_floor)
    time_to_reach_alice = abs(optimal_floor - Alice_floor)
    total_time = time_to_reach_optimal + Min_to_change + time_to_reach_alice
    print(total_time)
