import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("SuperApp")
janela.iconbitmap("superappicon.ico")
janela.resizable(False, False)

# TRABALHANDO COM A IMAGEM DA TELA
img = PhotoImage(file="superapp.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

label_tt = customtkinter.CTkLabel(master=janela, text="Entre na sua conta e tenha\n acesso a todos os dados da plataforma",
font=("Roboto", 18), text_color="white")
label_tt.place(x=10, y=10)


# FRAME
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

# WIDGETS DENTRO DO FRAME
label = customtkinter.CTkLabel(master=frame, text="Sistema de login", font=("Roboto", 25))
label.place(x=100, y=20)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome do usuário", width=300, font=("Roboto", 14))
entry1.place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text="Nome de usuário é de carácter obrigatório.", text_color="green", font=("Roboto", 14))
label1.place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha do usuário", width=300, font=("Roboto", 14))
entry2.place(x=25, y=175)
label2 = customtkinter.CTkLabel(master=frame, text="Senha é de caráter obrigatório.", text_color="green", font=("Roboto", 14))
label2.place(x=25, y=205)

chekbox = customtkinter.CTkCheckBox(master=frame, text="Lembrar do meu usuário e senha").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=285)

janela.mainloop()
