# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo

def pede_pasta():  
    pasta = askdirectory()
    caminho.set(value=pasta)  
               
def renomeia(pasta,trecho_velho,trecho_novo,extensao):
    pasta = pasta.get()
    trecho_velho = trecho_velho.get()
    trecho_novo = trecho_novo.get()
    extensao = list(extensao.get().split(','))    
    
    for arq in os.listdir(pasta):
        if extensao == ['Sem Exceção']:
            novonome = arq.replace(trecho_velho, trecho_novo)
            os.rename(f'{pasta}/{arq}', f'{pasta}/{novonome}')
        else:
            for i in extensao:            
                if i in arq:
                    novonome = arq.replace(trecho_velho, trecho_novo)
                    os.rename(f'{pasta}/{arq}', f'{pasta}/{novonome}')
    showinfo(title='Resultado',message=f'Trocas Feitas em {pasta}!')
      

janela = Tk()
janela.title('Localiza e Substitui')

mainframe = ttk.Frame(janela, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
janela.columnconfigure(0,weight=1)
janela.rowconfigure(0,weight=1)

ttk.Label(mainframe,text='Selecione no botão abaixo a pasta que possui os arquivos a serem renomeados', font = 'Arial 10 bold').grid(row=0, column=0, columnspan=3)
ttk.Label(mainframe, text='Digite suas exceções separadas por vírgulas: ').grid(row=2,column=0, sticky=E)
ttk.Label(mainframe, text='Texto a ser substituído: ').grid(row=3,column=0, sticky=E)
ttk.Label(mainframe, text='Texto a substituir: ').grid(row=4,column=0, sticky=E)

exc = StringVar(value='Sem Exceção')
e1 = ttk.Entry(mainframe,textvariable=exc,width=30).grid(row=2,column=1, columnspan=2)

old = StringVar()
e2 = ttk.Entry(mainframe,textvariable=old,width=30).grid(row=3,column=1, columnspan=2)

new = StringVar()
e3 = ttk.Entry(mainframe,textvariable=new,width=30).grid(row=4,column=1, columnspan=2)

caminho = StringVar(value='O caminho da pasta escolhida será colocado aqui')
b1 = ttk.Button(mainframe,text='Seleciona Pasta',command=pede_pasta).grid(column=2,row=1)
ttk.Label(mainframe,textvariable=caminho).grid(column=0,row=1,columnspan=2)

b2 = ttk.Button(mainframe,text='Trocar nomes',width=50, command=lambda: renomeia(caminho, old, new, exc)).grid(row=5,column=0,columnspan=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
    
   


janela.mainloop()


