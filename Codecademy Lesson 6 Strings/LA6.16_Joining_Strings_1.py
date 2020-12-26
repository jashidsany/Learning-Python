# Now that you’ve learned to break strings apart using .split(), let’s learn to put them back together using .join(). .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter. The syntax of .join() is:
# 'delimiter'.join(list_you_want_to_join)
# Delimiters are spaces 
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = (' '.join(reapers_line_one_words))
print(reapers_line_one)
