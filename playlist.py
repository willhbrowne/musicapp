from list_node import list_node

#Each instance of playlist represents a playlist of songs. Each playlist is a linked list. The attributes of each playlist are the number of songs in the playlist, the head node (first song), and the title/name of the playlist. 
class Playlist:
  def __init__(self, title):
    self.songs = 0
    self.head_node = None
    self.title = title

  def add_song(self, song):
    self.songs += 1
    new_node = list_node(song)
    if self.head_node is None:
      self.head_node = new_node
    else:
      new_node.next_node = self.head_node
      self.head_node = new_node

  def __repr__(self):
    return " Title: " + self.title + " songs: " + str([i for i in self])

  def __iter__(self):
    temp = self.head_node
    while temp.next_node is not None:
      yield temp 
      temp = temp.next_node

  def traverse(self):
    temp = self.head_node 
    while temp is not None:
      print(temp.data)
      temp = temp.next_node