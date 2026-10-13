import customtkinter as ctk
from auto_process import process_prior_data as prior
import modify_context as mdfy_ctx

previa_label: ctk.CTkLabel
mostrar_previa_button: ctk.CTkButton

campos_entrada: list[ctk.CTkEntry] = []


relacao_dicio = {
    "Dicionário simples": "simple_dicio",
    "Dicionário composto": "compound_dicio",
    "Dicionário complexo": "complex_dicio"
}


def trocar_aba(aba_atual:ctk.CTkFrame, proxima_aba:ctk.CTkFrame):
    aba_atual.pack_forget()
    proxima_aba.pack()


def select_dicio(nome_dicionario:str, select_key:ctk.CTkOptionMenu):
    dicio_name = relacao_dicio[nome_dicionario]
    list_key = mdfy_ctx.list_key_value_dicio(dicio_name)
    select_key.configure(values=list_key)
    select_key.set("")

    renderizar_opcoes(dicio_name)


def renderizar_opcoes(nome_dicionario:str):
    if nome_dicionario == "simple_dicio":
        print("Dicionário simples selecionado")
        return
    if nome_dicionario == "compound_dicio":
        print("Dicionário composto selecionado")
        return
    print("Dicionário complexo selecionado")


def codificar_mensagem(dicio_name: str, primary_key: str, frame:ctk.CTkFrame):
    global campos_entrada
    match dicio_name:
        case "Dicionário simples":
            frame.grid_forget()
            codigo = f"0,{primary_key}"
            mostrar_previa(codigo)
            mostrar_previa_button.grid_forget()

        case "Dicionário composto":
            frame.grid(
                row=5,
                column=0,
                sticky="w",
                padx=12,
                pady=5
            )
            renderizar_campos_compostos(
                primary_key,
                frame
            )
            mostrar_previa_composta(primary_key)

        case "Dicionário complexo":
            print("Dicionário complexo na codificação atual")


def mostrar_previa(codigo_da_previa):
    resultado = prior.recieve_prior(codigo_da_previa)
    previa_label.configure(text=resultado)


def mostrar_previa_composta(primary_key:str):
    global campos_entrada

    valores = [campo.get() if campo.get().strip() else "X" for campo in campos_entrada]
    codigo = ",".join([
        primary_key,
        str(len(valores)),
        *valores
    ])
    mostrar_previa(codigo)


def renderizar_campos_compostos(primary_key: str,frame: ctk.CTkFrame):
    global campos_entrada

    for widget in frame.winfo_children():
        widget.destroy()

    campos_entrada.clear()

    dicios = mdfy_ctx.list_key_value_dicio(
        "compound_dicio",
        True,
        True
    )

    quantidade_campos = dicios[primary_key][1]

    for i in range(quantidade_campos):

        label = ctk.CTkLabel(
            frame,
            text=f"Dado {i + 1}"
        )

        label.grid(
            row=i,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        entrada = ctk.CTkEntry(
            frame,
            placeholder_text=f"Digite o dado {i + 1}"
        )

        entrada.grid(
            row=i,
            column=1,
            sticky="w",
            padx=5,
            pady=5
        )

        campos_entrada.append(entrada)

        mostrar_previa_button.grid(
            row=6,
            column=0,
            sticky="w",
            padx=12,
            pady=12
        )