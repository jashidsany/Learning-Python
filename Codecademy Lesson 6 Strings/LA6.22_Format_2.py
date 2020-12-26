# .format() can be made even more legible for other people reading your code by including keywords.
# Previously with .format(), you had to make sure that your variables-
# -appeared as arguments in the same order that you wanted them to appear in the string, which just added unnecessary complications when writing code.
# def favorite_song_statement(song, artist):
#   return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)
