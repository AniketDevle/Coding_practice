"""
table [team_name] = [Points , goals_diference]

result = [Team_name1 , goals_scored1 , vs. , goals_scored2 , Team_name2]
"""



testcase = int(input())
for z in  range(testcase):
    table={}
    for k in range(12):
        team_name1 , team_goals1 , vs , team_goals2 , team_name2 = input().split()
        if team_name1 not in table:
            table[team_name1] = [0 , 0]

        if team_name2 not in table:
            table[team_name2] = [0 , 0]

        team_goals1 = int(team_goals1)
        team_goals2 = int(team_goals2)

        if (team_goals1>team_goals2):
            table[team_name1][0] = table[team_name1][0] + 3
            table[team_name1][1] = table[team_name1][1] + team_goals1 - team_goals2
            table[team_name2][1] = table[team_name2][1] + team_goals2 - team_goals1

        elif (team_goals1 == team_goals2):
            table[team_name1][0] = table[team_name1][0] + 1
            table[team_name2][0] = table[team_name2][0] + 1

        else:
            table[team_name2][0] = table[team_name2][0] + 3
            table[team_name1][1] = table[team_name1][1] + team_goals1 - team_goals2
            table[team_name2][1] = table[team_name2][1] + team_goals2 - team_goals1

    final_result = list(sorted(table.keys() , key = lambda x : (table[x][0] , table[x][1]) , reverse = True))
    print(final_result[0] + " " + final_result[1])

            
            
            
        
