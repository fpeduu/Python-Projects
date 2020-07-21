from time import sleep

class Calculadora:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f'Números na calculadora: {self.a} e {self.b}. '

    def soma(self):
        return f'A soma entre {self.a} e {self.b} é igual a {self.a + self.b}. '
    def subtracao(self):
        return f'A subtração entre {self.a} e {self.b} é igual a {self.a - self.b}. '
    def divisao(self):
        return f'A divisão entre {self.a} e {self.b} é igual a {self.a / self.b}. '
    def multiplicacao(self):
        return f'A multiplicação entre {self.a} e {self.b} é igual a {self.a * self.b}. '

a, b = input('Digite dois números separados por espaço. \n').strip().split()
calc = Calculadora(a, b)

while True:
    operacao = input('''Digite a opção desejada: \nSoma [1] \nSubtração [2] \nDivisão [3] \nMultiplicação [4] \nVer números [5] \nTrocar números [6] \nSair [0] \n''').strip()
    operacao_f = operacao.strip()

    if operacao_f == '0' or operacao_f == '1' or operacao_f == '2' or operacao_f == '3' or operacao_f == '4' or operacao_f == '5' or operacao_f == '6':
        if int(operacao_f) == 0: #Transformar numa função pra organizar mais
            print('Até a próxima! ')
            break
        elif int(operacao_f) == 1:
            print(calc.soma())
            sleep(1.5)
        elif int(operacao_f) == 2:
            print(calc.subtracao())
            sleep(1.5)
        elif int(operacao_f) == 3:
            print(calc.divisao())
            sleep(1.5)
        elif int(operacao_f) == 4:
            print(calc.multiplicacao())
            sleep(1.5)
        elif int(operacao_f) == 5:
            print(calc)
            sleep(1.5)
        elif int(operacao_f) == 6:
            a, b = input('Digite os dois novos números separados por espaço. \n').strip().split()
            calc = Calculadora(a, b)
            sleep(0.75)
        else:
            print('Opção inválida')
            sleep(1)
            
    else:
        print('Opção inválida')
        sleep(1)