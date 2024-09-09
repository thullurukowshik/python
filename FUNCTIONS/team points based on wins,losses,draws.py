def calculate_league_points(wins, draws, losses):
    # Complete this function
    sum = 0
    wins = wins * 4
    draws = draws *2
    losses = losses * -1
    sum = sum + wins + draws + losses
    print(sum)

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
calculate_league_points(wins,draws,losses)
