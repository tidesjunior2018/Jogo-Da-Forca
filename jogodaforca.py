import random
'''
Faça um jogo da forca.
'''

lista=['GARRAFA','PRATELEIRA','PAREDE','CALENDÁRIO','GATO','CACHORRO']
chances=6
tentativas=0
palavra=random.choice(lista)
letrasescolhidas=[]
estadoinicial=["_"]*len(palavra)
print(palavra)
print(estadoinicial)

while(tentativas<chances):
    letra=input('Digite uma letra: ').upper()
    letrasescolhidas.append(letra)
    
    if letra in palavra:            
        print(f'VOCÊ ACERTOU A LETRA {letra}') 
        estadoinicial=letra
    else:
        print(f'VOCÊ ERROU A LETRA {letra}')
        tentativas+=1
    print(f'Chances = {chances}')
    print(f'Tentativas = {tentativas}')
    print
    print(estadoinicial)

#print('=',*30)
print('Fim do programa!!!')
#print('=',*30)
parei o video 22 min