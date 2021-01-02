# The with keyword invokes something called a context manager for the file that we’re calling open() on.
# This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block
# The with syntax replaces older ways to access files where you need to call .close() on the file object manually.
# We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards

with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
