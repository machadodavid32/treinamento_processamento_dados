# Como usar uma list compreheesion

nova_lista = [2 * i for i in range(10)] # leia isso de tras pra frente, primeiro o range..depois for..
print(nova_lista)

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def aprovar_pessoa(nome):
    return nome + ' APROVADO'


nomes = ['Larissa', 'Manoela', 'Gracinha', 'Tiazinha']
#print([nome + ' aprovado' for nome in nomes])
# ['Larissa aprovado', 'Manoela aprovado', 'Gracinha aprovado', 'Tiazinha aprovado']

print([aprovar_pessoa(nome) for nome in nomes])
# ['Larissa APROVADO', 'Manoela APROVADO', 'Gracinha APROVADO', 'Tiazinha APROVADO']

'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''  

# Como recriar a lista de números acima usando a list compreheension?
from pprint import pprint # imprime coisas complexas de forma mais legível

pprint([[i for i in range(1,6)] for x in range(5)])
# Resposta: 
# [[1, 2, 3, 4, 5],
# [1, 2, 3, 4, 5],
# [1, 2, 3, 4, 5],
# [1, 2, 3, 4, 5],
# [1, 2, 3, 4, 5]]


# Usando condicionais em list c

nomes = ['Larissa', 'Manoela', 'Gracinha', 'Tiazinha']

print([aprovar_pessoa(nome) for nome in nomes if nome != 'Larissa'])
# Resposta: ['Manoela APROVADO', 'Gracinha APROVADO', 'Tiazinha APROVADO']

def eh_numero_par(numero):
    valor = numero % 2 # módulos 2 te entrega o restante de uma divisão
    if valor == 0:  # Se retornar zero é par
        return True
    else:
        False
        
            

# print([i for i in range(20) if i not in(1, 5, 15, 19)])
# Resposta: [0, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18]

print([i for i in range(20) if eh_numero_par(i)])
# Resposta: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# obs> A condicional é flexivel, podemos usar em outro lugar na list compreheesion

participantes = ['Larissa', 'Manoela', 'Gracinha', 'Tiazinha']
ganhadores = ['Gracinha', 'Tiazinha']

print([i + ' Ganhandor' if i in ganhadores else i + ' Não selecionado' for i in participantes])
# Resposta: ['Larissa Não selecionado', 'Manoela Não selecionado', 'Gracinha Ganhandor', 'Tiazinha Ganhandor']

# Desafio 1 - Crie a seguinte lista usando list compreheension [2, 4, 6, 8, 10]

print([i*2 for i in range(1, 6)])
# [2, 4, 6, 8, 10]

# Desafio 2 - usar uma lista de base e adicionar números na segunda lista
cores = ['vermelho', 'azul', 'roxo', 'laranja', 'branco']


print([str(cores.index(i) + 1) + '-' + i for i in cores])
# ['1-vermelho', '2-azul', '3-roxo', '4-laranja', '5-branco']

