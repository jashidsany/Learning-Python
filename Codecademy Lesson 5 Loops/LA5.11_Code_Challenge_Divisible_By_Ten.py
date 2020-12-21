# Divisible By Ten Challenge

#Write your function here
def divisible_by_ten(nums):
  count = 0 # a counter to hold values
  for number in nums: # number is the elements while nums is the list
    if number % 10 == 0: # for every number in nums that is divisible by 10 add 1 to count
      count += 1
  return count # make sure the indentation is correct otherwise wrong value is output

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40])
