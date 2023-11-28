from tkinter import *
from tkinter import filedialog
import time
import tkinter as tk
from tkinter import ttk
import Cpainelfull
import os
#pastaapp= os.path.dirname(__file__)
import getpass
usuario= getpass.getuser()

def abrir_jan_principal():
    principal= Cpainelfull.GeradorHorarios()
    
root= Tk()    

root.title("Orientação - Sorteio da ordem de Partida")
#root.iconbitmap(pastaapp +"\\imagem\\icone.ico" )   
root.iconbitmap  (f'C:\\Users\\{usuario}\\minisoftware\\imagem\\icone.ico')
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
img_fundo_entrada= PhotoImage(master=root, file= (f"C:\\Users\\{usuario}\\minisoftware\\imagem\\telaentrada.png"))
img_botao_entrada= PhotoImage(master=root, file= (f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botaoentrar.png"))
#criação de label
lab_fundo_entrada= Label(root, image=img_fundo_entrada)
lab_fundo_entrada.pack()
#criação de caixas de entrada
#criação de botões
bt_entrar= Button(root, bd=0, image=img_botao_entrada, command= abrir_jan_principal, cursor="hand2")
bt_entrar.place(width=118, height=64, x=186, y=308)
  #variáveis globais
  # funções
#executar mainloop
#app=root
root.mainloop()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Ola vai uma dica para quem quer saber mais sobre PDF, todos trabalham com medidas tipográficas que é 1/72 ou seja, uma polegada dividido por 72 então cada 72 que você usar em suas medidas corresponde a 25,4mm (2,54cm) então uma folha A4 tem exatos 595 x 844 (que corresponde a 210 x 297mm respectivamente)
"""
PDF é 1/72 ou seja, uma polegada dividido por 72 então cada 72 que você usar em suas medidas 
corresponde a 25,4mm (2,54cm) então uma folha A4 tem exatos 595 x 844 
(que corresponde a 210 x 297mm respectivamente)
Sendo assim, para colocar o título a 3cm da borda deve utilizar a medida de 85 
(pois 3cm é igual a 30mm que é igual a 1,18 polegadas).
A medida de 50 sugerida é equivalente a 0,7" que é igual a 18mm aproximadamente"""