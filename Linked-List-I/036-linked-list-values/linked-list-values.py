# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  ans = []
  curr = head
  while curr:
    ans.append(curr.val)
    curr = curr.next 
  return ans
  # Test 3