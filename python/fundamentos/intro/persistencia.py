import json

streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)
print()

with open("./python/fundamentos/intro/streamers.json", "w") as archivo:
   json.dump(streamers, archivo)

with open("./python/fundamentos/intro/streamers.json", "r") as archivo:
   streamers_nuevos = json.load(archivo)
print("Nuevo Streamers")
print(streamers_nuevos)