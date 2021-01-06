# In Python we can return multiple pieces of data by separating each variable with a comma
# What if we wanted to save these two results in separate variables? Well we can by unpacking the function return. We can list our new variables, comma-separated, that correspond to the number of values returned:

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("hey")
print(the_scream)
print(the_whisper)
