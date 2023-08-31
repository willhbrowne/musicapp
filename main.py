#Our program represents a Spotify-type app with different users, each with separate usernames and passcodes, with playlists with songs that can be accessed and “played” whenever the user is logged in. There are many different commands that the user can input, such as creating a playlist or a “queue” of songs that are set to play next. This type of program would be useful for someone looking to create a startup website or app similar to Spotify. Although it isn’t nearly as advanced as Spotify, our code is a good baseline for getting ideas and seeing working code. Having different users that have different logins with different playlists is a very real-life application, that major music apps use every day. If we continued to work on our project, we could add even more commands that would make the program run smoother or we could make the project much more visually appealing, with a search bar or different colors that make it look more realistic. But overall, our project has strong real-life applications that could be used for a pseudo-Spotify.
from playlist import Playlist
from song import Song
from user import User
from list_node import list_node

#This function enables the user to login by prompting them to enter a user-specific username and password. 
def login():
  username = input("Please enter your username: ")
  password = input("Please enter you password: ")
  search = User.all_users.search(username)
  if search is not None:
    if search.password == password:
      print("Logged in")
      return search
    else:
      print("Username or password incorrect")
      print()
      return login()
  else:
    print("Username or password incorrect")
    print()
    return login()

Song.import_songs("songs.csv")
User.import_users("users.csv")
logged_in = login()

end = input("What would you like to do? Enter 'help' for a list of commands\n")
while True:
  if end == "help":
    print("'end' - ends your current session\n'create playlist' - prompts you to create a playlist\n'play playlist' - plays a playlist that you enter\n'add queue' - adds a song that you enter to your queue\n'play song' - plays a specific song, or one from playlist/queue\n'play history' - plays the last song that you listened to\n'log out' - logs your user out of the program\n'clear queue' - clears your current queue\n")
  elif end == "end":
    break

    
  elif end == "create playlist":
    done: str
    p = Playlist(input("What would you like your playlist to be called?\n"))
    while True:
      done = input("Which song would you like to add to the playlist? Enter a number between 1 and 11083 or enter 'done' to finish your playlist:\n")
      if done == "done":
        print("Created playlist '" + p.title + "' with " + str(p.songs) + " songs")
        break
      if done.isnumeric():
        song = int(done)
        if song > 0 and song < 11084:
          s = Song.all_songs.search(song, Song.all_songs.root).data
          p.add_song(s)
          print("Added song: " + s.title)
      else:
        print("That is not a number")
    logged_in.add_playlist(p)
    

  elif end == "add queue":
    num = input("Which song would you like to add to the queue? Enter a number between 1 and 11083\n")
    if num.isnumeric():
      num = int(num)
      if num > 0 and num < 11083:
        s = Song.all_songs.search(num, Song.all_songs.root).data
        logged_in.add_to_queue(list_node(s))
        print("Added song: " + s.title)
      else:
        print("That number is not within the correct range")
    else:
      print("That is not a number")

      
  elif end == "play song":
    play = input("Would you like to play a song from a playlist, from the queue, or a specific song?\n")
    if play == "playlist":
      playlist = input("Which playlist would you like to listen to?\n")
      temp = logged_in.playlists.head_node 
      while temp is not None:
        if temp.data.title == playlist:
          break 
        temp = temp.next_node 
      if temp is not None:
        temp_song = temp.data.head_node
        for i in range(temp.data.songs):
          print("Playing song: " + temp_song.data.title)
          if i != temp.data.songs-1:
            cont = input("Play next song or exit?\n")
          if cont == "exit":
            print("Stopping playlist")
            break
          temp_song = temp_song.next_node
    if play == "queue":
      if logged_in.queue.num_of_nodes > 0:
        print("Playing song: " + logged_in.play_next().data.title)
      else:
        print("There are no songs in the queue")
    if play == "song":
      num = input("Which song would you like to play? Enter a number between 0 and 11083\n")
      if num.isnumeric():
        num = int(num)
        if num > 0 and num < 11084:
          print("Playing song: " + Song.all_songs.search(num, Song.all_songs.root).data.title)
        else:
          print("What number is not within the correct range")
      else:
        print("That is not a number")
        
  elif end == "play history":
    if logged_in.history.num_of_nodes > 0:
      print("Playing song: " + logged_in.play_last().title)
    else:
      print("You have no history")

  elif end == "log out":
    print("You are now logged out")
    logged_in = login()

  elif end == "clear queue":
    print("Clearing queue")
    logged_in.clear_queue()
  end = input("What would you like to do? Enter 'help' for a list of commands\n")
print("Ended session")