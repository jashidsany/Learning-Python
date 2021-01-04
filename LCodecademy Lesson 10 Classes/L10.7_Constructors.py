# There are different methods called magic because they behave differently from regular methods. Another popular ter is dunder methods because they usually have two underscores such as __init__().
# __init__() initializes a newly created object. It is called everytime the class is instantiated.
# Methods that are used to prepare an object being instantiated are called constructors.

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    # use .format after the string and set what you want to format in the ()
teaching_table = Circle(36)
