# One way that we can introduce polymorphism to our class definitions is by using Python’s special dunder methods. We’ve explored a few already, the constructor __init__() and the string representation method __repr__, but that’s only scratching the tip of the iceberg.
# Since we defined an __add__ method for our Color class, we were able to add these objects together using the + operator.

class Atom:
  def __init__(self, label):
    self.label = label

  def __add__(self, other):
    return Molecule([self,other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
