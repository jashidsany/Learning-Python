#Write your function here
def max_num(nums):
  maximum = nums[0] # maximum is the first element
  for number in nums: # for each element in nums
    if number > maximum: # if number is greater than maximum
      maximum = number # maximum is equal to that number
  return maximum # returns maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
