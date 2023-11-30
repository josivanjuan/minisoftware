import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import shuffle
import random
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
import subprocess
import time, datetime
from datetime import datetime, timedelta
from tkinter import scrolledtext
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from io import BytesIO
import webbrowser
import os
import Csobre
import getpass
usuario= getpass.getuser()

# CLASSE PARA TRABALHAR COM OS NOMES-------------------------------------------
class GeradorHorarios:
    def __init__(self):
        time.sleep(0.3)
        self.root = Toplevel()
        self.canvas = tk.Canvas(self.root)
    #definir cabeçalho e tamanho da janela
        self.root.title("Aplicativo - Sorteio da ordem Secreta")
        self.root.iconbitmap(f'C:\\Users\\{usuario}\\minisoftware\\imagem\\icone.ico')
        #self.root.resizable(width=False, height=False)
        self.root['bg'] = "#383838" 
        self.largura = 1360
        self.altura = 640
        self.largura_screen = self.root.winfo_screenwidth()
        self.altura_screen = self.root.winfo_screenheight()
    #definir a posição da janela
        self.posX=self.largura_screen/2 - self.largura/2
        self.posy=self.altura_screen/2 - self.altura/2
    #definir a geometria centralizada na tela
        self.root.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posy))
    #criar o plano de funo da tela
        self.img_fundo_root= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\telapainel.png" ))
        self.img_botao_sortear= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botaosortear.png" ))
        self.img_botao_sortear_feminino= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botao_sorteiofeminino.png" ))
        self.img_botao_sortear_masculino= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botao_sorteiomasculino.png" ))
        self.img_botao_apagar_sorteio= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\apagar.png" ))
        self.img_botao_gerarlistar= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botaogeralista.png" ))
        self.img_botao_pdf= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botaopdf.png" ))
        self.img_botao_csv= PhotoImage(master=self.root, file=(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\botaocsv.png" ))
    #criação de label para chamar o plano de fundo
        self.lab_fundo_entrada= Label(self.root, image=self.img_fundo_root)
        self.lab_fundo_entrada.pack()
#CRIAÇÃO DE MENUS
       #configuração janela principal
        self.meumenu= Menu(self.root)
#ARQUIVOadicionar menu dentro de um menu titulo
        self.fileMenu= Menu(self.meumenu,tearoff=0, background="#383838")
        self.fileMenu.add_command(label="Abrir Pasta do Sistema", command=self.abrir_pasta_sistema)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Sair", command=self.root.destroy)
        self.meumenu.add_cascade(label="Sorteio", menu=self.fileMenu )
#EDITARadicionar menu dentro de um menu titulo
        self.editMenu= Menu(self.meumenu, tearoff=0, background="#383838")
        self.editMenu.add_command(label="Manual do Sistema", command= self.abrir_manual)
        self.editMenu.add_command(label="Sobre", command= self.abrir_janela_sobre  )
        self.meumenu.add_cascade(label="Ajuda", menu=self.editMenu)
        self.root.config(menu=self.meumenu) 

#CRIAÇÃO DE BOTÕES PARA EXECUTAR AS FUNÇÕES-----------------------------------------------------------
#Criar botão para sorteio das 3 forças <<<<<<<<<<<<<<<<<<<<<<<<<<
        self.botao_sorteio_feminino= tk.Button(self.root, bd=0.5, image=self.img_botao_sortear_feminino, command= self.sorteio_equipesf, cursor='hand2') 
        self.botao_sorteio_feminino.place(width=40, height=40, x=25, y=155)
        self.botao_sorteio_masculino= tk.Button(self.root, bd=0.5, image=self.img_botao_sortear_masculino, command= self.sorteio_equipesm, cursor='hand2')
        self.botao_sorteio_masculino.place(width=40, height=40, x=85, y=155)
        #Criar botão para apagar sorteio equipes e apagar lista e nomes
        self.botao_apagar_sorteio= tk.Button(self.root, bd=0.5, image=self.img_botao_apagar_sorteio, command= self.apagarsorteio, cursor='hand2')
        self.botao_apagar_sorteio.place(width=40, height=40, x=145, y=155)
        self.botao_apagar_sorteio= tk.Button(self.root, bd=0.5, image=self.img_botao_apagar_sorteio, command= self.apagarlista, cursor='hand2')
        self.botao_apagar_sorteio.place(width=40, height=40, x=1130, y=42)
        self.botao_apagar_sorteio= tk.Button(self.root, bd=0.5, image=self.img_botao_apagar_sorteio, command= self.apagarnomes, cursor='hand2')
        self.botao_apagar_sorteio.place(width=40, height=40, x=537, y=490)
        #Criar botão para embaralhar / sortear os nomes para os horários de inicio que forem definidos
        self.botao_embaralhar= tk.Button(self.root, bd=0.5, image=self.img_botao_sortear, command= self.embaralhar_gerar_horarios, cursor="hand2")
        self.botao_embaralhar.place(width=64, height=64, x=700, y=140)
        # Criar Botão para transferir o texto sorteado para armazenar na caixa de lista geral de partida
        self.botao_transferir = tk.Button(self.root, text=">>", command=self.transferir_texto)
        self.botao_transferir.place(width=40, height=40, x=913, y=490)
        # Criar o botão de ordenar - gerar lista de partida
        botao_ordenar = tk.Button(self.root, bd=0.5, image=self.img_botao_gerarlistar, command=self.ordenar_horarios, cursor="hand2")
        botao_ordenar.place(width=40, height=40, x=980, y=42)
        # Criar o botão para gerar PDF
        self.botao_gerarpdf = tk.Button(self.root, bd=0.5, image=self.img_botao_pdf, command=self.pdfResultadofile, cursor="hand2")
        self.botao_gerarpdf.place(width=40, height=40, x=1030, y=42)
        # Criar o botão para gerar CSV
        self.botao_gerarcsv = tk.Button(self.root, bd=0.5, image=self.img_botao_csv, command=False, cursor="hand2")
        self.botao_gerarcsv.place(width=40, height=40, x=1080, y=42)

#criação de strng var para o PDF
        self.equipes_resultadof= tk.StringVar()
        self.equipes_resultadom= tk.StringVar()
        self.resultado_equipesf= tk.StringVar()
        self.resultado_equipesm= tk.StringVar()
        self.diap= tk.StringVar()
        self.dia= tk.StringVar()
        self.diab= tk.StringVar()
#VARIAVEL E MENU PARA SELEÇÃO DE COMPETIÇÃO -------------------------- def menu suspenso COMPETIÇÃO
        # Variável para armazenar a opção selecionada
        self.selected_optionc = tk.StringVar()
        # Lista de opções para o OptionMenu
        self.options_listc = [
            "Competição", 
            "CAMORFA",
            "ESAER",
            "INTERAFA",
            "INTERNAS DO ITA",
            "LIMA MENDES",
            "MAER",
            "MAREXAER",
            "MESTREX",
            "NAE", 
            "NAVAMAER", 
            "OCA",
            "PAM BR",
            "RACOAM"
        ] 
        # Criando o OptionMenu
        self.option_menu_varc = tk.StringVar(self.root)
        self.option_menu_varc.set(self.options_listc[0])  # Definindo a opção padrão
        self.option_menuc = tk.OptionMenu(self.root, self.option_menu_varc, *self.options_listc, command=self.on_option_selectedc)
        # Se the background color of Options Menu to green
        self.option_menuc.config(bg="#383838", fg="WHITE")
        # Set the background color of Displayed Options to Red
        self.option_menuc["menu"].config(bg="#383838")
        self.option_menuc.place(width=130, height=30, x=301, y=46)
#VARIAVEL E MENU PARA SELEÇÃO DE ETAPAS ------------------------------------- def menu suspenso ETAPA
        # Variável para armazenar a opção selecionada
        self.selected_option = tk.StringVar()
        # Lista de opções para o OptionMenu
        self.options_list = [
            "Etapa / Dia",
            "1º Dia", 
            "2º Dia", 
            "3º Dia", 
            "4º Dia", 
            "5º Dia", 
            "6º Dia", 
            "Outro"
        ] 
        # Criando o OptionMenu
        self.option_menu_var = tk.StringVar(self.root)
        self.option_menu_var.set(self.options_list[0])  # Definindo a opção padrão
        self.option_menu = tk.OptionMenu(self.root, self.option_menu_var, *self.options_list, command=self.on_option_selected)
        self.option_menu.config(bg="#383838", fg="WHITE")
        # Set the background color of Displayed Options to Red
        self.option_menu["menu"].config(bg="#383838")        
        self.option_menu.place(width=130, height=30, x=301, y=106)
#VARIAVEL E MENU PARA SELEÇÃO DE PERCURSOS ------------------------------------- def menu suspenso PERCURSO
        # Variável para armazenar a opção selecionada
        self.selected_optionp = tk.StringVar()
        # Lista de opções para o OptionMenu
        self.options_listp = [
            "Percurso",
            "Percurso Longo", 
            "Percurso Médio", 
            "Percurso Sprint", 
            "Revezamento",  
            "Outro"
        ] 
        # Criando o OptionMenu
        self.option_menu_varp = tk.StringVar(self.root)
        self.option_menu_varp.set(self.options_listp[0])  # Definindo a opção padrão
        self.option_menup = tk.OptionMenu(self.root, self.option_menu_varp, *self.options_listp, command=self.on_option_selectedp)
        self.option_menup.config(bg="#383838", fg="WHITE")
        # Set the background color of Displayed Options to Red
        self.option_menup["menu"].config(bg="#383838")           
        self.option_menup.place(width=130, height=30, x=301, y=162)
#CAIXA DE TEXTO PARA RECEBER NOMES DAS EQUIPES-------------def sorteio equipes
        self.text_equipes = scrolledtext.ScrolledText(self.root)
        self.text_equipes.insert(tk.END,"")
        self.text_equipes.place(width=160, height=82, x=25, y=48)
#CAIXA DE TEXTO : PARA MOSTRAR AS EQUIPES SORTEADAS FEMININO<----------def transferir_texto FEMININO
        self.equipes_resultadof = scrolledtext.ScrolledText(self.root)#, height=7, width=30)
        self.equipes_resultadof.place(width=160, height=82, x=25, y=320)
#CAIXA DE TEXTO : PARA MOSTRAR AS EQUIPES SORTEADAS MASSCULINO<----------def transferir_texto MASCULINO
        self.equipes_resultadom = scrolledtext.ScrolledText(self.root)#, height=7, width=30)
        self.equipes_resultadom.place(width=160, height=82, x=25, y=503)
#CAIXA DE TEXTO: PARA RECEBER A LISTA DE ATLETAS ---------------------------def embaralhar_gerar_horarios
        self.text_nomes = scrolledtext.ScrolledText(self.root)#, height=8, width=30)
        self.text_nomes.insert(tk.END,"")
        self.text_nomes.place(width=295, height=356, x=218, y=240)
#CAIXA DE TEXTO: PARA RECEBER HORÁRIOS DE SORTEIO
        self.entry_horario = tk.Entry(self.root)
        self.entry_horario.place(width=40, height=20, x=536, y=335)
        # Caixa de texto para inserir incremento em minutos
        self.entry_incremento = tk.Entry(self.root)
        self.entry_incremento.place(width=17, height=20, x=547, y=447)
#CAIXA DE TEXTO 1: PARA MOSTRAR OS NOMES SORTEADOS/EMBARALHADOS E HORÁRIOS<----------def transferir_texto
        self.text_resultado = scrolledtext.ScrolledText(self.root)#, height=7, width=30)
        self.text_resultado.place(width=300, height=356, x=598, y=240)
#CAIXA DE TEXTO 2: PARA SALVAR O TEXTO DO SORTEIO POR FORÇA-----------------def ordenar horarios
        self.caixa_texto2 = scrolledtext.ScrolledText(self.root)#, height=25, width=30)
        self.caixa_texto2.place(width=365, height=495, x=972, y=100)
# DEFINIR FUNÇÕES------------------------------------------------------------
#////////////////////////////////////////////////////////////////////////////////
    def abrir_janela_sobre(self):
        self.sobre = Csobre.JanelaSobre() 
#FUNÇÃO PARA SORTEAR / EMBARALHAR OS NOMES
    def sorteio_equipesf(self):
        # Obter nomes da caixa de texto 1
        equipe = self.text_equipes.get("1.0", "end-1c").splitlines()#('\n')
        equipe = [nome for nome in equipe if nome]  # Remover linhas em branco
        # Embaralhar os nomes
        shuffle(equipe)
        # Mostrar nomes embaralhadosna caixa de texto
        self.resultado_equipesf = '\n'.join(equipe)
        self.equipes_resultadof.delete("1.0", tk.END)
        self.equipes_resultadof.insert(tk.END, self.resultado_equipesf)
        return self.resultado_equipesf
#/////////////////////////////////////////////////////////////////////////////////////
##FUNÇÃO PARA SORTEAR / EMBARALHAR OS NOMES
    def sorteio_equipesm(self):
        # Obter nomes da caixa de texto 1
        equipes = self.text_equipes.get("1.0", "end-1c").splitlines()#('\n')
        equipes = [nome for nome in equipes if nome]  # Remover linhas em branco
        # Embaralhar os nomes
        shuffle(equipes)
        # Mostrar nomes embaralhadosna caixa de texto
        self.resultado_equipesm = '\n'.join(equipes)
        self.equipes_resultadom.delete("1.0", tk.END)
        self.equipes_resultadom.insert(tk.END, self.resultado_equipesm)
        return self.resultado_equipesm
##FUNÇÃO PARA APAGAR SORTEIOS
    def apagarsorteio(self):
        self.equipes_resultadom.delete("1.0", tk.END)
        self.equipes_resultadof.delete("1.0", tk.END)
#FUNÇÃO PARA ARMAZENAR OS VALORES DA VARIAVEL QUE SERÁ ESCOLHIDA NO MENU - COMPETIÇÃO
    def on_option_selectedc(self, *args):
        self.selected_optionc.set(self.option_menu_varc.get())
        self.diab= self.selected_optionc.get()
        print(self.diab)
#FUNÇÃO PARA ARMAZENAR OS VALORES DA VARIAVEL QUE SERÁ ESCOLHIDA NO MENU - ETAPA OU DIA 
    def on_option_selected(self, *args):
        self.selected_option.set(self.option_menu_var.get())
        self.dia= self.selected_option.get()
        print(self.dia)
#FUNÇÃO PARA ARMAZENAR OS VALORES DA VARIAVEL QUE SERÁ ESCOLHIDA NO MENU - PERCURSO
    def on_option_selectedp(self, *args):
        self.selected_optionp.set(self.option_menu_varp.get())
        self.diap= self.selected_optionp.get()
        print(self.diap)
#FUNÇÃO PARA SORTEAR / EMBARALHAR OS NOMES
    def embaralhar_gerar_horarios(self):
        # Obter nomes da caixa de texto 1
        nomes = self.text_nomes.get("1.0", "end-1c").splitlines()#('\n')
        nomes = [nome for nome in nomes if nome]  # Remover linhas em branco
        # Embaralhar os nomes
        shuffle(nomes)
        # Obter horário inicial e incremento
        horario_inicial = datetime.strptime(self.entry_horario.get(), "%H:%M")
        incremento = int(self.entry_incremento.get())
        # Gerar horários e formatar a saída
        horarios_gerados = [(horario_inicial + timedelta(minutes=i * (incremento + (incremento*2)))).strftime("%H:%M") for i in range(len(nomes))]
        # Mostrar nomes embaralhados e horários na caixa de texto
        resultado = [f"{hora} - {nome}" for hora, nome in zip(horarios_gerados, nomes)]
        resultado_texto = '\n'.join(resultado)
        self.text_resultado.delete("1.0", tk.END)
        self.text_resultado.insert(tk.END, resultado_texto)
#FUNÇÃO PARA SALVAR/ARMAZENAR O TEXTO DO SORTEIO DA CAIXA DE TEXTO 1 PARA CAIXA DE TEXTO 2 DA LISTA DE PARTIDA
    def transferir_texto(self):
        self.text_caixa1 = self.text_resultado.get("1.0", "end-1c")  # Obtém o texto da caixa de texto 1
        self.text_resultado.delete("1.0", "end")  # Apaga o texto da caixa de texto 1
        self.texto_caixa2 = self.caixa_texto2.get("1.0", "end-1c")  # Obtém o texto atual da caixa de texto 2
        texto_completo = self.texto_caixa2 + "\n" + self.text_caixa1  # Adiciona o texto da caixa 1 ao texto da caixa 2
        self.caixa_texto2.delete("1.0", "end")  # Limpa a caixa de texto 2
        self.caixa_texto2.insert("1.0", texto_completo)  # Insere o texto completo na caixa de texto 2
#FUNÇÃO PARA PEGAR A LISTA DE PARTIDA E COLOCAR E ORDEM CRESCENTE DE HORÁRIOS
    def ordenar_horarios(self):
        # Obter o texto da caixa de texto e dividi-lo em linhas
        self.linhas = self.caixa_texto2.get("1.0", "end-1c").splitlines()#("\n")
        # Remover linhas em branco
        self.linhas = [linha for linha in self.linhas if linha.strip()]
        # Ordenar as linhas em ordem crescente cx 3
        self.linhas_ordenadas = sorted(self.linhas)
        # Atualizar o texto na caixa de texto 3 com os horários ordenados
        self.caixa_texto2.delete("1.0", "end")
        self.caixa_texto2.insert("1.0", "\n".join(self.linhas_ordenadas))
#FUNÇÃO PARA APAGAR LISTA DE SORTEIO DE NOMES
    def apagarlista(self):
        self.msg= messagebox.askokcancel("Já Salvou o PDF?", "Tem certeza de que deseja apagar a lista de partida e todo o sorteio?")
        if self.msg:
            self.caixa_texto2.delete("1.0", "end")
            self.text_nomes.delete("1.0", "end")
            self.text_resultado.delete("1.0", "end")
            self.equipes_resultadom.delete("1.0", "end")
            self.equipes_resultadof.delete("1.0", "end")
            self.option_menu_varc.set(self.options_listc[0])
            self.option_menu_varp.set(self.options_listp[0])
            self.option_menu_var.set(self.options_list[0])
        else:
            None
    def apagarnomes(self):
        self.text_nomes.delete("1.0", "end")
#FUNÇÃO PARA GERAR O RESULTADO EM ARQUIVO DE PDF NA TELA
    def pdfResultadofile(self):
        self.msg= messagebox.askokcancel("Conferir informação", "Todos os campos foram preenchidos? Deseja Prosseguir?")
        
        if self.msg:      

            self.texto = self.linhas_ordenadas
            self.buffer = BytesIO()
            self.pdf = canvas.Canvas(self.buffer, pagesize=A4)
            self.pdf.setFont("Helvetica-Bold", 12) #titulo
            self.pdf.drawString(470, 820, "Lista de Partida")
            self.pdf.drawImage(f"C:\\Users\\{usuario}\\minisoftware\\imagem\\orienteering.png", 430,815, width=20, height=20 )
            self.pdf.rect(20,810,550, 1, fill=True, stroke=False)
    #CRIAR IMPRESSÃO PARA MOSTRAR A ORDEM DO SORTEIO DAS 3 FORÇAS
            self.pdf.setFont("Helvetica-Bold", 10) #sorteio feminino
            #self.pdf.drawString(100, 800, "Feminino" )
            self.pdf.drawString(100, 800, f"Feminino: {self.resultado_equipesf}")
            self.pdf.setFont("Helvetica-Bold", 10) #sorteio masculino
            self.pdf.drawString(100, 788, f"Masculino: {self.resultado_equipesm}")
            self.pdf.setFont("Helvetica-Bold", 10) #competição
            self.pdf.drawString(100, 776, f"{self.diab}")
            self.pdf.setFont("Helvetica-Bold", 10) #etapa
            self.pdf.drawString(100, 764, f"{self.dia}" )
            self.pdf.setFont("Helvetica-Bold", 10) #percurso
            self.pdf.drawString(100, 752, f"{self.diap}" )
            #imagens
            self.logo1 = f"C:\\Users\\{usuario}\\minisoftware\\logo\\logo1.png"
            self.logo2 = f"C:\\Users\\{usuario}\\minisoftware\\logo\\logo2.png"
            self.logo3 = f"C:\\Users\\{usuario}\\minisoftware\\logo\\logo3.png"
            self.logo4 = f"C:\\Users\\{usuario}\\minisoftware\\logo\\logo4.png"
            self.pdf.drawImage(self.logo1, 310,815, width=20, height=20 )
            self.pdf.drawImage(self.logo2, 340,815, width=20, height=20 )
            self.pdf.drawImage(self.logo3, 370,815, width=20, height=20 )
            self.pdf.drawImage(self.logo4, 400,815, width=20, height=20 )
                       #rodapé %d de %B de %Y
            hora= datetime.now().strftime("%d/%b/%Y às %H:%M:%S")
            self.pdf.rect(20,20,550, 1, fill=True, stroke=False)
            self.pdf.setFont("Helvetica-Bold", 6) #rodapé
            self.pdf.drawString(355, 10, "APP: Sorteio da Lista de Partida - gerada em: " + hora )
            self.y = 730
            for linha in self.texto:
                self.pdf.drawString (100, self.y, linha  )
                self.y -= 12
            self.pdf.save()
            self.buffer.seek(0)
            #criar função para salvar o arquivo PDF
            #gerar o arquivo na tela
            with open("listadepartida.pdf", "wb") as f:
                f.write(self.buffer.read())
            webbrowser.open("listadepartida.pdf")
        else:
            None  
    def abrir_pasta_sistema(self):
    # Substitua 'Caminho/da/Pasta' pelo caminho da pasta desejada
        self.caminho_pasta = f"C:\\Users\\{usuario}\\minisoftware\\"
        os.startfile(self.caminho_pasta)
    
    def abrir_manual(self):
        self.caminho_pasta = f"C:\\Users\\{usuario}\\minisoftware\\ajuda\\manual.pdf"
        os.system(f'start {self.caminho_pasta}')

#if __name__ == "__main__":
root = tk.Tk()
app = GeradorHorarios()
root.mainloop()
