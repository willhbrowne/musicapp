import csv
from bst import BinarySearchTree
import random

#Each instance of the song class creates a song. Each song has the title, the artist, the amount of streams on Spotify, the amount of days since released, and the index of the song (where it is within the binary search tree). The class attributes are all_songs, which is a binary search tree that holds all the songs in alphabetical order, and "i", which is the index of each song. 
class Song:
  all_songs = BinarySearchTree()
  i = 0


  def __init__(self, title, artist, streams, days):
    self.title = title
    self.artist = artist
    self.streams = streams
    self.days = days
    self.num: int
    Song.all_songs.insert(self)

  def __repr__(self):
    return "Title: " + self.title + " Artist: " + self.artist + " Streams: " + str(
      self.streams) + " Days: " + str(self.days)

  @classmethod  #designates it as a class method
  def import_songs(cls, filename: str):
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      items = list(reader)
    for item in items:
      Song(
        title=item.get('Song Name'),
        artist=item.get('Artist Name'),
        streams=int(item.get('Total Streams')),
        days=int(item.get('Days')))
    Song.Index()

  @classmethod 
  def random_song(cls):
    x = random.randint(0, Song.all_songs.num_of_nodes-1)
    return Song.all_songs.search(x, Song.all_songs.root)
    

  @classmethod
  def Index(cls):
    if Song.all_songs.root is not None:
      Song.traverse_in_order(Song.all_songs.root)

  @classmethod
  def traverse_in_order(cls, node):
    if node.left_node is not None:
      Song.traverse_in_order(node.left_node)
    node.data.num = Song.i
    Song.i += 1
    if node.right_node is not None:
      Song.traverse_in_order(node.right_node)