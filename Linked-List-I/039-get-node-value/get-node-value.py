# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  count = 0
  curr = head
  ans = None
  while curr:
    if count == index:
      ans = curr.val
    count += 1
    curr = curr.next
  return ans
    
