#Tarefas p/ próximo encontro.
#Melhorar o código
#Mostrar funcionamento
#Explicar funcionamento
#Dividir tarefas em funções

from random import randint

print('Jogo da forca')

def jogar():
    palavras = ['recife','programar','bonito','banana','comida','escola','computador','trabalho','estudar']
    pal_sec = palavras[randint(0, len(palavras)-1)]
    erros = 0
    let_ace = []
    for c in pal_sec:
        let_ace += '-'
    fim = False


    def verificaChute(erros):
        if chute in pal_sec:
            print("Acertou.")
            pos = 0
            for letra in pal_sec:
                if chute.upper() == letra.upper():
                    let_ace[pos] = chute.lower()
                pos+=1
        else:
            erros += 1
            print("Errou.".format(chute.upper()))
            print("Erros = {}".format(erros))
        return(erros)    

    def venceuOuPerdeu(erros, fim):
        if not "-" in let_ace:
            print("".join(let_ace))
            print("Parabéns, você acertou a palavra secreta. \n{}. ".format(''.join(let_ace)))
            fim = True
        elif erros >= 3:
            print("Eita. Você perdeu. \nA palavra secreta era {}. ".format(pal_sec))
            fim = True
        return fim


    while fim == False:
        print(''.join(let_ace))
        chute = str(input("Digite uma letra. "))
        
        erros = verificaChute(erros)

        fim = venceuOuPerdeu(erros, fim)


jogar()


repetir = True

def continuar(repetir):
    continuar = input('Deseja continuar? [S/N]')
    if continuar.upper() == 'S':
        jogar()
    elif continuar.upper() == 'N':
        print('Até a próxima. ')
        repetir = False
    else:
        print('Opção inválida')
        repetir = True
    return repetir


while repetir:
    repetir = continuar(repetir)