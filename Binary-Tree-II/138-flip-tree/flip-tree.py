# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  if root is None:
    return None

  temp = root.left
  root.left = root.right
  root.right = temp

  flip_tree(root.left)
  flip_tree(root.right)

  return root