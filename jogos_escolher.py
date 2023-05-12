import forca
import advinhacao

print("******************************************")
print("***Escolha seu jogo!***")
print("******************************************")
print("Jogo da forca(1) Jogo da adivinha(2) ")
jogo = int(input("Digite:"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    advinhacao.jogar()