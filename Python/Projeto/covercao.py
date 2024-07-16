#Como em java, existêm converções de valores, Como de int para uma srt. ]
# Como um linguagêm dinâmica, o Python consegue utilizar um sinal para mais de um tipo de dado. Exemplo:
print(1+1)
print('1'+'1') 
#Mas, se tentarmos juntar dois tipos de dados diferentes, o Python não consegue resolver. Exemplo:
'''print(1+'1')'''
#Para resolver isso, utilizamos a classe 'int()'
print('1', type('1'))#Nesta linha o 1 é identificado como str
print(int('1'), type(int('1')))#Nesta linha, ele identifica o 1 como int
print(int('1')+1)#ele consegue fazer a soma. Apenas porque o 1 pode ser um número inteiro.
'''print(int('abc')+1)'''# se a tentativa for feita com uma frase, ele não consegue somar e me mostra um erro
#Essa classe de aplica a outras variáveis, como: 'float()', 'srt()', 'bool()'
#Com isso, eu posso misturar um float com um int, e o resultado será entregue em float. Exemplo:
print(float('1')+1)
#Também posso colocar como boolean
print(bool(''))#Se não houver nenhum valor. Será considerada como flasa
print(bool(' '))#Se houver valor, ATÉ MESMO UM ESPAÇO. Será considerada como verdadera
#Também consigo transformar um número em string, mas não string em número
print(str(11)+'abc')
