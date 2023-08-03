'''
1 - construa melhor o jogo da forca
'''
import random

def menu(lista):
    for i in lista:
        print(f'{i}')

palavras=['impressora','modem','sacola','banco','sofá','cozinha']
palavrasorteada=random.choice(palavras)
letrasrepetidas=[]

while True:
    palavrasorteada=random.choice(palavras)
    print()
    lista=menu(['1-Single player','2-Sair','3-Regras do jogo da forca'])
    print()
    op=input('Digite sua opção:')
    if op=='1':
        chances=6
        tentativas=0
        palavrasorteada=random.choice(palavras)
        estadoinicial=['_']*len(palavrasorteada)
        while(tentativas<chances):
            print()
            print(estadoinicial)
            print()
            letra=input('Digite uma letra: ').lower()
            while letra in letrasrepetidas:
                print('você ja escolheu essa letra.Digite outra letra:')
                letra=input('Digite uma letra: ').lower()
            letrasrepetidas.append(letra)
            if letra in palavrasorteada:
                print(f'Você acertou a letra {letra} dentro da palavra sorteada.')
                for i in range(len(palavrasorteada)):
                    if letra==palavrasorteada[i]:
                        estadoinicial[i]=letra
            else:
                print(f'A letra {letra} não está na palavra sorteada')
                tentativas+=1
            print()
            print(f'chances = {chances-tentativas}')
            print(f'tentantivas = {tentativas}')
            print(f'Letras Repetidas = ',end=" ")
            for letra1 in letrasrepetidas:
                print(letra1,end=" ")
            print()
            print()
        if tentativas==chances:
            print("Game Over")
            print(f'A palavra sorteada é = {palavrasorteada}')
        else:
            print("Parabéns!!!.Você decifrou a palavra.")
    elif op=='2':
        print('Finalizando o jogo!!!')
        break
print()