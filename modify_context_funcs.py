import json


def list_key_value_dicio(dicio_name: str, skey=True, svalue=True):
    with open("configs/context.json", "r", encoding="utf-8") as file:
        context = json.load(file)
        dicio_names = []
    
    for k in context.keys():
        if "dicio" in k:
            dicio_names.append(k)

    if dicio_name not in dicio_names:
        print("Dicionário inexistente")
        return

    if skey and svalue:
        for k, v in context[dicio_name].items():
            print(f"Chave: {k}; Valor: {v}")
        return

    if skey:
        for k in context[dicio_name].keys():
            print(f"Chave: {k}")
        return

    if svalue:
        for v in context[dicio_name].values():
            print(f"Valor: {v}")
        return


def add_key_value_dicio(dicio_name: str, key: str, value: str):
    with open("configs/context.json", "r", encoding="utf-8") as file:
        context = json.load(file)
        dicio_names = []

    for k in context.keys():
        if "dicio" in k:
            dicio_names.append(k)

    if dicio_name not in dicio_names:
        print("Dicionário inexistente")
        return

    context[dicio_name][key] = value

    with open("configs/context.json", "w", encoding="utf-8") as file:
        json.dump(context, file, ensure_ascii=False, indent=4)


def remove_key_dicio(dicio_name: str, key: str):
    with open("configs/context.json", "r", encoding="utf-8") as file:
        context = json.load(file)
        dicio_names = []

    for k in context.keys():
        if "dicio" in k:
            dicio_names.append(k)
    
    if dicio_name not in dicio_names:
        print("Dicionário inexistente")
        return

    if key not in context[dicio_name]:
        print("Chave inexistente")
        return

    removed_key = context[dicio_name].pop(key)

    with open("configs/context.json", "w", encoding="utf-8") as file:
        json.dump(context, file, ensure_ascii=False, indent=4)

    print(f"keyeto de valor: \"{removed_key}\" removida")

