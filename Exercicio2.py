#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificar_letra_a(texto):
    # Converte a string para minúsculas para simplificar a contagem
    texto_minusculo = texto.lower()

    # Conta o número de ocorrências da letra 'a'
    contagem = texto_minusculo.count('a')

    if contagem > 0:
        return (f"A letra 'a' ocorre {contagem} vez(es) no parágrafo.")
    else:
        return ("A letra 'a' não foi encontrada.")

# Exemplo: Substitua este valor para testar com outra string
texto_informado = input("Por favor digite um parágrafo: ")
resultado = verificar_letra_a(texto_informado)
print(resultado)
