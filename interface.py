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
).grid(row=0, column=0)


root_inserir_linha = ctk.CTkFrame(
    root,
    width=200,
    height=200
)


ctk.CTkLabel(
    root_inserir_linha,
    text="Inserir linha",
    font=("Arial", 16)
).grid(row=0, column=0, sticky="w")

ctk.CTkButton(
    root_inserir_linha,
    text="Voltar",
    command=lambda: ifuncs.trocar_aba(root_inserir_linha, root_selecoes),
    fg_color=rdp.button_color,
    hover_color=rdp.button_hover_color
).grid(row=0, column=0)


root.mainloop()