# We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary.
# If we try to, we will get a TypeError. For example:
# The word “unhashable” in this context means that this ‘list’ is an object that can be changed.
# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key.
# If the key can change, that hash value would not be reliable.
# So the keys must always be unchangeable, hashable data types, like numbers or strings.

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}
