competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]]
results = [0, 0, 1]

"""
First Solution
"""


def tournamentWinner(competitions, results):
    teamPoints = {}
    currentWinner = '', 0
    for competition, result in zip(competitions, results):
        winner = competition[not result]
        loser = competition[result]

        if winner not in teamPoints:
            teamPoints[winner] = 0
        teamPoints[winner] += 3

        if teamPoints[winner] > currentWinner[1]:
            currentWinner = winner, teamPoints[winner]

    return currentWinner[0]


print(tournamentWinner(competitions, results))
