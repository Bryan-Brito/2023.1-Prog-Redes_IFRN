M = [ [1,2,3], [4,5,6], [7,8,9]]
print(M)

print(M[0][0])

V = [x[1] for x in M]
print(V)

#Alterações nessa lista
L = [1,5,6]
print(L[1])
L[1] = 9
print(L)

#Alteração de lista utilizando indexação e slices
L = [1,5,6]
print(L)
#Antes: [1,5,6]

#Depois: [1,9,10,5,6]
L[1:1] = [9,10]
print(L)

#Desejado: [1,10,5,6]
L[1:2] = []

#Alterações com métodos
L.append(9)
print(L)

#Removendo elemento
L.pop()
print(L)

#Adicionar vários itens ao final
L = [1,5,6]
print(L)

L.extend([10,11])

#Remove elemento por posição
L.pop(3)
print(L)

#Outros métodos de alteração
L = [1,9,6,5,2]
print(L)

#Inverter a ordem da lista
L.reverse()
print(L)

#Remover por conteúdo
L.remove(6)
print(L)

#Ordenar
L.sort()
print(L)