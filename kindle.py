# -*- coding: utf-8 -*-
# /media/pedro/Kindle/documents/
import subprocess
import sys
from difflib import get_close_matches

message_kindle_not_found = (
    "Kindle não encontrado! \nInforme o caminho do arquivo 'My Clippings': "
)

title = "KINPY"

whoami = "whoami"

data = subprocess.Popen([whoami], stdout=subprocess.PIPE)

output = str(data.communicate())


try:
    with open("/media/pedro/Kindle/documents/My Clippings.txt", "r") as arq_kindle:
        ar2 = arq_kindle.readlines()
except IOError:
    janela_1 = msgbox(message_kindle_not_found, title)
    Message_caminho = "Digite o caminho do arquivo: "

    output = enterbox(Message_caminho, title)
    print(output)
    try:
        with open(output, "r") as arq_kindle:
            ar2 = arq_kindle.readlines()
    except IOError:
        output = msgbox("Caminho não encontrado.", title)
    sys.exit()

livro_nome = str(input("Digite o nome do livro: "))
count = 0
ilinhas = iter(ar2)
test = False
for linha in ilinhas:
    if livro_nome in linha:
        test = True
        data_raw = next(ilinhas)
        ind = data_raw.find("Added on ")
        data_pronta = data_raw[ind + 9 :]

        next(ilinhas)
        a = next(ilinhas)
        if len(a) == 1:
            with open(f"Highlights: {livro_nome}.txt", "w") as arq_final:
                arq_final.write("\n")
                continue
        else:
            count += 1
            write = "#" + str(count) + " " + data_pronta + "\n" + "\n"
            with open(f"Highlights:{livro_nome}.txt", "w") as arq_final:
                arq_final.write("\n")
                arq_final.write(write)
                arq_final.write(a)
                arq_final.write("\n")
if not test:
    list_of_close_matches = get_close_matches(livro_nome, ar2)
    print(
        "Não foram encontrados livros com esse titulo. \nAqui está alguns com nomes parecidos"
    )
    for i in list_of_close_matches:
        print("-> " + i.strip())

arq_kindle.close()
arq_final.close()
