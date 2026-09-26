import write_functions as wfuncs

wfuncs.initialize_model_shortcut(1)

with open("encoded_data.txt", "r", encoding="utf-8") as arquivo:
    data_list = arquivo.readlines()
    for linha in data_list:
        linha = linha.strip()

        match linha[0]:
            case c:
                if c.isdigit():
                    wfuncs.render_simple_compound(linha)
                    continue
                if c.islower():
                    wfuncs.render_complex(linha)
                    continue
