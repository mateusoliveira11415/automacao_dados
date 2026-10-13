import json


with open("configs/preferences.json", "r", encoding="utf-8") as arquivo:
    preferences = json.load(arquivo)