# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#                          P    C
#      5 -> 5 -> 7 -> 7 -> 7 -> 6

def longest_streak(head):
  prev, curr = None, head
  longest = 0
  streak = 1
  while curr:
    if prev and curr.val != prev.val:
      streak = 1
    elif prev and curr.val == prev.val:
      streak += 1
    longest = max(streak, longest)
    prev = curr 
    curr = curr.next

  return longest   