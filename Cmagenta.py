from tkinter import *
import tkinter as tk
import time, datetime
from PIL import Image, ImageTk
import random
from Csorteio import OrdemSecreta

class Magenta:  
  def __init__(self):
    time.sleep(0.3)
    self.magenta= Toplevel()
    self.magenta.title("Aplicativo - Sorteio da ordem Secreta - Simplificado")
    self.magenta.iconbitmap('C:/Users/josivanjuan/Documents/PYTHON/0_extras/janelalogin/imagem/icone.ico')
    self.magenta.resizable(width=False, height=False)
    self.magenta['bg'] = "#383838" 
    self.largura = 700
    self.altura = 500
    self.largura_screen = self.magenta.winfo_screenwidth()
    self.altura_screen = self.magenta.winfo_screenheight()
  #definir a posição da janela
    self.posX=self.largura_screen/2 - self.largura/2
    self.posy=self.altura_screen/2 - self.altura/2
  #definir a geometria centralizada na tela
    self.magenta.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
  #criação do fundo
    self.img_fundo_magenta= PhotoImage(master=self.magenta, file="C:/Users/josivanjuan/Documents/PYTHON/0_extras/janelalogin/imagem/telasorteiomagenta.png")
    self.img_botao_sortear= PhotoImage(master=self.magenta, file="C:/Users/josivanjuan/Documents/PYTHON/0_extras/janelalogin/imagem/botaosortear.png")
    self.img_botao_apagar= PhotoImage(master=self.magenta, file="C:/Users/josivanjuan/Documents/PYTHON/0_extras/janelalogin/imagem/apagar.png")
    self.img_botao_sair= PhotoImage(master=self.magenta, file="C:/Users/josivanjuan/Documents/PYTHON/0_extras/janelalogin/imagem/botaosair.png")
   
  #criação de label
    self.lab_fundo_entrada= Label(self.magenta, image=self.img_fundo_magenta)
    self.lab_fundo_entrada.pack()
 
  #criação de botões
    self.bt_sortear= Button(self.magenta, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio1, cursor="hand2")
    self.bt_sortear.place(width=64, height=64, x=115, y=108)
    self.bt_sortear= Button(self.magenta, bd=0.5, image=self.img_botao_sortear, command=self.realizarsorteio2, cursor="hand2")
    self.bt_sortear.place(width=64, height=64, x=235, y=108)
    self.bt_sortear= Button(self.magenta, bd=0.5, image=self.img_botao_sortear, command=self.realizarsorteio3, cursor="hand2")
    self.bt_sortear.place(width=64, height=64, x=355, y=108)
    self.bt_sortear= Button(self.magenta, bd=0.5, image=self.img_botao_sortear, command=self.realizarsorteio4, cursor="hand2")
    self.bt_sortear.place(width=64, height=64, x=475, y=108)
    self.bt_sortear= Button(self.magenta, bd=0.5, image=self.img_botao_sortear, command=self.realizarsorteio5, cursor="hand2")
    self.bt_sortear.place(width=64, height=64, x=595, y=108)
    self.bt_apagar= Button(self.magenta, bd=0.5, image=self.img_botao_apagar, command=self.apagartudo, cursor="hand2")
    self.bt_apagar.place(width=40, height=40, x=600, y=29)
    self.bt_sair= Button(self.magenta, bd=0.5, image=self.img_botao_sair, command=self.magenta.destroy, cursor="hand2")
    self.bt_sair.place(width=40, height=40, x=643, y=29)
    

#criação das saidas de textos do sorteio
#caixa escolher dia
    self.dias= Spinbox(self.magenta, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=108, height=20, x=92, y=435)
    self.dias= Spinbox(self.magenta, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=108, height=20, x=212, y=435)
    self.dias= Spinbox(self.magenta, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=108, height=20, x=334, y=435)
    self.dias= Spinbox(self.magenta, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=108, height=20, x=456, y=435)
    self.dias= Spinbox(self.magenta, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=93, height=20, x=576, y=435)
#longo 1
#longo 1
#medio 1
    self.medio1fem = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio1fem.place(width=108, height=85, x=92, y=220)
    self.medio1mas = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio1mas.place(width=108, height=85, x=92, y=340)
    
    self.longo1fem = Label(self.magenta, text="", font="monospace 10 bold")
    self.longo1fem.place(width=108, height=85, x=212, y=340)
    self.longo1mas = Label(self.magenta, text="", font="monospace 10 bold")
    self.longo1mas.place(width=108, height=85, x=212, y=220)
#medio 2
    self.medio2fem = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio2fem.place(width=108, height=85, x=334, y=220)
    self.medio2mas = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio2mas.place(width=108, height=85, x=334, y=340)
#longo 2
    self.longo2fem = Label(self.magenta, text="", font="monospace 10 bold")
    self.longo2fem.place(width=108, height=85, x=454, y=340)
    self.longo2mas = Label(self.magenta, text="", font="monospace 10 bold")
    self.longo2mas.place(width=108, height=85, x=454, y=220)
#medio 3
    self.medio3fem = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio3fem.place(width=108, height=85, x=574, y=220)
    self.medio3mas = Label(self.magenta, text="", font="monospace 10 bold")
    self.medio3mas.place(width=108, height=85, x=574, y=340)

  def realizarsorteio1(self):
      sorteio1= OrdemSecreta.executarsorteio(self)
      sorteio11= OrdemSecreta.executarsorteio(self)
      self.medio1fem.config(text=f"{sorteio1}")
      self.medio1mas.config(text=f"{sorteio11}")
  def realizarsorteio2(self):
      sorteio2= OrdemSecreta.executarsorteio(self)
      sorteio22= OrdemSecreta.executarsorteio(self)
      self.longo1fem.config(text=f"{sorteio2}")
      self.longo1mas.config(text=f"{sorteio22}")
  def realizarsorteio3(self):
      sorteio3= OrdemSecreta.executarsorteio(self)
      sorteio33= OrdemSecreta.executarsorteio(self)
      self.medio2fem.config(text=f"{sorteio3}")
      self.medio2mas.config(text=f"{sorteio33}")
  def realizarsorteio4(self):
      sorteio4= OrdemSecreta.executarsorteio(self)
      sorteio44= OrdemSecreta.executarsorteio(self)
      self.longo2fem.config(text=f"{sorteio4}")
      self.longo2mas.config(text=f"{sorteio44}")
  def realizarsorteio5(self):
      sorteio5= OrdemSecreta.executarsorteio(self)
      sorteio55= OrdemSecreta.executarsorteio(self)
      self.medio3fem.config(text=f"{sorteio5}")
      self.medio3mas.config(text=f"{sorteio55}")
# apagar ----------------------------------------------------------------------
  def apagartudo(self):
      apagar= OrdemSecreta.apagarsorteio(self)
      self.medio1fem.config(text=f"{apagar}")
      self.medio1mas.config(text=f"{apagar}")
      self.longo1fem.config(text=f"{apagar}")
      self.longo1mas.config(text=f"{apagar}")
      self.medio2fem.config(text=f"{apagar}")
      self.medio2mas.config(text=f"{apagar}")
      self.longo2fem.config(text=f"{apagar}")
      self.longo2mas.config(text=f"{apagar}")
      self.medio3fem.config(text=f"{apagar}")
      self.medio3mas.config(text=f"{apagar}")     
