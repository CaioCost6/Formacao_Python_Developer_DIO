#UTILIZANDO %

nome = "Caio"
idade = 23
profissao = "Analista de dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

#Utilizamos: (%s - para string / %d - para inteiro / %f - para float)


print("---------------------------------------------------------------------")

#UTILIZANDO FORMAT

nome = "Caio"
idade = 23
profissao = "Analista de dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

print("------------------------------------------------------------------------------------------------------------------------------------------")

print("Olá, me chamo {1}. Eu tenho {0} anos de idade, trabalho como {2} e estou matriculado no curso de {3}." .format(idade, nome, profissao, linguagem))

print("-------------------------------------------------------------------------------------------------------------------------------")

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {lingua}." .format(nome=nome, idade=idade, profissao=profissao, lingua=linguagem))

print("-----------------------------------------------------------------------------")

#UTILIZANDO F-STRING

nome = "Caio"
idade = 23
profissao = "Analista de dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#F-STRING INFORMANDO QUANTAS CARACTERES APARECER APÓS O "."

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
