import math

# Método do Ponto Fixo para encontrar a raiz de f(x).
def ponto_fixo(g, raiz, tol, max_iter):
    """
    Parâmetros da função:
        f        -> Função g(x)
        xi       -> Suposição inicial da raiz
        tol      -> Tolerância desejada
        max_iter -> Número máximo de iterações
    """

    """
        O método de ponto fixo é utilizado para encontrar uma raiz de uma função a partir de uma função equivalente de forma que x = g(x).
    """

    """
        Portanto, o primeiro passo para realizar esse método é supor um valor para a raiz
    """
    raiz_anterior = raiz
    """
        Em seguida, a função g(x) recebe como parâmetro a raiz sugerida e o resultado passa a ser a nova raiz.

        Esse processo é repetido até que o erro absoluto entre a raiz recém-calculada e aquela calculada na repetição anterior seja maior que o valor da tolerância
    """
    for i in range(max_iter):
        raiz_proxima = g(raiz_anterior)
        if abs(raiz_proxima - raiz_anterior) < tol:
            return raiz_proxima, i + 1, abs(raiz_proxima - raiz_anterior)
        raiz_anterior = raiz_proxima

    return raiz_proxima, max_iter, abs(raiz_proxima - raiz_anterior)

# Definindo, como exemplo, a função da questão 6
def f(x):
    return 3 * x - math.exp(x)
    
def g(x):
    return math.log(3 * x)

raiz = float(input("Insira uma PRIMEIRA SUPOSIÇÃO para a raiz: "))
tol = float(input("Insira o valor da TOLERÂNCIA: "))
max_iter = int(input("Insira o valor MÁXIMO DE INTERAÇÕES: "))
print("\n=============== RESULTADO =================")
raiz, max_iter, erro = ponto_fixo(g, raiz, tol, max_iter)
if raiz is not None:
    print(f"Raiz aproximada: {raiz}\nNúmero de iterações: {max_iter}\nErro: {erro}")
else:
    print("Não foi possível encontrar uma raiz válida.")
