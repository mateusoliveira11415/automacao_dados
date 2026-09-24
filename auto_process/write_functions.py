import pyautogui as auto
import pyperclip as clip
import functions.text as text_func
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
    complex_dicio = configs["complex_dicio"]


with open("configs/error_messages.json", "r", encoding="utf-8") as arquivo:
    dicio_error = json.load(arquivo)

    none_key = dicio_error.get("none_key", "!Chave inexistente! ")
    index_error = dicio_error.get("index_error", "!Valores insuficientes! ")
    value_error = dicio_error.get("value_error", "!Valor inválido para conversão! ")


def initialize_model_shortcut(model: int):
    if model:
        auto.hotkey(*init_1)
        return
    auto.hotkey(*init_0)


def past_text(text: str, additionalEnter=additional_enter):
    if additionalEnter:
        auto.press("enter")
    clip.copy(text)
    auto.hotkey("ctrl", "v")
    auto.press("enter")


def render_simple_compound(infor: str):
    info_list = infor.split(",")
    primary_key = info_list[0]

    if len(info_list) < 2:
        past_text(index_error)
        return

    if not int(primary_key):
        text = simple_dicio.get(info_list[1], none_key)
        past_text(text)
        return

    try:
        text = compound_dicio.get(primary_key, none_key)
        replace_times = int(info_list[1])
        info_list = info_list[2:]
        text, info_list = text_func.replace_placeholders(text, replace_times, info_list)

    except IndexError:
        past_text(index_error)
        return

    except ValueError:
        past_text(value_error)
        return
    
    past_text(text)


def render_complex(infor: str):
    print("Função chamada")
    info_list = infor.split(",")
    print(info_list)

    try:
        primary_key = info_list[0]
        replace_primary_key = int(info_list[1])
        increment_times = int(info_list[2])
        is_ordening = int(info_list[3])
        text = complex_dicio.get(primary_key, none_key)

        info_list = info_list[4:]

        text, info_list = text_func.replace_placeholders(text, replace_primary_key, info_list)

    except IndexError:
        past_text(index_error)
        return

    except ValueError:
        past_text(value_error)
        return

    try:
        for i in range(increment_times):
            if is_ordening:
                text = text + f"{i + 1}: "

            second_key = info_list[0]
            replace_times = int(info_list[1])

            text = text + complex_dicio.get(str(primary_key + second_key), none_key)

            info_list = info_list[2:]
            
            text, info_list = text_func.replace_placeholders(text, replace_times, info_list)

    except IndexError:
        past_text(index_error)
        return

    except ValueError:
        past_text(value_error)
        return

    past_text(text)


initialize_model_shortcut(1)
render_complex("a,2,2,0,15,16,1,1,5,2,1,10")