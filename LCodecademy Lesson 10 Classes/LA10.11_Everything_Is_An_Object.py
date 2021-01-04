# We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.
# Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list
# Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically. But these instances are still full-blown objects to Python.

dir(5)

def this_function_is_an_object(x):
  return x

print(dir(this_function_is_an_object))
