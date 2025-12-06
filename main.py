regras = []
conjuntosRegras = {}

def lerArquivoRegras():
    global regras
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
    global regras 
    regras = list(regra.replace("q", "") for regra in regras) #Cria uma nova lista, mas sem os "q"s das regras

def tratarCadeia(cadeia):
    return list(cadeia + "/")

def organizarRegras(): 
    for regra in regras:
        estado_inicial = regra[0]  #Lê o primeiro caractere da regra (que será sempre um número)
        if estado_inicial not in conjuntosRegras: #Caso esse número não esteja dentro do conjunto de regras, cria um novo conjunto
            conjuntosRegras[estado_inicial] = [] 
        conjuntosRegras[estado_inicial].append(regra)  # adiciona a regra à lista correspondente
    return conjuntosRegras

def aplicarRegra(cadeia, pos, so, mov):
    cadeia[pos] = so

    if mov.upper() == "D":
        pos += 1
        # Se saiu da fita, adiciona símbolo branco
        if pos == len(cadeia):
            cadeia.append("/")   # símbolo branco padrão
            
    # Movimento para a esquerda
    elif mov.upper() == "E":
        pos -= 1
        # Se saiu à esquerda, adiciona branco no início
        if pos < 0:
            cadeia.insert(0, "/")
            pos = 0  # cabeça ajustada para o novo início

    return cadeia, pos

def verificarCorrespondencia(cadeia, estado_atual, pos):
    simbolo_lido = cadeia[pos]

    for regra in regras:
        partes = regra.split()
        if len(partes) != 5:
            print("Regra inválida encontrada:", regra)
            continue
        ei, si, eo, so, mov = partes
        if ei == estado_atual and si == simbolo_lido:
            nova_cadeia, nova_pos = aplicarRegra(cadeia, pos, so, mov)
            return True, eo, nova_cadeia, nova_pos

    return False, estado_atual, cadeia, pos

def lerCadeia(cadeia):
    estado = "1"      # estado inicial padrão
    pos = 0           # cabeça no início

    while True:
        # Aceitação
        if estado == "F":
            print("Cadeia aceita!")
            return True
        existe, novo_estado, cadeia, nova_pos = verificarCorrespondencia(
            cadeia, estado, pos
        )
        if not existe:
            print(f"Nenhuma regra encontrada para estado {estado} lendo '{cadeia[pos]}'")
            return False
        estado = novo_estado
        pos = nova_pos
        

print("Lendo regras...")
lerArquivoRegras()

print("Formatando regras...")
formatarRegras()

print("Organizando regras...")
organizarRegras()

print("Lendo cadeia...")
cadeia = lerArquivoCadeia()

print("Preparando cadeia...")
cadeia = tratarCadeia(cadeia)

print("Iniciando simulação da Máquina de Turing...")
resultado = lerCadeia(cadeia)

if resultado:
    print("Resultado: Cadeia aceita.")
else:
    print("Resultado: Cadeia rejeitada.")
