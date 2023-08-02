'''
1 - construa melhor o jogo da forca
'''
import random

def menu(lista):
    for i in lista:
        print(f'{i}')

palavras=['impressora','modem','sacola','banco','sofá','cozinha']
palavrasorteada=random.choice(palavras)

while True:
    print()
    lista=menu(['1-Single player','2-Sair','3-Regras do jogo da forca'])
    print()
    op=input('Digite sua opção:')
    if op=='1':
        chances=6
        tentativas=0
        palavrasorteada=random.choice(palavras)
        estadoinicial=['_']*len(palavrasorteada)
        print(palavrasorteada)
        while(tentativas<chances):
            print(estadoinicial)
            letra=input('Digite uma letra: ').lower()
            if letra in palavrasorteada:
                print(f'Você acertou a letra {letra} dentro da palavra sorteada.')
    elif op=='2':
        print('Finalizando o jogo!!!')
        break
print()