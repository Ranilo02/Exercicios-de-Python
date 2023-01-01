"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome no jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

# solução 1

jogador = dict()
gols = list()
totalgols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas):
    gol = int(input(f'  Quantos gols na partida{c}? '))
    totalgols += gol
    gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = totalgols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {totalgols} gols.')


# solução 2(p)

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
   partidas.append(int(input(f'  Quantos gols na partida{c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)   #soma dos gols?
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
