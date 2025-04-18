# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
list = [1,2,3,4,5,6,7,8,9,10]
print("Exercício 1 -> " + str(list))

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
list2 = [2, 'casa', True, 3, 'mesa']
print("Exercício 2 -> " + str(list2))

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "casa"
string2 = "mesa"
print( "Exercício 3 -> " + string1 + " e a " + string2)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1,2,3,4,4,4,5)
print (  "Exercício 4 -> " + str(tupla.count(4)))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
direct = {}
print(direct)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
direct2 = {"key1": 1, "key2": 2, "key3" : 3}
print("Exercício 6 ->" + str(direct2))

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
direct2["key4"]=4
print(direct2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
direc03 = {"key5":5, "key6":True , "key7": [1.3,"oi",False]}

print(direc03)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lit3 = [ "Elemento1",(2,"tupla"), {"key8":8, "key9": 9}, 1.0 ]

print(lit3)