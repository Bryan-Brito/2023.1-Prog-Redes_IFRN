nome = 'joao'
#Métodos para formatar Strings
print(f'a casa de {nome} fica em natal')
print('a casa de %s fica em natal' % nome)

#Utilizando uma sintaxe mais completa para a expressão
x = 1234
print('inteiros: ... %d ... %-6d ... %06d' % (x, x, x))


x = 1.23456789
print('%-6.2f | %05.2f | %+06.2f' % (x, x, x))