import requests
import json
import sys

# Velocità di movimento in km/h
vel = 5

with open('interesse.csv') as csv_file:
  coords=[]
  lines = csv_file.readlines()
  for i in range(1,len(lines)):
    data = lines[i].split(',')
    raw = data[0]
    raw = raw.replace('"POINT (','')
    raw = raw.replace(')"','')
    raw = raw.split(' ')
    coords.append(raw)

original_stdout = sys.stdout # Save a reference to the original standard output
with open('distanze.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created
    for i in range(len(coords)-1):
      for j in range(i+1, len(coords)):
        r = requests.get(f"""https://routing.openstreetmap.de/routed-car/route/v1/car/{coords[i][0]},{coords[i][1]};{coords[j][0]},{coords[j][1]}?overview=full""")
        route_1 = json.loads(r.content)["routes"][0]
        tempo = int(((route_1["distance"]/1000)/vel)*60)
        print(i, j, tempo)
    sys.stdout = original_stdout # Reset the standard output to its original value