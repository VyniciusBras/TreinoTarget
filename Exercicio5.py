#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
# Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, 
# qual interruptor controla cada lâmpada?  

# Definimos um dicionário que representa as lâmpadas (0 = desligada, 1 = ligada)
lampadas = {'A': 0, 'B': 0, 'C': 0}

# Primeira ação:
# Ligamos o interruptor A e aguardamos (simulamos o aquecimento da lâmpada A)
lampadas['A'] = 1

# Simulamos a espera para aquecer a lâmpada, alterando para False muda o resultado das idas.
tempo_aquecimento = True

# Desligamos o interruptor A e ligamos o interruptor B
lampadas['A'] = 0
lampadas['B'] = 1

# Agora, simulamos a primeira ida à sala das lâmpadas
# Identificamos a lâmpada acesa, quente e fria

def verificar_lampadas(lampadas, tempo_aquecimento):
    resultado = {}
    
    for lampada in lampadas:
        if lampadas[lampada] == 1:
            resultado[lampada] = "acesa"
        elif lampadas[lampada] == 0 and tempo_aquecimento:
            resultado[lampada] = "quente"
        else:
            resultado[lampada] = "fria"
    
    return resultado

# Simula a ida à sala das lâmpadas
estado_lampadas = verificar_lampadas(lampadas, tempo_aquecimento)

# Exibimos os resultados da primeira ida
for lampada, estado in estado_lampadas.items():
    print(f"Lâmpada {lampada} está {estado}.")

