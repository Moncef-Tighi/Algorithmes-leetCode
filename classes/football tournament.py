"""Four football teams face each other in a tournament and you must determine the final classification.
 Depending on the match result, a team gets a certain amount of points:

A win is worth 3 points.
A draw is worth 1 point.
A defeat is worth 0 points.
Each team faces another once, for a total of six played games. For each game the result is provided with the following notation:

"Team X - X Team"
(with X being the number of goals scored by both teams)

"A 0 - 1 B" ➞ B wins and gets 3 points, A lose and gets 0 points
"C 2 - 2 D" ➞ It's a draw, both C and D get 1 point
At the end of the tournament, points are counted for each team.
 If two or more teams have the same number of points, two further criteria are applied to determine who gets the best placement, in the order:

The greater number of goals scored.
The greater goals difference (goals scored minus goals conceded).
Given a list lst containing strings with the results of the six played games, you have to implement a function that returns a list containing four lists, one for each team, in the following notation:

[Team, PT, GS, GD]
Team: A string, name of the team.
PT: An integer, points obtained.
GS: An integer, the sum of scored goals.
GD: An integer, scored goals minus conceded goals (can be negative).
The main list containing the teams'
 info must be ordered in such a way as to present the correct placement of each team
  as if it were a summary of the final classification and performance.

"""