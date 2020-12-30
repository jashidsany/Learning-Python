# If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
# Looking at our sensors object from the first exercise:
# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
# If we wanted to add 3 new rooms, we could use:
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# which would add all three items to the sensors dictionary. Now, sensors looks like:
# {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
