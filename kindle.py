# -*- coding: utf-8 -*-
 #/media/pedro/Kindle/documents/
import sys
from easygui import *
import subprocess
import os
 
message_kindle_not_found = "Kindle não encontrado! \nInforme o caminho do arquivo 'My Clippings': "

title = "KINPY"

whoami='whoami'

data = subprocess.Popen([whoami], stdout = subprocess.PIPE)
  
output = str(data.communicate())


try:
	arq_kindle=open('/media/pedro/Kindle/documents/My Clippings.txt', 'r')	
except IOError:
	janela_1 = msgbox(message_kindle_not_found, title)
	Message_caminho = "Digite o caminho do arquivo: "
    
	output = enterbox(Message_caminho, title)
	print(output)
	try:
		arq_kindle=open(output.encode('utf-8'), 'r')
	except IOError:
		output = msgbox("Caminho não encontrado.", title)
	quit()

arq_final=open('criados.txt', 'w')
string="Dostoevsky: The Seeds of Revolt"
count=0
ilinhas = iter(arq_kindle)
for linha in ilinhas:
	if string in linha:
		next(ilinhas)
		next(ilinhas)
		a=next(ilinhas)
		if len(a)==1:
			arq_final.write('\n')
			continue
		else:
			count+=1
			write='#'+str(count)+'\n'+'\n'
			arq_final.write(write)
			arq_final.write(a)
			arq_final.write('\n')
	
arq_kindle.close()
arq_final.close()