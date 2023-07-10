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
print(palavra)
print(estadoinicial)

while(tentativas<chances):
    letra=input('\n\nDigite uma letra: ').upper()
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
    print(f'Chances = {chances}')
    print(f'Tentativas = {tentativas}')
    
    print(f'Letras Repetidas :')
    for letra1 in letrasrepetidas:
        print(letra1,end=" ")
print('\n')
#print('=',*30)
print('\nFim do programa!!!')
#print('=',*30)
parei no video 31 min