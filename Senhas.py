import random
import string

completo = string.ascii_letters + string.digits + string.punctuation
pedido_usuario = ''


def get_senha(pedido, tamanho):
    senha = ''
    for i in range(tamanho):
        senha += random.choice(pedido)
    return senha

def get_tamanho():
    tamanho_usuario = input('\nInsira quantos caracteres deseja(número inteiro positivo): ')
    if not tamanho_usuario.isdigit() or int(tamanho_usuario) < 1:
        print('\nInsira um numero inteiro positivo!')
    return int(tamanho_usuario)

while True:
    print('1. Gerar senha aleatoria;\n2. Gerar senha a partir de uma base de caracteres;\n3. Sair do programa.')
    opcoes = input('--> ')
    if opcoes == '1':
        print(f'\nA senha sugerida é: {get_senha(completo, get_tamanho())}\n')
    elif opcoes == '2':
        pedido_usuario = list(input('\nInforme sua senha padrão: '))
        if len(pedido_usuario) < 6:
            print('\nNo minimo 6 caracteres!')
            continue
        senha = ''.join(random.sample(pedido_usuario, len(pedido_usuario)))
        print(f'\nA senha sugerida é: {senha}\n')
    elif opcoes == '3':
        print('\n-=-=-=- Programa encerrado -=-=-=-')
        break
    else:
        print('\nOpção invalida!')
