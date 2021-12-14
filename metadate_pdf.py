from pdfminer.pdfparser import PDFParser , PDFDocument



def tratadata(data):
    carac = 0
    ano = []
    mes = []
    dia = []

#inicio do for    
    for i in data:

        if carac >=2 and carac <=5:
            ano.append(i) 
            
        
        elif carac >5 and carac <=7:         
            mes.append(i)
        elif carac >7 and carac<=9:
            dia.append(i)
        
        carac = carac + 1 
        
#fim for
    
    dia = ','.join(map(str,dia))
    mes = ','.join(map(str,mes))
    ano = ','.join(map(str,ano))
    dia = dia.replace(',', '')
    mes = mes.replace(',', '')
    ano = ano.replace(',', '')
    
    data = f'{dia}/{mes}/{ano}'

    return data
        
  

fp = open("lista.pdf", 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
parser.set_document(doc)
doc.set_parser(parser)


info = doc.info[0] #acessa no arquivo de dicionário o valor infornação



#O bloco try except serve para verificar se todas as informações, como:autor, data de modicação, estão nas informações do pdf
#cCaso as informações estejam são exibidas na tela
#separando os metadados encontrados pela biblioteca pdfminer  e colocando em cada variavel


try:
    autor = info['Author']
    print('AUTOR:'+autor)
except:
    pass

try:
    criador = info['Creator']
    criador =  "".join(map(chr,criador))
    print('CRADOR:'+criador)
except:
    pass

try:
    data_cria = info['CreationDate']
    data = tratadata(data_cria)
    print('DATA DE CRIAÇÃO:'+data)
except:
    pass

try:
    data_mod = info['ModDate']
    data1 = tratadata(data_mod)
    print('DATA DE MODIFICAÇÃO:'+data1)
except:
    pass

try:
    produtor = info['Producer']
    produtor =  "".join(map(chr,produtor))
    print('PRODUTOR:'+produtor)
except:
    pass    






