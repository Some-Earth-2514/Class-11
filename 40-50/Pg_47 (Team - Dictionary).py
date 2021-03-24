"""
Repeatedly ask the user to enter a team name and know how many games the team has won and how many they lost.
Store this info in a dictionary where the keys are the team names and the lists of form [win, losses].

i) Using the dictionaries created above allow the user to enter a team name and print out the team's winning percentage.
ii) Using the dictionary, create a list whose entries are the number of wins of each team.
iii) Using the dictionary, create a list of all those teams that have winning records
"""
team_input = int(input("Enter the total number of teams : "))
score = {}
for i in range(0, team_input):
    team_name = input("Enter team name: ")
    team_wins = int(input(" Enter number of wins: "))
    team_losses = int(input(" Enter number of losses: "))
    score[team_name] = [team_wins, team_losses]

# i)
team_name = input("Enter team name to calculate winning percentage ")
print("Winning percentage of ", team_name, "is", (score[team_name][0] / sum(score[team_name])) * 100)

# ii)
wins_team = [a[0] for a in score.values()]
print(wins_team)

# iii)
win_record = []
for i in score:
    if score[i][0] > 0:
        win_record.append(i)
        print(win_record)
