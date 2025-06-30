# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#          P    C
#     7 -> 7 -> 7
def is_univalue_list(head):
  prev, curr = None, head

  while curr:
    if prev and curr.val != prev.val:
      return False

    prev = curr
    curr = curr.next

  return True
