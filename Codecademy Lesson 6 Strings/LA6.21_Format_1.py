# Python also provides a handy string method for including variables in strings.
# This method is .format(). .format() takes variables as an argument and includes them in the string that it is run on.
# You include {} marks as placeholders for where those variables will be imported.
# def favorite_song_statement(song, artist):
#   return "My favorite song is {} by {}.".format(song, artist)

def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)

poem_title_card("I Hear America Singing", "Walt Whitman")
print(poem_title_card("I Hear America Singing", "Walt Whitman"))
