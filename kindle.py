#Pedro Henrique de Sousa Alcântara 30-05-22
import subprocess
import sys
from difflib import get_close_matches
import easygui
message_kindle_not_found = (
    "Kindle não encontrado! \nInforme o caminho do arquivo 'My Clippings': "
)

title = "KINPY"

whoami = "whoami"

data = subprocess.Popen([whoami], stdout=subprocess.PIPE)

output = str(data.communicate())


try:
    with open("/home/pedro/Desktop/My Clippings.txt", "r") as arq_kindle:
        ar2 = arq_kindle.readlines()
except IOError:
    janela_1 = easygui.msgbox(message_kindle_not_found, title)
    Message_caminho = "Digite o caminho do arquivo: "

    output = easygui.enterbox(Message_caminho, title)
    print(output)
    try:
        with open(output, "r") as arq_kindle:
            ar2 = arq_kindle.readlines()
    except IOError:
        output = easygui.msgbox("Caminho não encontrado.", title)
    sys.exit()

#LIVRO_NOME= str(input("Digite o nome do livro: "))
CONTADOR = 0
EXISTE_ANOTACOES = False
note_indicator = False
counter = 0
see = True
mark = []

while see == True:
    try:
        data = ar2[counter+1]
    except IndexError:
        see = False
        break
    if data[0:8] == "- Your N":
        dicionario = {"titulo": ar2[counter], "data": ar2[counter+1], "highlight": ar2[counter+8], "nota": ar2[counter+3]}
        print(dicionario)
        #print(ar2[counter+10])
        counter +=10
        mark.append(dicionario)
    else:
        dicionario = {"titulo": ar2[counter], "data": ar2[counter+1], "highlight": ar2[counter+3], "nota": "0"}
        print(dicionario)
        counter +=5
        mark.append(dicionario)