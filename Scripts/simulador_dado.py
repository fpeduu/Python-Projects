import random

while True:
    resposta = input('Deseja jogar o dado? [S/N] \n')
    resposta_f = resposta.strip().lower()
    
    while not resposta_f == 's' and not resposta_f == 'n':
        print('Resposta inválida! ')
        resposta = input('Deseja jogar o dado? [S/N] \n')
        resposta_f = resposta.strip().lower()

    if resposta_f == 's':
        print(f'E o número é... {random.randint(1, 6)}!')
    else:
        print('Até a próxima! ')
        break
            
