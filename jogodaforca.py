import random
'''
Faça um jogo da forca.
'''

lista=['GARRAFA','PRATELEIRA','PAREDE','CALENDÁRIO','GATO','CACHORRO']
chances=6
tentativas=0
palavra=random.choice(lista)
letrasrepetidas=[]
estadoinicial=["_"]*len(palavra)
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
    print(estadoinicial)   
    print(f'\nChances = {chances}')
    print(f'Tentativas = {tentativas}')
    
    print(f'Letras Repetidas :',end=" ")
    for letra1 in letrasrepetidas:
        print(letra1,end=" ")
if tentativas==chances:
    print('\nVocê perdeu!!!')
    print('\nVocê acabou o numero de tentativas.')
    print(f'A palavra escolhida era {palavra}')
else:
    print('\nVocê ganhou!!!')
        
print('\n\nFIM DO JOGO DA FORCA!!!')