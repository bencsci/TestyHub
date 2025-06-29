# Get the knights possible attacks and go through each attacks
# keep track of the number of moves
# if the knight lands on the pawn then return the minimum count
# use bfs to traverse through the attacks

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  rows = cols = n

  moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
  def bfs(row, col):
    v = set((row, col))
    q = deque([(row, col, 0)])

    while q:
      r, c, dist = q.popleft()

      if r == pr and c == pc:
        return dist

      for move in moves:
        mr, mc = move
        nr, nc = mr + r, mc + c
        
        pos = (nr, nc)
        if 0 <= nr < rows and 0 <= nc < cols and pos not in v:
          v.add(pos)
          q.append((nr, nc, dist + 1))

    return None
    
  return bfs(kr, kc)