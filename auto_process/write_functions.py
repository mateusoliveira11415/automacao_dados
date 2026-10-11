from functions import text as text_func
from functions import reader_configs as rconfig
import pyautogui as auto
import pyperclip as clip
import time


def initialize_model_shortcut(model: int):
    if model:
        auto.hotkey(*rconfig.init_1)
        return
    auto.hotkey(*rconfig.init_0)


def past_text(text: str, additionalEnter=rconfig.additional_enter):
    if additionalEnter:
        auto.press("enter")
    clip.copy(text)
    auto.hotkey("ctrl", "v")
    auto.press("enter")


def render_simple_compound(infor: str):
    info_list = infor.split(",")
    primary_key = info_list[0]

    if len(info_list) < 2:
        past_text(rconfig.index_error)
        return

    if not int(primary_key):
        text = rconfig.simple_dicio.get(info_list[1], rconfig.none_key)
        past_text(text)
        return

    try:
        text = rconfig.compound_dicio.get(primary_key, rconfig.none_key)
        replace_times = int(info_list[1])
        info_list = info_list[2:]
        text, info_list = text_func.replace_placeholders(text, replace_times, info_list)

    except IndexError:
        past_text(rconfig.index_error)
        return

    except ValueError:
        past_text(rconfig.value_error)
        return
    
    past_text(text)


def render_complex(infor: str):
    info_list = infor.split(",")

    try:
        primary_key = info_list[0]
        replace_primary_key = int(info_list[1])
        increment_times = int(info_list[2])
        is_ordening = int(info_list[3])
        text = rconfig.complex_dicio.get(primary_key, rconfig.none_key)

        info_list = info_list[4:]

        text, info_list = text_func.replace_placeholders(text, replace_primary_key, info_list)

    except IndexError:
        past_text(rconfig.index_error)
        return

    except ValueError:
        past_text(rconfig.value_error)
        return

    try:
        for i in range(increment_times):
            if is_ordening:
                text = text + f"{i + 1}: "

            second_key = info_list[0]
            replace_times = int(info_list[1])

            text = text + rconfig.complex_dicio.get(str(primary_key + second_key), rconfig.none_key)

            info_list = info_list[2:]
            
            text, info_list = text_func.replace_placeholders(text, replace_times, info_list)

    except IndexError:
        past_text(rconfig.index_error)
        return

    except ValueError:
        past_text(rconfig.value_error)
        return

    past_text(text)

