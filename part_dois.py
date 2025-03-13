import random

print('gerador de senhas!!!')
print('\nSenha minima de 9 digitos')

# String com todos os caracteres possíveis para a senha
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_,!@#$%&*+=^().;'

qtd_caracteres =int(input('quantidade de senhas: '))

def buscar_minusculo():
    minusculo=''
    for letra in range(qtd_caracteres//4):
        minusculo += random.choice(caracteres[:26])
    return minusculo

def buscar_maiusculo():
    maiusculo=''
    for letra in range(qtd_caracteres//3):
        maiusculo += random.choice(caracteres[26:52])
    return maiusculo

def buscar_numero():
    numero=''
    for letra in range(qtd_caracteres//3):
        numero += random.choice(caracteres[52:62])
    return numero

def buscar_caracts():
    caracts=''
    for letra in range(qtd_caracteres//3):
        caracts += random.choice(caracteres[62:])
    return caracts

senh=buscar_minusculo()+buscar_maiusculo()+buscar_numero()+buscar_caracts()
comprimento_senha=len(senh)

if comprimento_senha < qtd_caracteres:
    for letra in range(qtd_caracteres-comprimento_senha):
        senh= random.choice(caracteres)
        
        
        
senha_final=''
for item in random.sample(senh,len(senh)):
    senha_final+=item
    


print(senha_final,len(senh))
        