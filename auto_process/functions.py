import pyautogui as auto
import pyperclip as clip
import time
import json


with open("configs/hot_keys.json", "r", encoding="utf-8") as arquivo:
    hot_keys = json.load(arquivo)

    init_0 = hot_keys.get("init_0", ["ctrl", "win", "left"])
    init_1 = hot_keys.get("init_1", ["alt", "tab"])


def init_with_model(model: int):
    if model:
        auto.hotkey(*init_1)
        return
    auto.hotkey(*init_0)


with open("configs/context.json", "r", encoding="utf-8") as arquivo:
    configs = json.load(arquivo)

    aditional_enter = configs.get("aditional_enter", True)


def escrever(text: str, aditionalEnter=aditional_enter):
    print(aditionalEnter)
    if aditionalEnter:
        auto.press("enter")
    clip.copy(text)
    auto.hotkey("ctrl", "v")
    auto.press("enter")


