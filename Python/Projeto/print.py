print(12, 34, sep='-') #a '','' separa os valores e dentro do print. O ''sep'' tem a função de alterar o separador de valores.

print(56, 78, sep= "- separou -") # o comando sep aceita aspas simples e aspas duplas.

#Quebra de linha
# \r\n -> CRLF (comando de quebra de linha para Windows)
# \n -> LF (comando de quebra de linha para Linux...)

print(12, 34, 56, sep='-', end='__') # o comando end faz a tarefa da quebra de linha
print(12, 34, 56, sep='-', end='\r\n') # como dito o: '\r\n' faz a quebra e linha padrão 
print(12, 34, 56, sep='-', end='__\r\n')# também posso fazer uma quebra de linha e colocar algo ANTES
print(12, 34, 56, sep='-', end='\r\n__')# também posso fazer uma quebra de linha e colocar algo DEPOIS
print(1+1)

#Escape

print('Murilo Alves')
print('Murilo \'Alves') #A \ funciona como uma caracter de escape, ela faz com que o interpretador python IGNORE o próximo caractere.
print('Murilo \'Alves\'')

#r

print(r'Murilo \'Alves\'') # o 'r' é utilizado para mostrar as barras

#truque para facilitar o escape

#digamos que quero colocar aspas duplas em meu nome, mas, quando faço isso meu interpretador entende que estou passando outras informações

print('"Murio Alves"')# eu posso simplesmente alternar de ' para "
