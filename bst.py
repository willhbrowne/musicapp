#This class creates nodes specific to binary search trees. In this case, each instance is a song. The attributes are the data of the song, the children nodes (right and left), and the parent node, which starts as None but every node besides the root has a parent.
class bst_node:

  def __init__(self, data, parent=None):
    self.data = data
    self.left_node = None
    self.right_node = None
    self.parent = None

  def __repr__(self):
    return str(self.data)

#This class is a binary-sorted data structure that is sorted based on the title of the song: it is in alphabetical order. The attributes are the root (first) node that is at the top of the tree: it is the first song imported into the tree. 
class BinarySearchTree():

  def __init__(self):
    self.root = None
    self.num_of_nodes = 0

  def insert(self, data):
    self.num_of_nodes += 1
    if self.root is None:
      self.root = bst_node(data)
    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, node):
    if data.title.lower() < node.data.title.lower():
      if node.left_node is not None:
        self.insert_node(data, node.left_node)
      else:
        node.left_node = bst_node(data, node)
    else:
      if node.right_node is not None:
        self.insert_node(data, node.right_node)
      else:
        node.right_node = bst_node(data, node)

  def traverse(self):
    if self.root is not None:
      self.traverse_in_order(self.root)

  def traverse_in_order(self, node):
    if node.left_node is not None:
      self.traverse_in_order(node.left_node)
    print(node.data)
    if node.right_node is not None:
      self.traverse_in_order(node.right_node)

  def get_min(self):
    temp = self.root
    while temp.left_node is not None:
      temp = temp.left_node
    return temp

  def get_max(self):
    temp = self.root
    while temp.right_node is not None:
      temp = temp.right_node
    return temp

  def search(self, data, root):
    if data == root.data.num:
      return root
    elif data < root.data.num:
      return self.search(data, root.left_node)
    else:
      return self.search(data, root.right_node)

  def remove(self, data):
    node = self.search(data, self.root)
    if node.left_node is None and node.right_node is None:
      if node.parent.data > node.data:
        node.parent.left_node = None
      else:
        node.parent.right_node = None
    elif (node.left_node is None and node.right_node is not None):
      if node.parent.data > node.data:
        node.parent.left_node = node.right_node
      else:
        node.parent.right_node = node.right_node
    elif (node.left_node is not None and node.right_node is None):
      if node.parent.data > node.data:
        node.parent.left_node = node.left_node
      else:
        node.parent.right_node = node.left_node
    else:
      temp = node.left_node
      while temp.right_node is not None:
        temp = temp.right_node
      temp.parent.right_node = None
      temp.left_node = node.left_node
      temp.parent = node.parent
      temp.right_node = node.right_node
      if temp.right_node is not None:
        temp.right_node.parent = temp
      node.parent.left_node = temp
