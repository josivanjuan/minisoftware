from tkinter import *
from tkinter import filedialog
import time
import tkinter as tk
from tkinter import ttk
import Cprincipal
import getpass
usuario = getpass.getuser()
#local= f"C:/Users/{usuario}/sorteio/imagem/"

#configuração da janela MASTER
    #root= Tk()
def abrir_jan_principal():
    #root.quit()
    principal= Cprincipal.Principal()
    
root= Tk()    

root.title("Orientação - Sorteio da ordem Secreta")
root.iconbitmap(f"C:/Users/{usuario}/sorteio/imagem/icone.ico")
root.resizable(width=False, height=False)
root['bg'] = "#383838"
largura = 490
altura = 560
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
  #definir a posição da janela
posX=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2
  #definir a geometria centralizada na tela
root.geometry("%dx%d+%d+%d" % (largura, altura, posX, posy))
    #importar imagens
img_fundo_entrada= PhotoImage(master=root, file=f"C:/Users/{usuario}/sorteio/imagem/telaentrada.png")
img_botao_entrada= PhotoImage(master=root, file=f"C:/Users/{usuario}/sorteio/imagem/botaoentrar.png")
#criação de label
lab_fundo_entrada= Label(root, image=img_fundo_entrada)
lab_fundo_entrada.pack()
#criação de caixas de entrada
#criação de botões
bt_entrar= Button(root, bd=0, image=img_botao_entrada, command= abrir_jan_principal)
bt_entrar.place(width=118, height=64, x=186, y=308)
  #variáveis globais
  # funções
#executar mainloop
#app=root
root.mainloop()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""class Login:
  def __init__(self, root):
    self.root= root
#configuração da janela MASTER
    #root= Tk()
    self.root.title("Orientação - Sorteio da ordem Secreta")
    self.root.iconbitmap('0_extras/janelalogin/imagem/icone.ico')
    self.root.resizable(width=False, height=False)
    self.root['bg'] = "#383838"
    self.largura = 490
    self.altura = 560
    self.largura_screen = root.winfo_screenwidth()
    self.altura_screen = root.winfo_screenheight()
  #definir a posição da janela
    self.posX=self.largura_screen/2 - self.largura/2
    self.posy=self.altura_screen/2 - self.altura/2
  #definir a geometria centralizada na tela
    self.root.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
    #importar imagens
    self.img_fundo_entrada= PhotoImage(file="0_extras/janelalogin/imagem/telaentrada.png")
    self.img_botao_entrada= PhotoImage(file="0_extras/janelalogin/imagem/botaoentrar.png")
#criação de label
    self.lab_fundo_entrada= Label(self.root, image=self.img_fundo_entrada)
    self.lab_fundo_entrada.pack()
#criação de caixas de entrada
#criação de botões
    self.bt_entrar= Button(self.root, bd=0, image=self.img_botao_entrada, command= self.abrir_jan_principal)
    self.bt_entrar.place(width=118, height=64, x=186, y=308)
  #variáveis globais
  # funções
  def abrir_jan_principal(self):
    #self.root.destroy()
    self.principal= Cprincipal.Principal()
    #exec(open("0_extras/janelalogin/Cprincipal.py").read())"""