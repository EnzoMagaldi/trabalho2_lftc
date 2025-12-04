regras = []
conjuntosRegras = {}

def lerArquivoRegras():
    regras.clear() # Para quando o usuário insere outro conjunto de regras sem reiniciar o programa.
    with open("regrasMT.txt", "r") as arqRegras:
        for linha in arqRegras:
            linha = linha.rstrip() #Remove caracteres do lado direito da string (Ex: \n)
            if linha:  
                regras.append(linha)

def lerArquivoCadeia():
    with open("cadeia.txt", "r") as arqCadeia:
        cadeia = arqCadeia.read().strip()  #Lê a cadeia e remove espaços e quebras de linha extras
    return cadeia

def formatarRegras(): # Para remover o "q" dos estados, deixando apenas o número
    regras = list(regra.replace("q", "") for regra in regras) #Cria uma nova lista, mas sem os "q"s das regras
    return regras

def tratarCadeia(cadeia):
    cadeia = "1" + cadeia + "/"
    return cadeia

def organizarRegras(): 
    for regra in regras:
        estado_inicial = regra[0]  #Lê o primeiro caractere da regra (que será sempre um número)
        if estado_inicial not in conjuntosRegras: #Caso esse número não esteja dentro do conjunto de regras, cria um novo conjunto
            conjuntosRegras[estado_inicial] = [] 
        conjuntosRegras[estado_inicial].append(regra)  # adiciona a regra à lista correspondente
    return conjuntosRegras

def verificarCorrespondencia(cadeia, ch):

def lerCadeia(cadeia):
    for ch in cadeia:
        if ch.isdigit():
            numero = ch
            break
    verificarCorrespondencia(cadeia, ch)