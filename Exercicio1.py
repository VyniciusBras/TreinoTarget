#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule 
# a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#Funções declaradas
def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def in_fibonacci(n):
    fib_seq = fibonacci_sequence(n)
    if n in fib_seq:
        return (f"O número {n} pertence à sequência de Fibonacci.")
    else:
        return (f"O número {n} não pertence à sequência de Fibonacci.")

#Leitura do número
numero_informado = int(input("Informe um número: "))
resultado = in_fibonacci(numero_informado)
print(resultado)
