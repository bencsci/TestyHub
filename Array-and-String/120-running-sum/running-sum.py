def running_sum(numbers):
  sum = 0
  res = []
  for num in numbers:
    sum += num
    res.append(sum)

  return res