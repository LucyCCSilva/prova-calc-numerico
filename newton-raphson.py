import math

# Método do Newton-Raphson para encontrar a raiz de f(x).
def newton_raphson(f, df, raiz, tol, max_iter):
    """
    Parâmetros da função:
        f        -> Função g(x)
        df       -> Derivada da função f(x)
        x0       -> 
        tol      -> Tolerância desejada
        max_iter -> Número máximo de iterações
    """

    """
        O método de Newton-Raphson é utilizado para encontrar as raízes de uma função,, sendo mais eficiente quando a função é diferenciável e estimativa inicial suficientemente próxima da raiz.
    """

    """
        Portanto, o primeiro passo para realizar esse método é supor um valor para a raiz
    """
    for i in range(max_iter):
        """
            Em seguida, deve-se obter o valor da função e da sua derivada
        """
        y = f(raiz)
        dy = df(raiz)
        if dy == 0:
            raise ValueError("Derivada igual a zero. O método de Newton-Raphson falhou.")
        
        """
            A próxima raiz é dada a partir da fórmula iterativa: x(n+1) = x(n) - f(x(n))/ df(x(n))

            Esse cálculo é repetido até que o erro absoluto entre a raiz recém-calculada e aquela calculada na repetição anterior seja maior que o valor da tolerância
        """
        proxima_raiz = raiz - y / dy
        if abs(proxima_raiz - raiz) < tol:
            return proxima_raiz, i + 1, abs(proxima_raiz - raiz)
        
        raiz = proxima_raiz
    
    return raiz, max_iter, abs(f(raiz))

# Definindo, como exemplo, a função da questão 6
def f(x):
    return 3 * x - math.exp(x)

def df(x):
    return 3 - math.exp(x)

raiz = float(input("Insira uma PRIMEIRA SUPOSIÇÃO para a raiz: "))
tol = float(input("Insira o valor da TOLERÂNCIA: "))
max_iter = int(input("Insira o valor MÁXIMO DE INTERAÇÕES: "))
print("\n=============== RESULTADO =================")
try:
    raiz, iteracoes, erro = newton_raphson(f, df, raiz, tol, max_iter)
    print(f"Raiz aproximada: {raiz}\nIterações: {iteracoes}\nErro: {erro}")
except ValueError as e:
    print(e)
