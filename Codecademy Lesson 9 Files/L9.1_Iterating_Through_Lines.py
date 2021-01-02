# When we read a file, we might want to grab the whole document in a single string, like .read() would return.
# But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing. Suppose we have a file:
# keats_sonnet.txt
# To one who has been long in city pent,
# ’Tis very sweet to look into the fair
# And open face of heaven,—to breathe a prayer
# Full in the smile of the blue firmament.
# script.py
# with open('keats_sonnet.txt') as keats_sonnet:
#  for line in keats_sonnet.readlines():
#    print(line)
# The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt.
# It then iterates over each line in the document and prints the entire file out.

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
