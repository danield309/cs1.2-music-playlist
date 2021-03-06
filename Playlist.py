from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song
  
   # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song = self.__first_song
    index = 0

    while current_song != None:
      if current_song.get_title() == title:
        return index
      
      if current_song.get_title() != title:
        index += 1
        current_song = current_song.get_next_song()
        index = -1
        return index

  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.__first_song

    if current_song.get_title != title:
      return print(f"{title} was deleted!")

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    length = 0
    current_song = self.__first_song

    while current_song != None:
      length += 1
      current_song = current_song.get_next_song()
      return length


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.__first_song
    index = 1
    
    while current_song != None:
      print(f"{current_song} {index}")
      current_song = current_song.get_next_song()
      index +=1
