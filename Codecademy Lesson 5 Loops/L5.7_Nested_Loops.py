sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data: # location is the sublists
  print(location)
  for scoops in location: # scoops is elements in the sublists
    scoops_sold += scoops # this adds those elements to scoops_sold

print(scoops_sold)
