players = ['Kobe Bryant', 'Michael Jordan', 'Dirk Nowitzki', 'LeBron James', 'Stephen Curry']
teams = ['LA Lakers', 'Chicago Bulls', 'Dallas Mavericks', 'Cleveland Cavaliers', 'GS Warriors']

# for index, player in enumerate(players, start=0):
#     franchise = teams[index]
#     print(f'{player} is in {franchise}')

#
for player, franchise in zip(players, teams):
    print(f'{player} is in {franchise}')