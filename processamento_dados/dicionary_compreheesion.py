from pprint import pprint

pprint({i:i for i in range(20)})

# Popular um dicionário com valores

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5',]
pprint({produto: 1 for produto in produtos})
# resposta: {'produto 1': 1, 'produto 2': 1, 'produto 3': 1, 'produto 4': 1, 'produto 5': 1}


# Como gerar uma matriz de valores de teste.

pprint({produto: [0 for i in range(5)] for produto in produtos})
#{'produto 1': [0, 0, 0, 0, 0],
# 'produto 2': [0, 0, 0, 0, 0],
# 'produto 3': [0, 0, 0, 0, 0],
# 'produto 4': [0, 0, 0, 0, 0],
# 'produto 5': [0, 0, 0, 0, 0]}

pprint({produto: [i*2 for i in range(5)] for produto in produtos})
# {'produto 1': [0, 2, 4, 6, 8],
# 'produto 2': [0, 2, 4, 6, 8],
# 'produto 3': [0, 2, 4, 6, 8],
# 'produto 4': [0, 2, 4, 6, 8],
# 'produto 5': [0, 2, 4, 6, 8]}


# Gerar valores de teste usando random
import random

pprint({produto: [random.randint(1000, 15000) for i in range(5)] for produto in produtos})
# {'produto 1': [10834, 3174, 7553, 8564, 2617],
# 'produto 2': [1897, 5792, 2090, 13843, 7706],
# 'produto 3': [9455, 7782, 8625, 9336, 12946],
# 'produto 4': [13012, 11772, 2635, 1458, 9861],
# 'produto 5': [14309, 11181, 7500, 9629, 7302]}

sorteios = ['sorteio 1', 'sorteio 2', 'sorteio 3', ]
participantes = ['joel', 'jessica', 'maria', 'aline', 'david', 'marcos', 'daniele', 'rafaela']

pprint({sorteio: [random.choice(participantes)] for sorteio in sorteios})
# {'sorteio 1': ['aline'], 'sorteio 2': ['marcos'], 'sorteio 3': ['jessica']}

