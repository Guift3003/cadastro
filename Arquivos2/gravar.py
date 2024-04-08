import csv
import os
import tkinter as tk
from tkinter import messagebox


def excluir():

    resposta = messagebox.askokcancel("Excluir contato", "Tem certeza de que deseja excluir o contato selecionado ?")

    if resposta:
        with open("temp.csv", "a", newline="") as arquivo_temporario, open("dados.csv", "r") as arquivo_dados:
            escritor = csv.writer(arquivo_temporario)
            leitor = csv.reader(arquivo_dados)
            for i in leitor:
                if (i[0] != entry_nome.get()) and (i[1] != entry_fone.get()) and (i[2] != entry_email):
                    escritor.writerow([i[0], i[1], i[2]])

        os.replace("temp.csv", "dados.csv")
        ler_contatos()

    else:
        messagebox.showinfo("Excluir contato", "Operação cancelada pelo usuário")








def gravar_contato():

    if (entry_nome.get() == "") or (entry_fone.get() == "") or (entry_email.get() == ""):
        messagebox.showerror("Erro ao gravar", "Todos os campos devem ser preenchidos")

    else:
        with open("dados.csv", "a", newline="") as arquivo_dados:
            escritor = csv.writer(arquivo_dados)
            escritor.writerow([entry_nome.get().strip(), entry_fone.get().strip(), entry_email.get().strip()])
            messagebox.showinfo("Sistema contatos", "Contato cadasctrado com sucesso")
            limpar_campos()

    ler_contatos()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_fone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome.focus_set()

def ler_contatos():
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        lista_contatos.delete(0, tk.END) #Limpar a lista
        for linha in leitor:
            lista_contatos.insert("end", linha[0])


def buscar_contato_pelo_indice(indice_procurado):
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        volta = 0
        for linha in leitor:
            if volta == indice_procurado:
                entry_nome.insert(tk.END, linha[0])
                entry_fone.insert(tk.END, linha[1])
                entry_email.insert(tk.END, linha[2])
                break
            volta = volta + 1



def obter_indice(event):
    indice = lista_contatos.curselection()[0]
    limpar_campos()
    buscar_contato_pelo_indice(indice)




janela = tk.Tk()

janela.geometry("580x300")

label_nome = tk.Label(janela, text="Nome: ")
label_fone = tk.Label(janela, text="Telefone: ")
label_email = tk.Label(janela, text="E-mail: ")
label_contatos = tk.Label(janela, text="Contatos:")

entry_nome = tk.Entry(janela)
entry_fone = tk.Entry(janela)
entry_email = tk.Entry(janela)

button_gravar = tk.Button(text="Salvar", command=gravar_contato)
button_excluir = tk.Button(text="Excluir", command=excluir)

lista_contatos = tk.Listbox(janela, selectmode="single")
lista_contatos.bind("<<ListboxSelect>>", obter_indice)


label_nome.place(x=10, y=10)
entry_nome.place(x=10, y=40, width=300, height=30)
label_nome.config(font=("Arial", 16))
entry_nome.config(font=("Arial", 16))

label_fone.place(x=10, y=80)
entry_fone.place(x=10, y=110, width=300, height=30)
label_fone.config(font=("Arial", 16))
entry_fone.config(font=("Arial", 16))

label_email.place(x=10, y=150)
entry_email.place(x=10, y=180, width=300, height=30)
label_email.config(font=("Arial", 16))
entry_email.config(font=("Arial", 16))


button_gravar.place(x=10, y=220, width=150, height=40)
button_gravar.config(font=("Arial", 13))

button_excluir.place(x=160, y=220, width=150, height=40)
button_excluir.config(font=("Arial", 13))

lista_contatos.place(x=320, y=40, width=250)
lista_contatos.config(font=("Arial", 16))


label_contatos.place(x=320, y=10)
label_contatos.config(font=("Arial", 16))

ler_contatos()









janela.mainloop()





