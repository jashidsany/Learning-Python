# However, if we call range with two arguments, we can create a list that starts at a different number.
# For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):
# If we use a third argument, we can create a list that “skips” numbers.
# For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

list1 = range(5, 15, 3)
print(list(list1))

list2 = range(0, 40, 5)
print(list(list2))
