def permutations(items):
  res = []
  sol = []

  def dfs():
    if len(sol) == len(items):
      res.append(sol[:])
      return

    for item in items:
      if item not in sol:
        sol.append(item)
        dfs()
        sol.pop()

  dfs()
  return res