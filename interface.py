import customtkinter as ctk
import interface_functions as ifuncs
import read_preferences as rdp


root = ctk.CTk()


root.geometry("400x300")
root.title("Fox Scriptor")


ctk.CTkLabel(
    root,
    text="Fox Scriptor",
    font=("Arial", 24)
).pack(pady=20)


root_selecoes = ctk.CTkFrame(
    root,
    width=200,
    height=200
)
root_selecoes.pack(pady=10)

ctk.CTkButton(
    root_selecoes,
    text="Inserir linha",
    command=lambda: ifuncs.trocar_aba(root_selecoes, root_inserir_linha),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(
    row=0,
    column=0
)


root_inserir_linha = ctk.CTkFrame(
    root,
    width=800,
    height=800
)
root_inserir_linha.grid_propagate(False)


ctk.CTkLabel(
    root_inserir_linha,
    text="Inserir linha",
    font=("Arial", 20)
).grid(
    row=0,
    column=0,
    sticky="w",
    padx=12,
    pady=12
)

ctk.CTkLabel(
    root_inserir_linha,
    text="Selecionar dicionário",
    font=("Arial", 16)
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=12
)

selecionar_dicionario = ctk.CTkOptionMenu(
    root_inserir_linha,
    values=[
        "Dicionário simples",
        "Dicionário composto",
        "Dicionário complexo"
    ],
    command=lambda nome_dicionario: ifuncs.select_dicio(nome_dicionario, selecionar_chave),
    fg_color=rdp.button_color,
    button_color=rdp.button_color,
    button_hover_color=rdp.button_hover_color
)
selecionar_dicionario.grid(
    row=2,
    column=0,
    sticky="w",
    padx=12,
    pady=(0, 12)
)

ctk.CTkLabel(
    root_inserir_linha,
    text="Selecionar chave primária",
    font=("Arial", 16)
).grid(
    row=3,
    column=0,
    sticky="w",
    padx=12
)
selecionar_chave = ctk.CTkOptionMenu(
    root_inserir_linha,
    values=[],
    fg_color=rdp.button_color,
    button_color=rdp.button_color,
    button_hover_color=rdp.button_hover_color
)
selecionar_chave.grid(
    row=4,
    column=0,
    sticky="w",
    padx=12,
    pady=(0, 12)
)

ctk.CTkButton(
    root_inserir_linha,
    text="Voltar",
    command=lambda: ifuncs.trocar_aba(root_inserir_linha, root_selecoes),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(
    row=10,
    column=0,
    sticky="w",
    padx=12
)

ctk.CTkButton(
    root_inserir_linha,
    text="Voltar",
    command=lambda: ifuncs.trocar_aba(root_inserir_linha, root_selecoes),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(
    row=10,
    column=0,
    sticky="w",
    padx=12
)

ctk.CTkButton(
    root_inserir_linha,
    text="Registrar linha",
    command=lambda: print("Clicaram em mim"),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(
    row=10,
    column=0,
    sticky="w",
    padx=12,
    pady=12
)

ctk.CTkButton(
    root_inserir_linha,
    text="Voltar",
    command=lambda: ifuncs.trocar_aba(root_inserir_linha, root_selecoes),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(
    row=10,
    column=1,
    sticky="w",
    padx=12
)


root.mainloop()