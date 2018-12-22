# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children
                     if child is not child_node]

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

root.remove_child(bad_seed)
