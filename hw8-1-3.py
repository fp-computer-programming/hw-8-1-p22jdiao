# Author: JD 12/09/2021

"""
In the group stage of the FIFA World Cup, a team earns 3 points for a win, 1 point for a tie,
 and no points for a loss. Write a program that propmts the user to input the number of wins 
 and ties for 2 teams, calculates the total points each team earned in the group stage, and 
 displays a statement stating which team finished with more points during the group stage. 
"""
 
def win_determiner(team_1_win, team_1_tie, team_2_win, team_2_tie):
     team_1_score = team_1_win * 3 + team_1_tie
     team_2_score = team_2_win * 3 + team_2_tie
     
     if team_1_score > team_2_score:
         return "Team 1"
     elif team_2_score > team_1_score:
         return "Team 2"
     else:
         return "neither of them, it is a tie"
     
t1w = int(input("The number of wins of team 1: "))
t1t = int(input("The number of ties of team 1: "))

t2w = int(input("The number of wins of team 2: "))
t2t = int(input("The number of ties of team 2: "))

winner = win_determiner(t1w, t1t, t2w, t2t)

print("The winner is", winner+".")

#test
print(win_determiner(0, 0, 0, 0) == "neither of them, it is a tie")
print(win_determiner(10, 0, 0, 10) == "Team 1")
print(win_determiner(5, 10, 10, 5) == "Team 2")