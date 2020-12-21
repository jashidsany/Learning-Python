#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    # while length of lst is greater than 0 and the starting element is even
    lst = lst[1:]
    # run this line of code where lst runs the 2nd element and returns it to lst
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
