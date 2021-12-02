import os
import json
def crearJson(usuarios):
  a = []
  if not os.path.isfile("usersdb.json"):
      a.append(usuarios)
      with open("usersdb.json", 'w') as f:
          f.write(json.dumps(a, indent=2))
  else:
      with open("usersdb.json") as feedsjson:
          feeds = json.load(feedsjson)

      feeds.append(usuarios)
      with open("usersdb.json", 'w') as f:
          f.write(json.dumps(feeds, indent=2))