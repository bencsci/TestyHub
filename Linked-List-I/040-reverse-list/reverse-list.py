# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  prev, curr = None, head
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  return prev

