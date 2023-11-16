from tkinter import *
import tkinter as tk
import time, datetime
from PIL import Image, ImageTk
import random
from Csorteio import OrdemSecreta
import getpass
usuario = getpass.getuser()

class Preto:  
  def __init__(self):
    time.sleep(0.3)
    self.preto= Toplevel()
    self.preto.title("Aplicativo - Sorteio da ordem Secreta - Completo")
    self.preto.iconbitmap(f'C:/Users/{usuario}/sorteio/imagem/icone.ico')
    self.preto.resizable(width=False, height=False)
    self.preto['bg'] = "#383838" 
    self.largura = 1000
    self.altura = 500
    self.largura_screen = self.preto.winfo_screenwidth()
    self.altura_screen = self.preto.winfo_screenheight()
  #definir a posição da janela
    self.posX=self.largura_screen/2 - self.largura/2
    self.posy=self.altura_screen/2 - self.altura/2
  #definir a geometria centralizada na tela
    self.preto.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
  #criação do fundo
    self.img_fundo_preto= PhotoImage(master=self.preto, file=f"C:/Users/{usuario}/sorteio/imagem/telasorteiopreto.png")
    self.img_botao_sortear= PhotoImage(master=self.preto, file=f"C:/Users/{usuario}/sorteio/imagem/botaosortear.png")
    self.img_botao_apagar= PhotoImage(master=self.preto, file=f"C:/Users/{usuario}/sorteio/imagem/apagar.png")
    self.img_botao_sair= PhotoImage(master=self.preto, file=f"C:/Users/{usuario}/sorteio/imagem/botaosair.png")
   
  #criação de label
    self.lab_fundo_entrada= Label(self.preto, image=self.img_fundo_preto)
    self.lab_fundo_entrada.pack()

    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio1)
    self.bt_sortear.place(width=64, height=64, x=120, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio2)
    self.bt_sortear.place(width=64, height=64, x=230, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio3)
    self.bt_sortear.place(width=64, height=64, x=340, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio4)
    self.bt_sortear.place(width=64, height=64, x=450, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio5)
    self.bt_sortear.place(width=64, height=64, x=560, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio6)
    self.bt_sortear.place(width=64, height=64, x=670, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio7)
    self.bt_sortear.place(width=64, height=64, x=780, y=108)
    self.bt_sortear= Button(self.preto, bd=0.5, image=self.img_botao_sortear, command= self.realizarsorteio8)
    self.bt_sortear.place(width=64, height=64, x=890, y=108)
    self.bt_apagar= Button(self.preto, bd=0.5, image=self.img_botao_apagar, command=self.apagartudo)
    self.bt_apagar.place(width=40, height=40, x=890, y=20)
    self.bt_sair= Button(self.preto, bd=0.5, image=self.img_botao_sair, command=self.preto.destroy)
    self.bt_sair.place(width=40, height=40, x=940, y=20)

#caixa escolher dia
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=95, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=207, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=318, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=430, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=541, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=653, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=765, y=459)
    self.dias= Spinbox(self.preto, values=("Selecione o Dia", "   1º Dia   ", "   2º Dia   ", "   3º Dia   ", "   4º Dia   ", "   5º Dia   "))
    self.dias.place(width=100, height=20, x=877, y=459)

#criação das saidas de textos do sorteio
#medio 1
    self.medio1fem = Label(self.preto, text="", font="monospace 10 bold")
    self.medio1fem.place(width=106, height=105, x=93, y=212)
    self.medio1mas = Label(self.preto, text="", font="monospace 10 bold")
    self.medio1mas.place(width=106, height=105, x=93, y=338)
#medio 2
    self.medio2fem = Label(self.preto, text="", font="monospace 10 bold")
    self.medio2fem.place(width=106, height=105, x=204, y=212)
    self.medio2mas = Label(self.preto, text="", font="monospace 10 bold")
    self.medio2mas.place(width=106, height=105, x=204, y=338)
#longo 1
    self.longo1fem = Label(self.preto, text="", font="monospace 10 bold")
    self.longo1fem.place(width=106, height=105, x=315, y=212)
    self.longo1mas = Label(self.preto, text="", font="monospace 10 bold")
    self.longo1mas.place(width=106, height=105, x=315, y=338)
#longo 2
    self.longo2fem = Label(self.preto, text="", font="monospace 10 bold")
    self.longo2fem.place(width=106, height=105, x=426, y=212)
    self.longo2mas = Label(self.preto, text="", font="monospace 10 bold")
    self.longo2mas.place(width=106, height=105, x=426, y=338)
#medio 3
    self.medio3fem = Label(self.preto, text="", font="monospace 10 bold")
    self.medio3fem.place(width=106, height=105, x=537, y=212)
    self.medio3mas = Label(self.preto, text="", font="monospace 10 bold")
    self.medio3mas.place(width=106, height=105, x=537, y=338)
#medio 4
    self.medio4fem = Label(self.preto, text="", font="monospace 10 bold")
    self.medio4fem.place(width=106, height=105, x=648, y=212)
    self.medio4mas = Label(self.preto, text="", font="monospace 10 bold")
    self.medio4mas.place(width=106, height=105, x=648, y=338)
#longo 3
    self.longo3fem = Label(self.preto, text="", font="monospace 10 bold")
    self.longo3fem.place(width=106, height=105, x=759, y=212)
    self.longo3mas = Label(self.preto, text="", font="monospace 10 bold")
    self.longo3mas.place(width=106, height=105, x=759, y=338)
#longo 4
    self.longo4fem = Label(self.preto, text="", font="monospace 10 bold")
    self.longo4fem.place(width=106, height=105, x=870, y=212)
    self.longo4mas = Label(self.preto, text="", font="monospace 10 bold")
    self.longo4mas.place(width=106, height=105, x=870, y=338)  
# funções de sorteio
  def realizarsorteio1(self):
      sorteio1= OrdemSecreta.executarsorteio(self)
      sorteio11= OrdemSecreta.executarsorteio(self)
      self.medio1fem.config(text=f"{sorteio1}")
      self.medio1mas.config(text=f"{sorteio11}")
  def realizarsorteio2(self):
      sorteio2= OrdemSecreta.executarsorteio(self)
      sorteio22= OrdemSecreta.executarsorteio(self)
      self.medio2fem.config(text=f"{sorteio2}")
      self.medio2mas.config(text=f"{sorteio22}")
  def realizarsorteio3(self):
      sorteio3= OrdemSecreta.executarsorteio(self)
      sorteio33= OrdemSecreta.executarsorteio(self)
      self.longo1fem.config(text=f"{sorteio3}")
      self.longo1mas.config(text=f"{sorteio33}")
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
  def realizarsorteio6(self):
      sorteio6= OrdemSecreta.executarsorteio(self)
      sorteio66= OrdemSecreta.executarsorteio(self)
      self.medio4fem.config(text=f"{sorteio6}")
      self.medio4mas.config(text=f"{sorteio66}")
  def realizarsorteio7(self):
      sorteio7= OrdemSecreta.executarsorteio(self)
      sorteio77= OrdemSecreta.executarsorteio(self)
      self.longo3fem.config(text=f"{sorteio7}")
      self.longo3mas.config(text=f"{sorteio77}")
  def realizarsorteio8(self):
      sorteio8= OrdemSecreta.executarsorteio(self)
      sorteio88= OrdemSecreta.executarsorteio(self)
      self.longo4fem.config(text=f"{sorteio8}")
      self.longo4mas.config(text=f"{sorteio88}")
#apagar---------------------------------
  def apagartudo(self):
      apagar= OrdemSecreta.apagarsorteio(self)
      self.medio1fem.config(text=f"{apagar}")
      self.medio1mas.config(text=f"{apagar}")
      self.medio2fem.config(text=f"{apagar}")
      self.medio2mas.config(text=f"{apagar}")
      self.longo1fem.config(text=f"{apagar}")
      self.longo1mas.config(text=f"{apagar}")
      self.longo2fem.config(text=f"{apagar}")
      self.longo2mas.config(text=f"{apagar}")
      self.medio3fem.config(text=f"{apagar}")
      self.medio3mas.config(text=f"{apagar}")
      self.medio4fem.config(text=f"{apagar}")
      self.medio4mas.config(text=f"{apagar}")
      self.longo3fem.config(text=f"{apagar}")
      self.longo3mas.config(text=f"{apagar}")
      self.longo4fem.config(text=f"{apagar}")
      self.longo4mas.config(text=f"{apagar}")
