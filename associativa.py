import random
import matplotlib.pyplot as plt

def convolucao(x, h):
    """
    Calcula a convolução discreta entre duas sequências x e h.
    Retorna uma nova lista.
    """
    n = len(x)
    m = len(h)
    
    tamanho_saida = n + m - 1
    y = [0] * tamanho_saida
    
    for i in range(n):
        for j in range(m):
            y[i + j] += x[i] * h[j]
    
    return y


def gerar_sequencia(tamanho, minimo=-5, maximo=5):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]


x = [1, 2, 3]
h = [0, 1, 0.5]
g = [2, -1]

print("x =", x)
print("h =", h)
print("g =", g)

# (x * h) * g
lado1 = convolucao(convolucao(x, h), g)

# x * (h * g)
lado2 = convolucao(x, convolucao(h, g))

print("\n(x * h) * g =", lado1)
print("x * (h * g) =", lado2)
print("\nSão iguais?", lado1 == lado2)


# ==========================
# GERAÇÃO DOS GRÁFICOS
# ==========================

# Gráfico do lado 1
plt.figure()
plt.stem(range(len(lado1)), lado1)
plt.title("(x * h) * g")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Gráfico do lado 2
plt.figure()
plt.stem(range(len(lado2)), lado2)
plt.title("x * (h * g)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()