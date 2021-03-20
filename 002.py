def jokepo(a):
    from random import choice
    computador = choice(['Pedra','Papel','Tesoura']).lower()
    jogador = a
    print(f'O jogador escolheu {a} e o computador escolheu {computador}')
    if jogador == computador:
        print('EMPATOU!')
    else:
        if computador == 'pedra' and jogador == 'papel':
            print('PARABÉNS VOCÊ GANHOU!')
        elif computador == 'pedra' and jogador == 'tesoura':
            print('PERDEU!')
        elif jogador == 'pedra' and computador == 'papel':
            print('PERDEU!')
        elif jogador == 'pedra' and computador == 'tesoura':
            print('PARABÉNS VOCÊ GANHOU!')
        elif jogador == 'tesoura' and computador == 'papel':
            print('PARABÉNS VOCÊ GANHOU!')


    
while True:
    jogada = str(input('Escolha entre Pedra Papel e tesoura: ')).strip().lower()
    jokepo(jogada)
    r = str(input('Quer tentar novamente[S/N]: ')).strip().lower()[0]
    if r == 'n':
        break
print('VOLTE SEMPRE')

