#Write your function here
def over_nine_thousand(lst):
  sum = 0 # creates a variable to store sum
  for number in lst: # for each number in lst
    sum += number # add it to the sum variable
    if sum > 9000: # if the sum happens to go over 9000 break
      break
  return sum # return the sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
