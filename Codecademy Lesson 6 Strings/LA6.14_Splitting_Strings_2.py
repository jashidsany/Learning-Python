# If we provide an argument for .split() we can dictate the character we want our string to be split on. This argument should be provided as a string itself.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# This creates a new and iterates through author_names
# author_last_names has name split by a negative index and appends the rest of the string to author_last_names
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)
