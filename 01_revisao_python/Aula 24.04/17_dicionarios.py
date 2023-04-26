#Dicionário vazio
D = {}

D = dict()

#Dicionário com itens
D = {'nome': 'João', 'idade': '25'}
print(D)

D = dict(nome='João', idade=25)
print(D)

#Criando dicionário por pares de chave/valor
D = dict([('nome', 'idade'), ('João', '25')])
print(D)

#Indexação de dicionários
#Elementos de um dicionário devem ser acessados através de sua chave
D = {'nome': 'João', 'idade': '25'}

#Acessando o valor disponível em nome
print(D['nome'])
print(D['idade'])

#Tamanho do dicionário
print(len(D))

#Associação em dicionário
print('nome' in D)

#Alterações em dicionários

#Adicionar um elemento
D['sexo'] = 'masculino'
print(D)

#Editar elemento do dicionário
D['idade'] = 30
print(D)

#Apagar um elemento
del D['idade']
print(D)

#Alterações no dicionário utilizando métodos
D = {'nome': 'João', 'idade':'25'}

D.pop('idade')
print(D)

#Métodos de dicionários
D = {'nome': 'João', 'idade':'25'}

#Cria lista com as chaves
print(list(D.keys()))

#Criar uma loista com os valores
print(list(D.values()))

#Criar uma lista com os pares chave/valor
print(list(D.items()))

#Retorne None, caso a chave não exista
D = {'nome': 'João', 'idade':'25'}
#print(D['sexo'])
print(D.get('sexo'))

#iteração em dicionários
D = {'nome': 'João', 'idade':'25'}

for i in D.keys():
    print(i)