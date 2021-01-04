# If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We’d do that like this:
# class SearchEngineEntry:
 # def __init__(self, url):
 #   self.url = url
# codecademy = SearchEngineEntry("www.codecademy.com")
# wikipedia = SearchEngineEntry("www.wikipedia.org")
# print(codecademy.url)
# prints "www.codecademy.com"
# print(wikipedia.url)
# prints "www.wikipedia.org"
# Since the self keyword refers to the object and not the class being called, we can define a secure method on the SearchEngineEntry class that returns the secure link to an entry.

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = (diameter/2)
  def circumference(self):
    circumference = 2 * Circle.pi * self.radius
    return circumference

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
