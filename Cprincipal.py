from tkinter import *
import random
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import Csobre
import Ctiposorteio
import Cmagenta
import Cpreto
from tkinter import ttk
import time, datetime
import getpass
usuario = getpass.getuser()

class Principal:
  #def __init__(self, root):
    #self.root= root
  def __init__(self):
    time.sleep(0.3)
    self.root= Toplevel()
    self.root.title("Aplicativo - Sorteio da ordem Secreta ")
    self.root.iconbitmap(f"C:/Users/{usuario}/sorteio/imagem/icone.ico")
    self.root.resizable(width=False, height=False)
    self.root['bg'] = "#383838" 
    self.largura = 1100
    self.altura = 600
    self.largura_screen = self.root.winfo_screenwidth()
    self.altura_screen = self.root.winfo_screenheight()
  #definir a posição da janela
    self.posX=self.largura_screen/2 - self.largura/2
    self.posy=self.altura_screen/2 - self.altura/2
  #definir a geometria centralizada na tela
    self.root.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
  #criação do fundo
    self.img_fundo_master1= PhotoImage(master=self.root, file=f"C:/Users/{usuario}/sorteio/imagem/telaprincipal.png")
    self.img_botao_1a8= PhotoImage(master=self.root, file=f"C:/Users/{usuario}/sorteio/imagem/botao1a8.png")
    self.img_botao_1a5= PhotoImage(master=self.root, file=f"C:/Users/{usuario}/sorteio/imagem/botao1a5.png")
  #criação de label
    self.lab_fundo_entrada= Label(self.root, image=self.img_fundo_master1)
    self.lab_fundo_entrada.pack()
  #criação de caixas de entrada
  #criação de botões
    self.bt_sorteio1= Button(self.root, bd=0.5, image=self.img_botao_1a8, command= self.sorteio_magenta, cursor="hand2" )
    self.bt_sorteio1.place(width=104, height=104, x=103, y=238)
    self.bt_sorteio2= Button(self.root, bd=0.5, image=self.img_botao_1a5, command= self.sorteio_preto, cursor="hand2")
    self.bt_sorteio2.place(width=104, height=104, x=103, y=430)

#configuração janela principal
    self.meumenu= Menu(self.root)
#ARQUIVOadicionar menu dentro de um menu titulo
    self.fileMenu= Menu(self.meumenu,tearoff=0, background="#383838")
    self.fileMenu.add_command(label="Magenta", command=self.sorteio_magenta)
    self.fileMenu.add_command(label="Preto", command=self.sorteio_preto)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Sair", command=self.root.destroy)
    self.meumenu.add_cascade(label="Sorteio", menu=self.fileMenu )
#EDITARadicionar menu dentro de um menu titulo
    self.editMenu= Menu(self.meumenu, tearoff=0, background="#383838")
    self.editMenu.add_command(label="Tipo de Sorteio", command= self.abrir_janela_tiposorteio)
    self.editMenu.add_command(label="Sobre", command= self.abrir_janela_sobre  )
    self.meumenu.add_cascade(label="Ajuda", menu=self.editMenu)
    self.root.config(menu=self.meumenu) 

  def abrir_janela_sobre(self):
    self.sobre= Csobre.JanelaSobre() 
  def abrir_janela_tiposorteio(self):
    self.tipos= Ctiposorteio.JanelaTiposorteio()
  def sorteio_magenta(self):
    self.sort_magenta= Cmagenta.Magenta()
  def sorteio_preto(self):
    self.sort_preto= Cpreto.Preto()
  

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#root= tk.Tk()
#app = Principal(root)
#root.mainloop()
