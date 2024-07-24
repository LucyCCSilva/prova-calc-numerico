import math

def bissecao(f, xi, xs, tol, max_iter):
    """
    Método da Bisseção para encontrar a raiz de f(x).

    :param f: Função f(x)
    :param xi: Limite inferior do intervalo
    :param xs: Limite superior do intervalo
    :param tol: Tolerância desejada
    :param max_iter: Número máximo de iterações
    :return: A raiz aproximada, o número de iterações realizadas e o erro
    """
    if f(xi) * f(xs) >= 0:
        print("A função deve ter sinais opostos em xi e xs.")
        return None, 0, None

    for i in range(max_iter):
        xr = (xi + xs) / 2.0
        if abs(f(xr)) < tol or (xs - xi) / 2.0 < tol:
            return xr, i + 1, abs(f(xr))
        
        if f(xi) * f(xr) < 0:
            xs = xr
        else:
            xi = xr

    return xr, max_iter, abs(f(xr))

def f1(x):
    return math.cos(x) - x  # Exemplo: f(x) = cos(x) - x

def f2(x):
    return math.log(x)

if __name__ == "__main__":
    
    print("Exemplo 1: f(x) = cos(x) - x")
    
    xi, xs = 0, 1
    tol = 1e-5
    max_iter = 100

    raiz, iteracoes, erro = bissecao(f1, xi, xs, tol, max_iter)
    
    print(f"Raiz aproximada: {raiz}, Iterações: {iteracoes}, Erro: {erro}")
    
    print("\nExemplo 2: f(x) = ln(x)")
    
    xi, xs = 0.5, 5
    tol = 1e-3
    max_iter = 100
    
    raiz, iteracoes, erro = bissecao(f2, xi, xs, tol, max_iter)
    
    print(f"Raiz aproximada: {raiz}, Iterações: {iteracoes}, Erro: {erro}")

