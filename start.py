#coding: utf

####### GPIOS #########
#LED BRANCO = 6, 18   #
#LED AMARELO = 17, 12 #
#LED AZUL = 22 ,5     #
#LED VERMELHO= 24 ,27 #
#LED VERDE =  25, 23  #
#######################


import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import ImProc
import numpy as np
import cv2
import sys
import os
'''
###############################################
##arr = array lido na img atual               #
##path = caminho do arquivo que tem a planilha#
# ESTA FUNCAO RECEBE CADA COR DE CADA AMOSTRA #
# JUNTA TODAS OS RESULTADOS SEPARADOS POR COR #
###############################################
def createCSV(arr,path):
    #print(arr)
    #print(path)
    csv = np.genfromtxt(path,delimiter=',')
    data = np.array(csv)
    newData = arr
    if(len(data)==0):
        data = np.concatenate((data,newData),axis=0)
    else:
        data = np.column_stack((data,newData))
        
    np.savetxt(path,data,delimiter=',',fmt='%f')  

################################################
'''    
    
path = '/home/pi/Documents/tc2/'


overlay = sys.argv[1]
captura = capturaImagens.CapturaImagens()
captura.captura(overlay)

tamanhoImg = str(overlay)
nomeAmostra =raw_input("ID Amostra: \n")
#print(nomeAmostra)
listaDeCores = ['green','red','white','yellow','blue']
#intensidadeDePixelsEmCadaCor=[]
#for x in range (len(listaDeCores)):
processamento = ImProc.ImProc()
#process = processamento.firstTec(nomeAmostra,listaDeCores[x],tamanhoImg)
processamento.histogramas(nomeAmostra,listaDeCores,tamanhoImg)
#intensidadeDePixelsEmCadaCor.append(process)




'''
#SALVA TODOS OS ARRAYS DE UMA COR EM UM CSV

nomeAmostra =raw_input("Digite a idendificação da amostra \n")

caminhoAmostra = path+"planilhas/Todos/"+nomeAmostra+".csv"


print(caminhoAmostra)
with open(caminhoAmostra,"w")as empty_csv:##apenas cria o arquivo
    pass
for x in range(len(intensidadeDePixelsEmCadaCor)):
    
    createCSV(intensidadeDePixelsEmCadaCor[x],caminhoAmostra)

################################################################



#Salva os arrays de cada cor em um CSV
a0 = np.asarray(intensidadeDePixelsEmCadaCor[0])
np.savetxt(path+"planilhas/green.csv", a0,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Green/Green.csv"
createCSV(a0,caminhoTodos)
a1 = np.asarray(intensidadeDePixelsEmCadaCor[1])
np.savetxt(path+"planilhas/red.csv", a1,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Red/Red.csv"
createCSV(a1,caminhoTodos)
a2 = np.asarray(intensidadeDePixelsEmCadaCor[2])
np.savetxt(path+"planilhas/white.csv", a2,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/White/White.csv"
createCSV(a2,caminhoTodos)
a3 = np.asarray(intensidadeDePixelsEmCadaCor[3])
np.savetxt(path+"planilhas/yellow.csv", a3,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Yellow/Yellow.csv"
createCSV(a3,caminhoTodos)
a4 = np.asarray(intensidadeDePixelsEmCadaCor[4])
np.savetxt(path+"planilhas/blue.csv", a4,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Blue/Blue.csv"
createCSV(a4,caminhoTodos)
'''

