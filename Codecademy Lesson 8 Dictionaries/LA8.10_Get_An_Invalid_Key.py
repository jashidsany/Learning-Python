# Accessing a key that is not part of the dictonary will produce an error.
# One way to avoid this error is to first check if the key exists in the dictionary:
# key_to_check = "Landmark 81"
# if key_to_check in building_heights:
#  print(building_heights["Landmark 81"])
# This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])
