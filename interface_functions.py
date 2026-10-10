import customtkinter as ctk


def trocar_aba(aba_atual:ctk.CTkFrame, proxima_aba:ctk.CTkFrame):
    aba_atual.pack_forget()
    proxima_aba.pack()