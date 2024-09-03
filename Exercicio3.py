#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; 
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

INDICE = 12
SOMA = 0
K = 1

#Nas primeira interação o K se torna 2, levando a SOMA se tornar 2, 
# na segunda interação o K se torna 3, levando a SOMA se torna 5, 
# assim por diante até chegar na ultima interação que o K se torna 12 
# e a SOMA se torna 77 (soma = 66 + 12).

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
