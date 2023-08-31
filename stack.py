from list_node import list_node

#Stack is a customized linked list: it will behave like a stack but is a sub-species of a linked list. Each stack has attributes of a head node and the number of nodes within the stack. In this specific project's case, each stack represents the history of a specific user (their most recently played song). 
class Stack:

  def __init__(self):
    self.head_node = None
    self.num_of_nodes = 0

  def stack_size(self):
    return self.num_of_nodes

  def push(self, data):
    self.num_of_nodes += 1
    new_node = list_node(data)
    if self.head_node is None:
      self.head_node = new_node
    else:
      new_node.next_node = self.head_node
      self.head_node = new_node

  def pop(self):
    self.num_of_nodes -= 1
    remove = self.head_node
    self.head_node = self.head_node.next_node
    return remove.data

  def peek(self, i):
    temp_node = self.head_node
    if self.num_of_nodes > i:
      for x in range(i):
        temp_node = temp_node.next_node
      return temp_node.data