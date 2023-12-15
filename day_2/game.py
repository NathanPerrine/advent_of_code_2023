file = open("day_2/input.txt", "r")

limit = {
  'red': 12,
  'green': 13,
  'blue': 14
}

id_total = 0
power_total = 0

for line in file:
  colors = {
    'red': 0,
    'blue': 0,
    'green': 0
  }

  print(line.strip())

  # games = line.split(';')
  # print(games)

  game = line.split(':')

  # Get the game id as an int
  # Split the game on ":" to separate the game id and the sets, break the id down to the number
  game_id = int(game.pop(0).split(' ')[-1])
  print(f'game id: {game_id}')


  # Get the sets of the game
  sets = game[0].split(';')

  # print(sets)
  possible = True

  for set in sets:
    set = set.strip()
    # print(set)
    pieces = set.split(',')

    for piece in pieces:
      piece = piece.strip()
      # print(piece)
      value, color = piece.split(' ')
      value = int(value)
      print(value, color)

      if value > colors[color]:
        colors[color] = value

      # For star 1, if we exceed the set limit for a color we don't want to continue or add the game to the total
      # if value > limit[color]:
      #   possible = False
      #   break

  # if possible:
  #   id_total += game_id
  # print(f'id total: {id_total}')

  game_power = 1
  for v in colors.values():
    # print(v)
    game_power *= v

  print(colors)
  print(game_power)
  power_total += game_power


  print('\n')
# print(id_total)
print(power_total)


# line = 'Game 87: 30 red, 10 green, 3 blue; 13 blue, 6 red, 2 green; 1 green, 2 red, 10 blue'
# colors = {
#   'red': 0,
#   'blue': 0,
#   'green': 0
# }
# limit = {
#   'red': 12,
#   'green': 13,
#   'blue': 14
# }

# idTotal = 0

# game = line.split(':')
# game_id = game.pop(0)
# sets = game[0].split(';')
# print('game id: ' + game_id)
# print(sets)
# for set in sets:
#   print('game: ' + set)
#   cubes = set.split(',')
#   for cube in cubes:
#     cube = cube.strip()

#     value, color = cube.split(" ")
#     value = int(value)
#     print(value, color)
#     colors[color] = int(value)

#     if value > limit[color]:
#       print(f'There are {value} {color}s in this set, which is higher than the limit of {limit[color]}')
#       break
#     idTotal += int(game_id.split(' ')[-1])
#     # print(game_id.split(' ')[-1])


# print(colors)
# print(idTotal)