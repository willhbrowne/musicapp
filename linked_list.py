from list_node import list_node

#A type of collection where each item in the collection is stored individually in memory and each item in the collection stores a reference to the next item in the list. Items in a linked list cannot be referenced with an index because they are not stored sequentially in memory. The attributes are the head node and the number of nodes.
class Linked_list:

  #the only attributes for a linked list are the head node and the number of nodes
  def __init__(self):
    self.head_node = None
    self.num_of_nodes = 0

  def list_size(self):
    return self.num_of_nodes

  #this method helps to traverse the linked list
  #it allows you to loop through your linked list
  #this is how you traverse a linked list
  def __iter__(self):
    node = self.head_node
    while node.next_node is not None:
      yield node
      node = node.next_node

  def insert_at_start(self, data):
    self.num_of_nodes += 1
    new_node = list_node(data)

    if self.head_node is None:
      self.head_node = new_node
    else:
      new_node.next_node = self.head_node
      self.head_node = new_node

  def insert_at_end(self, data):
    self.num_of_nodes += 1
    new_node = list_node(data)

    if self.head_node is None:
      self.head_node = new_node
    else:
      temp_node = self.head_node
      while temp_node.next_node is not None:
        temp_node = temp_node.next_node
      temp_node.next_node = new_node

  def insert_after(self, node, data):
    self.num_of_nodes += 1
    new_node = list_node(data)
    temp_node = self.head_node
    while temp_node.data is not node:
      temp_node = temp_node.next_node
      if temp_node.next_node is None:
        break

    new_node.next_node = temp_node.next_node
    temp_node.next_node = new_node

  #Same as iter but prints out every node
  def traverse(self):
    current_node = self.head_node
    while current_node is not None:
      print(current_node)
      current_node = current_node.next_node

  #Create a node out of the data
  #if the list is empty it makes the data the head node
  #If the data comes before the head node alphabetically then it puts it at the beginning
  #Otherwise it going through the linked list and adds it in the correct spot alphabetically

  def add(self, data):
    self.num_of_nodes += 1
    new_node = list_node(data)

    if self.head_node is None:
      self.head_node = new_node
    elif self.head_node.data.title >= new_node.data.title:
      new_node.next_node = self.head_node
      self.head_node = new_node
    else:
      temp_node = self.head_node
      previous_node = self.head_node
      while temp_node is not None and new_node.data.title > temp_node.data.title:
        previous_node = temp_node
        temp_node = temp_node.next_node
      previous_node.next_node = new_node
      new_node.next_node = temp_node

  def __repr__(self):
    list = []
    temp_node = self.head_node
    while temp_node is not None:
      list.append(temp_node.data)
      temp_node = temp_node.next_node
    return str(list)

  def search(self, data):
    temp = self.head_node
    for i in range(self.num_of_nodes):
      if temp.data.username == data:
        return temp.data
      temp = temp.next_node
    return None