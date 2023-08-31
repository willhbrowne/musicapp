from list_node import list_node

#The queue class has three attributes: the head node, the rear node, and the amount of nodes. Within the queue are nodes (songs): the first 10 songs in each user's queue are random, but after that they can add songs that will be ready for playing as they traverse the queue. Each instance of the queue class literally represents a "queue" like in Spotify: it is a list of songs (nodes) that are next to play for the user.
class Queue:

  def __init__(self):
    self.head_node = None
    self.rear_node = None
    self.num_of_nodes = 0

  def enqueue(self, data):
    self.num_of_nodes += 1
    new_node = list_node(data)
    if self.head_node is None:
      self.head_node = new_node
    elif self.rear_node is None:
      self.rear_node = new_node
      self.head_node.next_node = self.rear_node
    else:
      self.rear_node.next_node = new_node
      self.rear_node = new_node

  def dequeue(self):
    self.num_of_nodes -= 1
    temp_node = self.head_node
    self.head_node = temp_node.next_node
    return temp_node.data

  def __repr__(self):
    return "Queue: " + str([i for i in self])

  def __iter__(self):
    temp = self.head_node
    while temp.next_node is not None:
      yield temp 
      temp = temp.next_node