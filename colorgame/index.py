import random

colors = ('Red', 'Blue', 'White', 'Green', 'Pink', 'Yellow')
numInput = int(input('Enter Num of Players: '))

player = {}

for i in range(numInput):
    player_name = input('Enter Player Name: ')
    player_chip = int(input('Enter Player Chip: \n'))
    player[player_name] = player_chip

print(player)