# -*- coding: utf-8 -*-
#Pedro Henrique de Sousa Alcântara 30-05-22
 #/media/pedro/Kindle/documents/
import sys
from easygui import *
import subprocess
import os
from difflib import get_close_matches

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
#livro_nome=str(input("Digite o nome do livro: "))
string="Dostoevsk: The Seeds of Revolt"
ar2=arq_kindle.readlines()
count=0
ilinhas = iter(arq_kindle)
test=False
for linha in ilinhas:
	if string in linha:
		test=True
		data_raw=next(ilinhas)
		ind=data_raw.find('Added on ')
		data_pronta=data_raw[ind+9:]

		next(ilinhas)
		a=next(ilinhas)
		if len(a)==1:
			arq_final.write('\n')
			continue
		else:
			count+=1
			write='#'+str(count)+' '+data_pronta+'\n'+'\n'
			arq_final.write(write)
			arq_final.write(a)
			arq_final.write('\n')
if test==False:
	list_of_close_matches=get_close_matches(string, ar2)
	print('Não foram encontrados livros com esse titulo. \nAqui está alguns com nomes parecidos')
	for i in list_of_close_matches:
		print('-> '+ i.strip())


arq_kindle.close()
arq_final.close()