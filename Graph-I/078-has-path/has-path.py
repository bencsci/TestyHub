def has_path(graph, src, dst):

  def dfs(src):
    if src == dst:
      return True

    for node in graph[src]:
      if dfs(node):
        return True

    return False
  #Test
  return dfs(src)
  