#Write your function here
def same_values(lst1, lst2):
  new_lst = [] # creates new list
  for index in range(len(lst1)): # for each index in range of the length of lst1
    if lst1[index] == lst2[index]: # if the indexs are the same
      new_lst.append(index) # append that index to the new list
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
