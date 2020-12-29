# library.py
# that would be the export location
# Add your always_three() function below:
def always_three():
  return 3

# Scope also applies to classes and to the files you are working within.
# Yes. Even files inside the same directory do not have access to each other’s variables, functions, classes, or any other code.
# Well, files are actually modules, so you can give a file access to another file’s content using that glorious import statement.

# Import library below:
from library import always_three


# Call your function below:
print(always_three())
