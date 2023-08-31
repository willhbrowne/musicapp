import csv
from playlist import Playlist
from linked_list import Linked_list
from queue import Queue
from stack import Stack
from song import Song

#The user class has one class attribute: all_users, which is a linked list of all the users in the imported csv. Each instance of this class represents a user of our pseudo-Spotify app, who each have a specific username, password, email, a "queue" which holds the songs that are next to play, a history which is a stack of the last songs played by the user, and their playlists, which are linked lists that hold songs that the user adds to the playlist through the index of the songs.
class User:
  all_users = Linked_list()

  def __init__(self, username, password, email, queue, history, playlists):
    self.username = username
    self.password = password
    self.email = email
    self.queue = queue
    self.history = history
    self.playlists = playlists
    self.playlists.insert_at_end(User.random_playlist("First playlist", 5))
    User.all_users.insert_at_end(self)
    for i in range(5):
      self.add_to_queue(Song.random_song())

  def __repr__(self):
    return "username: " + self.username + " password: " + self.password + " email: " + self.email

  def add_playlist(self, playlist):
    self.playlists.add(playlist)

  @classmethod
  def random_playlist(cls, title, num_of_songs):
    p = Playlist(title)
    for i in range(num_of_songs):
      p.add_song(Song.random_song())
    return p
      
  def add_to_queue(self, song):
    self.queue.enqueue(song)

  def play_last(self):
    temp = self.history.peek(0)
    self.history.pop()
    return temp.data

  def play_next(self):
    temp = self.queue.dequeue()
    self.history.push(temp)
    return temp

  def play_song(self, song):
    self.history.push(song)

  def clear_queue(self):
    self.queue = Queue()

  @staticmethod
  def search(keyword):
      matches = []
      current_node = User.all_users.head_node
      while current_node is not None:
          if keyword.lower() in current_node.data.username.lower():
              matches.append(current_node)
          current_node = current_node.next_node
      return matches[0].data
  
  @classmethod  #designates it as a class method
  def import_users(cls, filename: str):
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      items = list(reader)
    for item in items:
      User(
        username=item.get('username'),
        password = item.get("password"),
        email = item.get("email"),
        queue = Queue(),
        history = Stack(),
        playlists = Linked_list()
        )