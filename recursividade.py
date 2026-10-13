# Recursividade é a estratégia de quebrar um problema em partes menores até um
# problema conhecido.
# Por exemplo: 5! = 5 x 4! ; 4! = 4 x 3! ; ... ; 1! = 1 x 0! ; 0! = 1
# 0! é chamado de condição base, é a solução de um problema conhecido

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(0))
print(fatorial(5))

# Problema: Somar os elementos de uma lista

lista = [3, 5, 678, 3, 78, 90]
def soma_lista_sem_recursao(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
print(soma_lista_sem_recursao(lista))


def soma_lista_com_recursao(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista_com_recursao(lista[1:])
print(soma_lista_com_recursao(lista))