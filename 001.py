from random import choice

computador = choice(['Pedra','Papel','Tesoura'])
jogador = str(input('Escolha uma opção [Pedra,Papel ou tesoura: ')).strip().lower()
if computador == jogador:
    print(f'Você escolheu {jogador} e o computador escolheu {computador}: EMPATOU!')

elif computador == 'Pedra' and jogador == 'Papel':
    print(f'Você escolheu {jogador} e o computador escolheu {computador}: PARABÉNS VOCÊ GANHOU!')
elif computador == 'Pedra' and jogador == 'tesoura':
    print(f'Você escolheu {jogador} e o computador escolheu {computador}: PERDEU!')

print('VOLTE SEMPRE')
print(computador)
