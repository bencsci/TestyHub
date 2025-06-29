def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first = elements[0]
  remaining = elements[1:]

  withoutFirst = subsets(remaining)
  withFirst = []
  
  for subset in withoutFirst:
    withFirst.append([first, *subset])

  return withFirst + withoutFirst