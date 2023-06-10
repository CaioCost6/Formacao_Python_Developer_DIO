
curso = "pYthoN"

#FUNCAO MAIUSCULA (UPPER())
print(curso.upper())

#FUNCAO MINUSCULA (LOWER())
print(curso.lower())

#LETRA INICIAL MAIUSCULA (TITLE())
print(curso.title())

#Eliminando espaços em branco

curso = "    Python  "

#REMOVER TODOS OS ESPAÇOS (STRIP())
print(curso.strip())

#REMOVER ESPAÇO DA ESQUERDA (LSTRIP())
print(curso.lstrip())

#REMOVER ESPAÇO DA DIREITA (RSTRIP())
print(curso.rstrip())

#Centralização e junções

curso = "Python"

#CENTRALIZAR E INFORMAR TOTAL DE CARACTERE QUE DESEJA
print(curso.center(10,"-"))

#INFORMAR QUAL CARACTERE DESEJA APOS A LETRA
print("-".join(curso))