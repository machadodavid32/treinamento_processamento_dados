# Como podemos criar listas?

# Usando loop com range
numeros = []
for i in range(0,5):
    numeros.append(i)
print(numeros)

# Usando a função MAP

nomes = ['Larissa', 'Manoela', 'Gracinha', 'Tiazinha']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))
# ['Larissa APROVADO', 'Manoela APROVADO', 'Gracinha APROVADO', 'Tiazinha APROVADO']
  
    
    