def scanNumber(i, j):
  # Return 0 if out of bounds or number already seen
  if i > len(board) or j > len(board[0]) or i < 0 or j < 0 or (i,j) in seenAlready: return 0

  # Return 0 if number is not found
  if not board[i][j].isnumeric(): return 0

  digits = board[i][j]
  seenAlready.append((i,j))

  # Scan left for full number
  left = j-1
  while left >= 0:
    # Number not found, stop looking further left
    if not board[i][left].isnumeric(): break
    digits = board[i][left] + digits
    seenAlready.append((i, left))
    left -= 1

  # Scan right for full number
  right = j+1
  while right < len(board[0]):
    # Number not found, stop looking further right
    if not board[i][right].isnumeric(): break
    digits = digits + board[i][right]
    seenAlready.append((i, right))
    right += 1

  return int(digits)


# i = line number, j = character number
def getAdjacentNumbers(i, j):
  # Up and left 1
  nw = scanNumber(i-1, j-1)
  # Up 1
  n = scanNumber(i-1, j)
  # Up 1, right 1
  ne = scanNumber(i-1, j+1)
  # Left 1
  w = scanNumber(i, j-1)
  # Right 1
  e = scanNumber(i, j+1)
  # Down 1, left 1
  sw = scanNumber(i+1, j-1)
  # Down 1
  s = scanNumber(i+1, j)
  # Down 1, right 1
  se = scanNumber(i+1, j+1)

  # find any adjacent numbers
  adj = [nw,n,ne,w,e,sw,s,se]
  # If numbers found, will be > 0
  adj = [x for x in adj if x > 0]
  # If len of adj == 2, gear was found (numbers next to 2 gears), return the product of those numbers, else 0
  return adj[0]*adj[1] if len(adj)==2 else 0


  # return nw+n+ne+w+e+sw+s+se

board = []
seenAlready = []
total = 0
with open("day_3/input.txt", 'r') as f: board = [[c for c in line.rstrip()] for line in f]
# index, line
for i, line in enumerate(board):
  for j, c in enumerate(line):
    # Check if character is a symbol or not
    # if not c.isnumeric() and c!='.':
    if c == '*':
      # Symbol found
      total += getAdjacentNumbers(i, j)
print(total)