# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def linked_palindrome(head):
  nums = []

  curr = head
  
  while curr:
    nums.append(curr.val)
    curr = curr.next

  l, r = 0, len(nums) - 1
  while l < r:
    if nums[l] != nums[r]:
      return False
    l += 1
    r -= 1

  return True
