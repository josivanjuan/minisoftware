import tkinter as tk
from tkinter import filedialog
import getpass
usuario= getpass.getuser()

import tkinter as tk
from tkinter import filedialog
import os

def abrir_pdf():
    # Obtém o caminho do arquivo PDF
    caminho_arquivo = entrada_caminho.get()

    # Verifica se o caminho é válido
    if os.path.exists(caminho_arquivo) and caminho_arquivo.lower().endswith('.pdf'):
        # Abre o arquivo PDF com o programa padrão
        os.system(f'start {caminho_arquivo}')
    else:
        # Exibe uma mensagem de erro se o caminho não for válido
        lbl_status["text"] = "Caminho inválido ou arquivo não é PDF"

# Função para selecionar o arquivo PDF
def selecionar_arquivo():
    # Abre a caixa de diálogo para seleção de arquivo
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])

    # Atualiza o texto na entrada de caminho
    entrada_caminho.delete(0, tk.END)
    entrada_caminho.insert(0, caminho_arquivo)

# Criando a janela principal
janela = tk.Tk()
janela.title("Abrir Arquivo PDF")

# Criando widgets
lbl_instrucao = tk.Label(janela, text="Insira o caminho do arquivo PDF:")
entrada_caminho = tk.Entry(janela, width=50)
btn_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_abrir = tk.Button(janela, text="Abrir PDF", command=abrir_pdf)
lbl_status = tk.Label(janela, text="")

# Posicionando widgets na janela
lbl_instrucao.grid(row=0, column=0, columnspan=3, pady=10)
entrada_caminho.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
btn_selecionar.grid(row=1, column=2, pady=10)
btn_abrir.grid(row=2, column=0, columnspan=3, pady=10)
lbl_status.grid(row=3, column=0, columnspan=3)

# Iniciando o loop principal da aplicação
janela.mainloop()