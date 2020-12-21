#Write your functi on here
def add_greetings(names):
  return ["Hello, " + names[i] for i in range(len(names)) ]
  # Add "Hello " to names which is the list name and i is the element in the list
  # Keep looping for every name for the length of the list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
#['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
