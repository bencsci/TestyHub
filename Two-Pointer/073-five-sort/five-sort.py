# have two pointers at the start and end
# l finds a 5, r skips 5
# swap positions until l < r
# o(n)
#         l      r
# [12, 7, 1, 12, 5, 5]
def five_sort(nums):
  l, r = 0, len(nums)-1

  while l < r:
    if nums[l] == 5 and nums[r] != 5:
      temp = nums[l]
      nums[l] = nums[r]
      nums[r] = temp
    elif nums[l] != 5:
      l += 1
    elif nums[r] == 5:
      r -= 1

  return nums
  