import random

print('gerador de senhas!!!')
print('\nSenha minima de 9 digitos')

# String com todos os caracteres possíveis para a senha
caracteres = 'abcdefghijklmnopqrstuvwxyz-_,!@#$%&*+=^.;ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

qtd_senha = int(input('quantidade de senhas: '))
qtd_caracteres = int(input('quantidade de caracteres: '))

for i in range(qtd_senha):
    senha = ''
    for q in range(qtd_caracteres):
        senha += random.choice(caracteres)  # Escolhe um caractere aleatório da string 'caracteres'
    
    print('Essa é uma senha gerada => ' + senha)

""" 
        senhas += random.choice(qtd_caracteres)
        
    print( 'Essas são as senhas => ' + senhas )
     """