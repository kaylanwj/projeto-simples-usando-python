import PyPDF2 
import os

marger = PyPDF2.PdfMerger()

lista_arquivo = os.listdir("arquivos")
lista_arquivo.sort()
print(lista_arquivo)

for arquivo in lista_arquivo:
    if ".pdf" in arquivo:
        marger.append(f"arquivos/{arquivo}")

marger.write("PDF Final.pdf")