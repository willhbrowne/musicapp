# musicapp

# what does this project do?

Our program represents a Spotify-type app with different users, each with separate usernames and passcodes, with playlists with songs that can be accessed and “played” whenever the user is logged in. There are many different commands that the user can input, such as creating a playlist or a “queue” of songs that are set to play next. This type of program would be useful for someone looking to create a startup website or app similar to Spotify. Although it isn’t nearly as advanced as Spotify, our code is a good baseline for getting ideas and seeing working code. Having different users that have different logins with different playlists is a very real-life application, that major music apps use every day. If we continued to work on our project, we could add even more commands that would make the program run smoother or we could make the project much more visually appealing, with a search bar or different colors that make it look more realistic. But overall, our project has strong real-life applications that could be used for a pseudo-Spotify.

# playlist class

Each instance of playlist represents a playlist of songs. Each playlist is a linked list. The attributes of each playlist are the number of songs in the playlist, the head node (first song), and the title/name of the playlist. 

# queue class

The queue class has three attributes: the head node, the rear node, and the amount of nodes. Within the queue are nodes (songs): the first 10 songs in each user's queue are random, but after that they can add songs that will be ready for playing as they traverse the queue. Each instance of the queue class literally represents a "queue" like in Spotify: it is a list of songs (nodes) that are next to play for the user.

# song class

Each instance of the song class creates a song. Each song has the title, the artist, the amount of streams on Spotify, the amount of days since released, and the index of the song (where it is within the binary search tree). The class attributes are all_songs, which is a binary search tree that holds all the songs in alphabetical order, and "i", which is the index of each song. 

# stack class

Stack is a customized linked list: it will behave like a stack but is a sub-species of a linked list. Each stack has attributes of a head node and the number of nodes within the stack. In this specific project's case, each stack represents the history of a specific user (their most recently played song). 

# linked list class

A type of collection where each item in the collection is stored individually in memory and each item in the collection stores a reference to the next item in the list. Items in a linked list cannot be referenced with an index because they are not stored sequentially in memory. The attributes are the head node and the number of nodes.

# bst node class

This class creates nodes specific to binary search trees. In this case, each instance is a song. The attributes are the data of the song, the children nodes (right and left), and the parent node, which starts as None but every node besides the root has a parent.

# bst class

This class is a binary-sorted data structure that is sorted based on the title of the song: it is in alphabetical order. The attributes are the root (first) node that is at the top of the tree: it is the first song imported into the tree. 

# user class

The user class has one class attribute: all_users, which is a linked list of all the users in the imported csv. Each instance of this class represents a user of our pseudo-Spotify app, who each have a specific username, password, email, a "queue" which holds the songs that are next to play, a history which is a stack of the last songs played by the user, and their playlists, which are linked lists that hold songs that the user adds to the playlist through the index of the songs.

# list node class

Each instance of this class is a node. The attributes are the data/information inside the node and the next_node, which is the one that comes after the node in the linked list.
