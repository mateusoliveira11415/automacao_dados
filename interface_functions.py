import customtkinter as ctk
from auto_process import process_prior_data as prior
import modify_context as mdc

previa_label: ctk.CTkLabel

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
    list_key = mdc.list_key_value_dicio(dicio_name)
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


def codificar_mensagem(dicio_name: str, primary_key: str):
    match dicio_name:
        case "Dicionário simples":
            codigo = f"0,{primary_key}"
            print("Código gerado:", codigo)
            mostrar_previa(codigo)


def mostrar_previa(codigo_da_previa):
    print("Código recebido:", codigo_da_previa)

    resultado = prior.recieve_prior(codigo_da_previa)
    print("Resultado recebido:", repr(resultado))

    previa_label.configure(text=resultado)