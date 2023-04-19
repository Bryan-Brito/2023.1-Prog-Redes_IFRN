#Lista vazia
L = []
L = list()

#Lista com 4 itens
L = [4, 'abc', 1.23, [9,8,7],[1,2,3,4,5]]
print(L)

#Lista de um objeto iterável
L = list('spam')
print(L)

#Indexaçã e slide
L = [4, 'abc', 1.23]
print(L[0]) 
print(L[-2])
print(L[:2])

#Operações básicas com listas
L = [4, 'abc', 1.23]
M = ['fgh', 5.6, 10, 145]

print(len(L))
print(len(M))

print(L+M) #concatenando listas
print(len(L+M))

#Repetição de elementos
print(3*L)

#Iteração e associação
L = [4, 'abc', 1.23]
print('abc' in L)

#Iterando sobre a lista
for x in L:
    print(x)

#List comprehensions
#Recurso para criação de listas por iteração a outro objeto

res = [i*4 for i in 'abc']
print(res)