import random

perguntar = False

def verificaChute(chute):
    if chute < 1 or chute > 10:
        while chute < 1 or chute > 10:
            print('Resposta inválida! ')
            chute = int(input('Digite um número de 1 a 10: '))

print('***' * 7)
print(' Jogo da adivinhação')
print('***' * 7)

def main():
    numero_secreto = random.randint(1, 10)
    vidas = 3
    pontos = 0

    def continua():
        vida_mais = vidas + 1
        print('Ganhou mais uma vida!')
        numero_secreto = random.randint(1, 10)
        print('Pensei em outro número de 1 a 10. Tente Descobrir!')
        return vida_mais, numero_secreto

    print('Pensei em um número de 1 a 10.\nConsegue descobrir qual é? Te dou 3 chances!')

    while True:
        chute = int(input('Digite seu chute: '))
        verificaChute(chute)
            
        if chute == numero_secreto:
            pontos += 1
            print('Exato!! Parabéns!')
            print(f'Tens {pontos} pontos.')
                
            continuar = input('Deseja continuar?? [S/N]\n')
            continuar_f = continuar.strip().lower() #formatado
            if continuar_f == 's':
                vidas, numero_secreto = continua()
            
            elif continuar_f == 'n':
                print('Certo. Até a próxima! ')
                break

            else:
                while not continuar_f == 's' and not continuar_f == 'n':
                    print('Resposta inválida! ')
                    continuar = input('Deseja continuar?? [S/N]')     
                    continuar_f = continuar.strip().lower()   

                if continuar_f == 's':
                    vidas, numero_secreto = continua()
                else:
                    print('Certo. Até a próxima! ')
                    break

        else:
            if vidas > 1:
                vidas -= 1
                print(f'Errou! Tens mais {vidas} chances. ')
            else:
                print('Errou! Suas chances acabaram. ')
                print('FIM DE JOGO')
                break

main()