from tkinter import *
import time
import tkinter as tk
from PIL import Image, ImageTk
import getpass
usuario = getpass.getuser()

class JanelaTiposorteio:
    def __init__(self):#, root, titulo, largura, altura): #construtor que cria a funcionalidade incial da classe
        
        time.sleep(0.4)
        self.tiposorteio= Toplevel()
        self.tiposorteio.title("Ajuda sobre Sorteios")
        self.tiposorteio.iconbitmap(f"C:/Users/{usuario}/sorteio/imagem/icone.ico")
        self.tiposorteio.resizable(width=False, height=False)
        self.tiposorteio['bg'] = "#383838" 
        self.largura= 450
        self.altura= 270
        self.larguratela= self.tiposorteio.winfo_screenwidth()
        self.alturatela= self.tiposorteio.winfo_screenheight()
        self.posX=self.larguratela/2 - self.largura/2
        self.posy=self.alturatela/2 - self.altura/2
        self.tiposorteio.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
        self.lab_fundo_mensagem= Message(self.tiposorteio, font=('monospace', 10), text="Há dois tipos de sorteios:\n  1 - Magenta - percursos Médio-Longo alternados\n  2 - Preto - percursos Médio-Médio-Longo-Longo alternados\n\nClique no botão da cor desejada para mostrar as telas de Painel de Sorteio.\n\nAs telas contém os tipos de sorteios disponíveis para esta versão.\n\nRecomenda-se realizar demonstração de sorteio, clicando diversas vezes nos botões sortear e usando a lixeira para apagar, antes do sorteio definitivo. E ainda não fechar a janela para realizar o sorteio definitivo. Isso significará maior aleatoriedade no sorteio definitivo")
        self.lab_fundo_mensagem.place(width=450, height=270)
     


