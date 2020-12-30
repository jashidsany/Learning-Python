songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

zipped_music = zip(songs, playcounts)
plays = {songs:playcounts for songs, playcounts in zipped_music}
print(plays)
print("\n")

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
