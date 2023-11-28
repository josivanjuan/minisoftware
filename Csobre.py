from tkinter import *
import tkinter as tk
import time, datetime
from PIL import Image, ImageTk
import os
import getpass
usuario = getpass.getuser()
#pastaapp= os.path.dirname(__file__)
#class JanelaSobre:
 #   def __init__(self):#, root, titulo, largura, altura): #construtor que cria a funcionalidade incial da classe
  #      time.sleep(0.4)
        #self.janelasobre= Toplevel()
            #conteudo da janela
class JanelaSobre:
    def __init__(self):#, root, titulo, largura, altura): #construtor que cria a funcionalidade incial da classe
        time.sleep(0.4)
        self.janelasobre= Toplevel()
        self.janelasobre.title("Detalhes sobre o aplicativo e desenvolvedor")
        self.janelasobre.iconbitmap(f'C:/Users/{usuario}/minisoftware/imagem/icone.ico')
        self.janelasobre.resizable(width=False, height=False)
        self.janelasobre['bg'] = "#383838"
        self.largura= 490
        self.altura= 560
        self.larguratela= self.janelasobre.winfo_screenwidth()
        self.alturatela= self.janelasobre.winfo_screenheight()
        self.posX=self.larguratela/2 - self.largura/2
        self.posy=self.alturatela/2 - self.altura/2
        self.janelasobre.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
        self.img_fundo_tiposorteio= PhotoImage(master=self.janelasobre, file=(f"C:/Users/{usuario}/minisoftware/imagem/topsobre.png"))
        self.lab_fundo_topsobre= Label(self.janelasobre, image=self.img_fundo_tiposorteio)
        self.lab_fundo_topsobre.pack()
        self.lab_fundo_mensagem= Label(self.janelasobre, font=('monospace', 9), text="Sugestões e relatos de panes:\n josivanjuan@gmail.com",bg="#ff751a", fg="#FFFFFF")
        self.lab_fundo_mensagem.place(width=200, height=30, x=145, y=480)
        self.label_hora= Label(self.janelasobre, text="", font=('monospace', 8),bg="#ff751a", fg="#FFFFFF")
        self.label_hora.place(width=200, height=30, x=145, y=510)
        self.exibir_hora_atual()
        

    def exibir_hora_atual(self):   
        self.hora_atual= datetime.datetime.now().strftime("%H:%M:%S")
        self.label_hora.config(text=f"Hora atual: {self.hora_atual}")
        self.janelasobre.after(1000, self.exibir_hora_atual)


    
#root= Tk()
#objetojanela1= JanelaPadrao(root, "Sorteio da ordem Secreta", 560, 490)
#objetojanela1.criarjanela()
#root.mainloop()

