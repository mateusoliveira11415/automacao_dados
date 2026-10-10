import json


with open("preferences.json", "r", encoding="utf-8") as arquivo:
    preferences = json.load(arquivo)

    button_color = preferences["button_color"]
    button_hover_color = preferences["button_hover_color"]