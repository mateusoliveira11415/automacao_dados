def replace_placeholders(text_string:str, range_value:int, infor: list):
    text = text_string

    for i in range(range_value):
        text = text.replace(f".{i}.", infor[i])

    return text, infor[range_value:]

