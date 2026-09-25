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