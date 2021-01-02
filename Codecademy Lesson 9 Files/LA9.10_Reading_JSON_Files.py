# SON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript.
# The name, like CSV is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON).

import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message)
