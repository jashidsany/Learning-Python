#Write your function here
def exponents(bases, powers):
  new_lst = [] # creates a new list
  for base in bases: # for each element in bases loop through
    for power in powers: # for each element in powers loop the arguement
      new_lst.append(base ** power) # adds the base ** power to the new list
  return new_lst # returns new list (indentation must match up with first indent)

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
