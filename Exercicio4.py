#4) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, ___
#b) 2, 4, 8, 16, 32, 64, ____
#c) 0, 1, 4, 9, 16, 25, 36, ____
#d) 4, 16, 36, 64, ____
#e) 1, 1, 2, 3, 5, 8, ____
#f) 2,10, 12, 16, 17, 18, 19, ____

# a) A sequência aumenta em 2 a cada termo.
sequencia_a = [1, 3, 5, 7]
proximo_a = sequencia_a[-1] + 2
print(f"a) {proximo_a}")

# b) Cada termo é o dobro do anterior.
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_b = sequencia_b[-1] * 2
print(f"b) {proximo_b}")

# c) Esta é a sequência com numeros ao quadrado perfeitos.
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (len(sequencia_c))**2
print(f"c) {proximo_c}")

# d) Essa sequência representa esses numeros: 2,4,6,8 ao quadrado.
sequencia_d = [4, 16, 36, 64]
proximo_d = (2 * (len(sequencia_d) + 1)) ** 2
print(f"d) {proximo_d}")

# e) Sequência de Fibonacci, onde cada termo é a soma dos dois anteriores.
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_e = sequencia_e[-1] + sequencia_e[-2]
print(f"e) {proximo_e}")

# f) Após o primeiro número 2, a sequência inclui todos os números começando com 1 e de dois dígitos.
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = sequencia_f[-1] + 1
print(f"f) {proximo_f}")
