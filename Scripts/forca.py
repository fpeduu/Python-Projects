from random import randint
def jogar():
    print('Jogo da forca')
    palavras = ['banana','comida','escola','computador','trabalho','estudar']
    pal_sec = palavras[randint(0,5)]
    let_ace = str
    acertou = False
    erros = 0
    enforcado = False
    if pal_sec == 'banana' or pal_sec == 'comida' or pal_sec == 'escola':
       let_ace = ["-","-","-","-","-","-"]
    elif pal_sec == 'computador':
        let_ace = ["-","-","-","-","-","-","-","-","-","-"]
    elif pal_sec == 'trabalho':
        let_ace = ["-","-","-","-","-","-","-","-"]
    else:
        let_ace = ["-","-","-","-","-","-","-"]
    while not enforcado and not acertou:
        print("".join(let_ace))
        chute = str(input("Digite uma letra. "))
        if chute in pal_sec:
            pos = 0
            count = 0
            for letra in pal_sec:
                if chute.upper() == letra.upper():
                    let_ace[pos] = chute.lower()
                    count += 1
                
                pos+=1
        if count == 1:
            print("Tem 1 letra {} na palavra secreta. ".format(chute.upper()))
        if count > 1:
            print("Tem {} letras {} na palavra secreta. ".format(count,chute.upper()))
        if not chute in pal_sec:
            erros += 1
            print("Não tem nenhuma letra {} na palavra secreta. ".format(chute.upper()))
            print("Erros = {}".format(erros))
        if not "-" in let_ace:
            print("".join(let_ace))
            acertou = True
        if erros >= 3:
            enforcado = True
    if acertou == True:
       print("Parabéns, você acertou a palavra secreta. \n{}. ".format("".join(let_ace)))
    if enforcado == True:
        print("Eita. Você perdeu. \nA palavra secreta era {}. ".format("".join(pal_sec)))
    print("""Digite "jogar()" para jogar novamente. """)