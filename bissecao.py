import math

# Método da Bisseção para encontrar a raiz de f(x).
def bissecao(f, xi, xs, tol, max_iter):
    """
    Parâmetros da função:
        f        -> Função f(x)
        xi       -> Limite inferior do intervalo
        xs       -> Limite superior do intervalo
        tol      -> Tolerância desejada
        max_iter -> Número máximo de iterações
    """

    """
        O método de bisseção é utilizado para encontrar uma raiz de uma função contínua em um intervalo [a, b] onde f(a) e f(b) têm sinais opostos.

        Portanto, o primeiro passo para realizar esse método é verificar se f(xi) * f(xs) resulta em um resultado positivo ou em zero.
    """
    if f(xi) * f(xs) >= 0:
        print("A função deve ter sinais opostos em xi e xs.")
        return None, 0, None

    """
        Aqui é feita a busca pelo valor mais próximo da raiz.
        Essa busca é realizada por um número de vezes equivalente ao número máximo de iterações definido em max_iter.

        Primeiro é definido o valor de xr, que recebe o valor médio do intervalo [xi, xs].

        Depois é verificado se a função ao receber xr ultrapassa o limite da tolerância ou se a metade do comprimento do intervalo atual é menor do que é a tolerância, ou seja, se o resultado é suficientemente próximo da raiz.

            Se qualquer uma dessas condições for verdade, a função retorna a raiz aproximada (xr), o número de interações somado mais um (i) e o resultado da função com xr (f(xr)).

            Caso nenhuma das condições seja verdade, é entao verificado se o resultado para xi e para xr, possuem, sinais opostos.

                Se sim, ou seja f(xi) * f(xr) < 0, a aproximação atual passa a ser o limite superior do intervalo. 

                Se não, a aproximação atual passa a ser o limite inferior do intervalo.

        Por fim, quando o limite de iterações é atingido, a última raiz calculada, o max_iter e o resultado da função para essa última raiz é retornado

    """
    for i in range(max_iter):
        raiz = (xi + xs) / 2.0
        if abs(f(raiz)) < tol or (xs - xi) / 2.0 < tol:
            return raiz, i + 1, abs(f(raiz))
        
        if f(xi) * f(raiz) < 0:
            xs = raiz
        else:
            xi = raiz

    return raiz, max_iter, abs(f(raiz))

# Definindo, como exemplo, a função da questão 6
def f(x):
    return 3 * x - math.exp(x)

x1 = float(input("Insira o valor para o limite INFERIOR do intervalo: "))
x2 = float(input("Insira o valor para o limite SUPERIOR do intervalo: "))
tol = float(input("Insira o valor da TOLERÂNCIA: "))
max_iter = int(input("Insira o valor MÁXIMO DE INTERAÇÕES: "))

print("\n=============== RESULTADO =================")
raiz, num_inter, erro = bissecao(f, x1, x2, tol, max_iter)
print(f"Raiz aproximada: {raiz}\nNúmero de iterações: {num_inter}\nErro: {erro}")
