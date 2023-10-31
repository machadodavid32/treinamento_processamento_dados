# regex - regular expression
# De forma geral, o regex é como se fosse uma forma de encontrar, substituir e extrair..
# um único ou sequencia de caracteres de dentro de um string

import re

hey = 'carol@gmail.com'

# findall
#result = re.findall(r"(@.{1,8}\.)", hey)
#print(result)
# Resposta: ['@gmail.']

# Search
result = re.search(r"(@.{1,8}\.)", hey)
print(result)
# Resposta: <re.Match object; span=(5, 12), match='@gmail.'>

# Split
result = re.split(r"(@.{1,8}\.)", hey)
print(result)
# Resposta: ['carol', '@gmail.', 'com']

# sub
result = re.sub(r"(@.{1,8}\.)", '@yahoo.', hey)
print(result)
# Resposta: carol@yahoo.com


