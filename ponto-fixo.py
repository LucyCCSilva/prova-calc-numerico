import math

def ponto_fixo(g, x0, tol, max_iter):
    x_prev = x0
    for i in range(max_iter):
        x_next = g(x_prev)
        if abs(x_next - x_prev) < tol:
            return x_next, i + 1, abs(x_next - x_prev)
        x_prev = x_next

    return x_next, max_iter, abs(x_next - x_prev)

def g(x):
    return math.cos(x)  # Exemplo: g(x) = cos(x)

x0 = 0.5
tol = 1e-5
max_iter = 100

raiz, iteracoes, erro = ponto_fixo(g, x0, tol, max_iter)
if raiz is not None:
    print(f"Raiz aproximada: {raiz}, Iterações: {iteracoes}, Erro: {erro}")
else:
    print("Não foi possível encontrar uma raiz válida.")
