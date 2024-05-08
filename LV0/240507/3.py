# 캐릭터의 좌표

def solution(keyinput, board):
  x_lim, y_lim = board[0]//2, board[1]//2
  keyboard = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, 1),
    "down": (0, -1),
  }
  x,y = 0,0
  for move in keyinput:
    dx,dy = keyboard[move]
    if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
        continue
    else:
        x,y = x+dx,y+dy
        print(x, y)
  return [x, y]
