# Could be better, first iteration was O(n) list comprehension
# Second iteration has to loop through each line a second time to check dictionary entries. Also since word numbers overlap would be smarter to loop through from the right of the line as well, but keeping the last letter when a word was found prevents issues such as 'twone' counting as two, instead of one.

file = open("day_1/input.txt", "r")

words_to_numbers = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

total = 0

for line in file:
  print('Original line: ' + line.strip())
  nums = []
  sub = ''
  for letter in line:
    sub += letter
    if letter.isdigit():
      sub = ''
      nums.append(letter)
    else:
      for x in words_to_numbers.keys():
        if x in sub:
          nums.append(words_to_numbers[x])
          sub = sub[-1]
          break

  two_digit = str(nums[0]) + str(nums[-1])
  print('Two digit: ' + two_digit)
  total += int(two_digit)
  print(total)
  print('\n')

#   for letter in line:
#     pass

print(str(total))


  # numbers = [i for i in line if i.isdigit()]
  # print('Numbers: ' + str(numbers))
  # two_digit_num = int(str(numbers[0] + str(numbers[-1])))
  # print('Two digit num: ' + str(two_digit_num))
  # print('\n')
  # total += two_digit_num

# print('Total: ' + str(total))

# sample = 'wsixthreeqpzjpn195'

# nums = []
# sub = ''
# for letter in sample:
#   sub += letter
#   print(sub)
#   if letter.isdigit():
#     sub = ''
#     print(letter)
#     nums.append(letter)
#   else:
#     for x in words_to_numbers.keys():
#       if x in sub:
#         nums.append(words_to_numbers[x])
#         sub = ''
#         break
    # if sub in words_to_numbers.keys():
    #   nums.append(words_to_numbers[sub])
    #   sub = ''


# print(nums)

# print(str(total))
# print(words_to_numbers.keys())