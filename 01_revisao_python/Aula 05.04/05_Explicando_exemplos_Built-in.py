#Exemplos feitos pelo professor
S = "spam"
print(len(S)) #mostrar o tamanho de 's'
print(S[0]) #mostrando o primeiro ínidice de posição 0
print(S[1:3]) #definindo um intervalo que começa na posição 1 e vai até a posição 2
print(S + 'xyz') #concatençaõ de SPAM com XYZ

#Explicação feita por Bryan Brito

print(S.find('pa')) #A função 'find' irá encontrar o índice de onde começa o objeto 'pa' dentro da variável
print(S.upper()) #A função 'upper' tem como saída a variável com todas as letras em maiúsculo
print(S.isalpha()) #'isalpha' tem como objetivo verificar se todos os caracteres na string estão presentes no alfabeto, sendo assim, retornará 'True. Se não for o caso, irá retornar 'false'
print(S.replace('pa','ca')) #'replace' irá trocar os caracteres que estão sendo informados

L = [123, 'casa', 3.14] #Atribui uma lista à variável 'L'
print(len(L)) #Mede o tamanho da lista conforme os objetos contidos nela
print(L[0]) #Mostra o objeto no índice 0
print(L * 2) #Plota duas vezes a lista
L.append('bola') #Adiciona o valor à lista
print(L)


M = [[1,2,3],[4,5,6],[7,8,9]] #Concede à variável 'M' uma lista composta de listas
col2 = [n[1] for n in M] #Retorna os itens que estão dentro dos índices de cada lista
print(col2)
D = {'com':'ABC', 'num':23} #Dispõe um dicionário à variável 'D'
print(D['num']) #Retorna o valor dentro da chave 'num'
D['cor'] = 'azul' #Acrescenta uma chave e um valor ao dicionário 'D'
print(D)