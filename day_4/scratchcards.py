# Card example: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card number: winning numbers | your numbers
# Rules: First match is worth 1 point, points doubled each match after first

from collections import defaultdict

cards = []
copies = defaultdict(lambda:1)
total_points = 0
total_cards = 0
with open("day_4/input.txt", 'r') as f:
  cards = [line.strip() for line in f]

for card in cards:
  points = 0
  matches = 0

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
      matches += 1

  # For all matches of this card, loop through the next x cards and add the amount of the current card to that cards count
  # Ex: Card 2 has 1 copy, and 10 matches, add 2 copies to each of the next ten cards
  if matches > 0:
    for number in range(1, matches+1):
      copies[card_id + number] += copies[card_id]

  total_points += points
  total_cards += copies[card_id]

  print(f'Points this card: {points}')
  print(f'Total matches this card: {matches}')
  print(f'Total cards so far: {total_cards}')

  print('\n')

print(f'Total points: {total_points}')
print(f'Total cards: {total_cards}')
# print(sum(copies.values()))
# print(copies)