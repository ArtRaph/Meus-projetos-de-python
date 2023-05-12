pontos = 1000
chute = int(input('Você tem {} de ponto Qual valor de 100 voce deseja subtrair? '.format(pontos)))


while(chute <=100 ):
    pontos_perdidos = chute
    pontos = pontos - pontos_perdidos
    print("está aqui o calculo que voce quer {}".format(pontos))
    break
else:
    print("Valor nao valido")

