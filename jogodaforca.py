import random
'''
Faça um jogo da forca.
'''

lista=['GARRAFA','PRATELEIRA','PAREDE','CALENDÁRIO','GATO','CACHORRO','COMPUTADOR','PORTA','ESTANTE','TELEVISÃO']
chances=6
tentativas=0
palavra=random.choice(lista)
letrasrepetidas=[]
estadoinicial=["_"]*len(palavra)
print('='*67)
print('|BEM VINDO AO JOGO DA FORCA FEITO POR ARISTIDES DUARTE MARQUES JR.|')
print('='*67)
print()
print('Você tem 6 tentativas para acertar a palavra sorteada')
print()
print('A palavra que foi sorteada foi:',end=" ")
print(estadoinicial)

while((tentativas<chances) and ("".join(estadoinicial)!=palavra)):
    letra=input('\n\nDigite uma letra: ').upper()
    while letra in letrasrepetidas:
        print('\nVocê já escolheu essa letra.Escolha outra:')
        letra=input('Digite uma letra: ').upper()
    letrasrepetidas.append(letra)
    
    if letra in palavra:            
        print(f'VOCÊ ACERTOU A LETRA {letra}') 
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estadoinicial[i]=letra
    else:
        print(f'VOCÊ ERROU A LETRA {letra}')
        tentativas+=1
    
    print()
    print('A palavra que foi sorteada foi:',end=" ")
    print(estadoinicial)   
    print(f'\nChances = {chances}')
    print(f'Tentativas = {tentativas}')
    
    print(f'Letras Repetidas :',end=" ")
    for letra1 in letrasrepetidas:
        print(letra1,end=" ")
    print()
    if tentativas==1:
        print(' --------')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|       /')
    if tentativas==2:
        print(' --------')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|       / \\')
    if tentativas==3:
        print(' --------')
        print('|        ')
        print('|     -- ')
        print('|        ')
        print('|       / \\')
    if tentativas==4:
        print(' --------')
        print('|        ')
        print('|      -- --')
        print('|        ')
        print('|       / \\')
    if tentativas==5:
        print(' --------')
        print('|        ')
        print('|      --|--')
        print('|        |')
        print('|       / \\')
    if tentativas==6:
        print(' --------')
        print('|        0')
        print('|      --|--')
        print('|        |')
        print('|       / \\')
if tentativas==chances:
    print('\nVocê perdeu!!!')
    print('\nVocê acabou o numero de tentativas.')
    print(f'A palavra escolhida era {palavra}')
else:
    print('\nVocê ganhou!!!')
        
print('\n\nFIM DO JOGO DA FORCA!!!')