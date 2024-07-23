import math

def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivada igual a zero. O método de Newton-Raphson falhou.")
        
        x_next = x - fx / dfx
        if abs(x_next - x) < tol:
            return x_next, i + 1, abs(x_next - x)
        
        x = x_next
    
    return x, max_iter, abs(f(x))

# Exemplo de função f(x) = x^2 - 2 (procurando pela raiz quadrada de 2)
def f(x):
    return x**2 - 2

# Derivada de f(x), df(x) = 2x
def df(x):
    return 2 * x

x0 = 1.0
tol = 1e-5
max_iter = 100

try:
    raiz, iteracoes, erro = newton_raphson(f, df, x0, tol, max_iter)
    print(f"Raiz aproximada: {raiz}, Iterações: {iteracoes}, Erro: {erro}")
except ValueError as e:
    print(e)
