# -*- coding: utf-8 -*-
import os
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring,askinteger
from tkinter.messagebox import showinfo, askquestion

def renomeia(pasta,trecho_velho,trecho_novo,extensao):
    for arq in os.listdir(pasta):
        if extensao == 'Sem':
            novonome = arq.replace(trecho_velho, trecho_novo)
            os.rename(f'{pasta}/{arq}', f'{pasta}/{novonome}')
        else:
            for i in extensao:            
                if i in arq:
                    novonome = arq.replace(trecho_velho, trecho_novo)
                    os.rename(f'{pasta}/{arq}', f'{pasta}/{novonome}')
    showinfo(title='Resultado',message=f'Trocas Feitas em {pasta}!')   

while True:
    caminho = askdirectory(title='Selecione a pasta com os arquivos a serem renomeados: ')
    extint = askinteger(title='Ativar modo específico', prompt='Digite 1 caso queira que somente alguns arquivos sejam renomeados (.mp3 ou .pdf, por exemplo), ou 0 caso contrário: ')
    
    if extint == 1:
        ext = list(askstring(title='Digite sua exceção', prompt='Digite suas exceções separadas por vírgula (,). Escolha direito!: ').split(','))
    else:
        ext = 'Sem'
        pass    
    
    old = askstring(title='Texto Original',prompt='Digite o texto a ser substituído: ')
    new = askstring(title='Texto Novo',prompt='Digite o texto a substituir: ')              
                   
    renomeia(caminho, old, new, ext)
    continua = askquestion(message='Deseja continuar a execução do programa?')
    if continua == 'no':
        break
        
       
    

           