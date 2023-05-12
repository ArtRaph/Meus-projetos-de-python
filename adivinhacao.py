import random

def jogar():

    print("******************************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("******************************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade: ") 
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite aqui: "))
    while (nivel <= 3):
        if(nivel == 1):
            total_tentativas = 20
        elif (nivel == 2):
                total_tentativas = 10
        elif (nivel == 3):
            total_tentativas = 5
        else:
            print("Pow, parceiro faz direito aí")
            continue   
        for rodadas in range (1, total_tentativas + 1):
            print("Tentativas {} de {}".format(rodadas, total_tentativas))
            chute_str= input("Digite um número entre 1 e 100: ")
            chute = int(chute_str)
            print('Seu número foi ', chute)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100!")    
                continue

            acertou = chute == numero_secreto
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto


            if (acertou):
                print("Você acertou!")
                break
            else:
                if (maior):
                    print("Você errou! Seu número é maior do que o número secreto")
                elif (menor):
                    print("Você errou! Seu número é menor do que o número secreto") 
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        print("Seu total de pontos foi: {}".format(pontos))
        print("Fim de jogo")
if(__name__ == "__main__"):
    jogar()
    