#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0 # creates a sum1
  sum2 = 0 # creates a  sum2
  for number in lst1: # for elements in lst1
    sum1 += number # add the elements in lst1 to variable sum1
  for number in lst2: # for elements in lst2
    sum2 += number # add the elements in lst2 to variable sum2
  if sum1 >= sum2: # if sum of elements in lst1 > lst2 return lst1, if sum is equal return lst1
    return lst1
  else: # else return lst2
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
