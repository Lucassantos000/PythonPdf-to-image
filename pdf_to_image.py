from os import times
from pdf2image import convert_from_path
import time

nome_arq_pdf = input(u"Nome_do_arquivo_pdf_sem_tipo(.pdf)->")
caminho_arq = fr'C:\Users\aa\Desktop\metpdf\{nome_arq_pdf}.pdf'
nome_imagem = input("prefixo_da_imagem-> ")
i = 0


from pdf2image import convert_from_path #importa a função convert_from_path 
pages = convert_from_path(caminho_arq, 500)

for page in pages:
    page.save(f'./imagens/{nome_imagem}_{i}.jpg', 'JPEG')
    i = i+1