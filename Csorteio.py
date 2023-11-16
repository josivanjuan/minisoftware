from tkinter import *
import tkinter as tk
from tkinter import filedialog
import time
import random
#variáveis globais


class OrdemSecreta:
    #def __init__(self): #construtor que cria a funcionalidade incial da classe
    #    self.self = self
             
    def executarsorteio(self):
        self.forcas= ["Marinha","Exército","Força Aérea"]
        self.num_sorteios = 3 
        self.sort = random.sample(self.forcas, self.num_sorteios)
        self.resultado= (self.sort[0] + "\n" + self.sort[1] + "\n" + self.sort[2] + "\n")
        #print(self.resultado)
        return self.resultado
        #self.medio1fem.config(text=self.resultado)
    
    def apagarsorteio(self):
        self.resultado=""
        return self.resultado
        #print(self.resultado)




#resultado1= OrdemSecreta()
#resultado1.realizarsorteio()
#resultado1.apagarsorteio()

