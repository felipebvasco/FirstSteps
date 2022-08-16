#Sistemas de Apostas em Sistema "High Low"
#Variáveis:
# -saldo = Dinheiro Total
# -option = Opção para escolher modo de jogo
# -saldoaposta = Saldo apostado na rodada
# -saldorestante = saldo que restou após fazer a aposta (para manipular)
# -escolhaplayer = Número no qual o player decidiu apostar
# -numerodado = Número que foi sorteado no dado durante a rodada
# -saldoprêmio = Valor do saldo com o prêmio acrescido
# -saldoperdido = saldo após uma aposta errada


import random



saldo = float(input('Coloque o Saldo Disponível para começar as aspostas: '))
option = int(input('''Digite qual opção você deseja utilizar:
1 - Apostar em Número específico (increase balance value by 83,4%)
2 - Apostar no Sistema High-Low (increase balance value by 20%)

'''))

        
def game1():
    saldoaposta = float(input('Digite quanto você deseja apostar: '))
    saldorestante = saldo - saldoaposta
    if saldoaposta > saldo:
        print('Você não tem esse saldo disponível')
        exit()
    escolhaplayer = int(input('Escolha um número do dado entre 1 e 6: '))
    numerodado = random.randint(1, 6)
    print('O número sorteado foi {}'.format(numerodado))
    if numerodado == escolhaplayer:
        saldopremio = saldorestante + (saldoaposta * 1.834)      
        print('''Parabéns, Você acertou o número sorteado!
Saldo atual: {:.2f}'''.format(saldopremio))
    if escolhaplayer != numerodado:
        saldoperdido = saldo - saldoaposta
        print('Você errou, que pena! Seu saldo se encontra com o valor de R${:.2f}'.format(saldoperdido))
    
    
               

def game2():
    saldoaposta = float(input('Digite quanto você deseja apostar: '))
    saldorestante = saldo - saldoaposta
    if saldoaposta > saldo:
        print('Você não tem esse saldo disponível')
        exit()
    escolhaplayer1 = int(input('''Escolha entre números
1 - low(1, 2 e 3)
2 - High(4, 5 e 6)
'''))
    if escolhaplayer1 == 1:
        escolhatipo1 = low = [1, 2, 3]
        numerodado2 = random.randint(1, 6)
        if numerodado2 in low:
            saldopremio1 = saldorestante + (saldoaposta * 1.2)
            print('''Parabéns, O número sorteado foi {} e estava na sua escolha (low)
Saldo atual: {}'''.format(numerodado2, saldopremio1))
        if escolhaplayer1 != numerodado2:
            print('Você errou, que pena!')
    if escolhaplayer1 == 2:
        escolhatipo2 = high = [4, 5, 6]
        numerodado2 = random.randint(1, 6)
        if numerodado2 in high:
            saldopremio1 = saldorestante + (saldoaposta * 1.2)
            print('''Parabéns, O número sorteado foi {} e estava na sua escolha (high)
Saldo atual: {}'''.format(numerodado2, saldopremio1))
        if numerodado2 not in high:
            print('Você errou, que pena!')
   
if option == 1:
    game1()
    continuar = int(input('''
Deseja continuar Jogando?
1 - Sim
2 - Não

'''))
    while continuar == 1:
        game1()
        continuar = int(input('''
Deseja continuar Jogando?
1 - Sim
2 - Não

'''))
        
        
    if saldo == 0:
        print('Seu dinheiro acabou')
    else:
        exit()
        

if option == 2:
    game2()
    continuar = int(input('''Deseja continuar Jogando?
1 - Sim
2 - Não

'''))
    while continuar == 1:
        game2()
        continuar = int(input('''
Deseja continuar Jogando?
1 - Sim
2 - Não

'''))

    else:
        exit()


if saldo == 0:
    print('Seu dinheiro acabou')
    
    

        
    
                   


