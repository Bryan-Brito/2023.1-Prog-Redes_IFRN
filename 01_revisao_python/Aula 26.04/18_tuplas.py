#Tupla vazia
T = ()

T = tuple()

#Tupla com itens
T = (4)
print(T)

T = (4,'abc',1.23,(9,8,7))
print(T)

T = 10,20
print(T)
print(type(T))

#Tupla
T = tuple('spam')
print(T)
T = tuple(range(0,10))
print(T)

#Indexação e slide
T = (10, 3.56, 200, 'casa')
print(T[0])
print(T[-1])#Último elemento

print(T[1:3])#Range de elementos

#Operações básicas com tuplas
print((1,2)+(3,4))

print((1,2)*3)

#Iteração e associação
T = (10, 20, 30)

print(10 in T)

for x in T:
    print(x)

#Tuple comprehensions
#Recurso para criação de tuplas por iteração a outro objeto

a = 'ifrn'
res = tuple(c*2 for c in a)
print(res)

x=(10) #o inteiro 10
print(x)
print(type(x))
y=(10,) #a tupla com um elemento inteiro
print(y)
print(type(y))


#Conversão
#Por exemplo, como as Tuplas são imutáveis, para ordena-las, é necessário converter para lista.

T = ('c','a','x','r')

#Converter para lista
tmp = list(T)
print(type(tmp))
print(tmp)
tmp.sort()
print(tmp)

#Converter para tupla
T = tuple(tmp)
print(type(T))
print(T)


#Métodos 
T = (1,2,3,2,5,2)

#Offset do primeiro elemento com valor 2
print(T.index(2))

#O próximo indice com valor 2 após o indice 2
print(T.index(2,2))

#Quantas vezes o valor 2 aparece
print(T.count(2))