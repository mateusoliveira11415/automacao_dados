import pyautogui as auto
import pyperclip as clip
import time
import json


with open("configs/hot_keys.json", "r", encoding="utf-8") as arquivo:
    hot_keys = json.load(arquivo)

    init_0 = hot_keys.get("init_0", ["ctrl", "win", "left"])
    init_1 = hot_keys.get("init_1", ["alt", "tab"])


with open("configs/context.json", "r", encoding="utf-8") as arquivo:
    configs = json.load(arquivo)

    additional_enter = configs.get("aditional_enter", True)

    simple_dicio = configs["simple_dicio"]
    compound_dicio = configs["compound_dicio"]


with open("configs/error_messages.json", "r", encoding="utf-8") as arquivo:
    dicio_error = json.load(arquivo)

    none_key = dicio_error.get("none_key", "!Chave inexistente! ")
    index_error = dicio_error.get("index_error", "!Valores insuficientes! ")
    value_error = dicio_error.get("value_error", "!Valor inválido para conversão! ")


def init_with_model(model: int):
    if model:
        auto.hotkey(*init_1)
        return
    auto.hotkey(*init_0)


def write(text: str, additionalEnter=additional_enter):
    if additionalEnter:
        auto.press("enter")
    clip.copy(text)
    auto.hotkey("ctrl", "v")
    auto.press("enter")


def open_aplication(application_name):
    auto.press("win")
    auto.write(application_name)
    auto.press("enter")


def write_simple_compound_dicio(infor: str):
    info_list = infor.split(",")
    primary_key = info_list[0]

    if len(info_list) < 2:
        write(index_error)
        return

    if not int(primary_key):
        text = simple_dicio.get(info_list[1], none_key)
        write(text)
        return

    try:
        text = compound_dicio.get(primary_key, none_key)
        range_value = int(info_list[1])
        info_list = info_list[2:]

        for i in range(range_value):
            text = text.replace(f".{i}.", info_list[i])

    except IndexError:
        write(index_error)
        return

    except ValueError:
        write(value_error)
        return
    
    write(text)
