MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")



if idade >= MAIOR_IDADE:
    print("Maior de idade")
else:
    print("Menor idade")


if idade >= MAIOR_IDADE:
    print("Maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Pode começar as aulas teoricas, mas não pode fazer as práticas")    
else:
    print("Menor idade")
