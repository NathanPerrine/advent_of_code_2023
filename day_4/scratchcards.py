# Card example: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card number: winning numbers | your numbers
# Rules: First match is worth 1 point, points doubled each match after first

cards = []
total_points = 0
with open("day_4/input.txt", 'r') as f:
  cards = [line.strip() for line in f]

# print(cards)
for card in cards:
  points = 0

  print(card)
  card_id = int(card[:card.index(':')].split(' ')[-1].strip())
  print(f'Card id: {card_id}')
  numbers = card[card.index(':')+1:]
  numbers = numbers.split('|')
  print(numbers)
  winning_numbers = set(numbers[0].strip().split(' '))
  player_numbers = numbers[1].strip().split(' ')

  print(f'Winning numbers: {winning_numbers}')
  print(f'Player numbers: {player_numbers}')

  for number in player_numbers:
    if number in winning_numbers and number != '':
      if points == 0:
        points += 1
      else:
        points *= 2

  total_points += points
  print(f'Points this card: {points}')

  print('\n')
print(total_points)