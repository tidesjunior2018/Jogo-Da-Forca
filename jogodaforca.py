import random
'''
Faça um jogo da forca.
'''

lista=['GARRAFA','PRATELEIRA','PAREDE','CALENDÁRIO','GATO','CACHORRO']
chances=6
tentativas=0
estadoinicial=["_"]*len(lista)
palavra=random.choice(lista)
print(estadoinicial)