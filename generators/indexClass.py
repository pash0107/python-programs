import random

colors = ('Red', 'Blue', 'White', 'Green', 'Pink', 'Yellow')
numInput = int(input('Enter Num of Players: '))

# player = {}

class Players:

    def __init__(self):
        self.player = {}
        for i in range(numInput):
            player_name = input('Enter Player Name: ')
            player_chip = int(input('Enter Player Chip: '))
            self.player[player_name] = player_chip
        return self.player
    
# for i in range(numInput):
#     player_name = input('Enter Player Name: ')
#     player_chip = int(input('Enter Player Chip: '))
#     player[player_name] = player_chip
player = Players()
print(player)