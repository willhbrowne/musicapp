#Each instance of this class is a node. The attributes are the data/information inside the node and the next_node, which is the one that comes after the node in the linked list.
class list_node:
  def __init__(self, data):
    self.data = data 
    self.next_node = None
        
    #Returns the string representation of the node
  def __repr__(self):
    return str(self.data)