# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using.
# If the key you are trying to .get() does not exist, it will return None by default:
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# this line will return 632:
# building_heights.get("Shanghai Tower")
# this line will return None:
# building_heights.get("My House")
# You can also specify a value to return if the key doesn’t exist.
# For example, we might want to return a building height of 0 if our desired building is not in the dictionary:
# >>> building_heights.get('Shanghai Tower', 0)
# 632
# >>> building_heights.get('Mt Olympus', 0)
# 0
# >>> building_heights.get('Kilimanjaro', 'No Value')
# 'No Value'

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder")
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
