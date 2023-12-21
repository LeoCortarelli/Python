import random  #Importação para fazer o numero sorteado

print("Bem vindo ao jogo de advinhação do Leo")
numeroLimite = input("Digite o numero maximo para o desafio: ")
#Por padrao a variavel vai vir como String

if numeroLimite.isdigit(): # isdigit() VERIFICA SE O USUARIO DIGITOU UM NÚMERO
    numeroLimite = int(numeroLimite) # Transformndo para inteiro
else: 
    print("Erro valor informado não é um número favor execute o programa novamente")
    quit()
    
random_numero = random.randint(0, numeroLimite) # random.randint Ele ira sortear um numero para para o usuario adivinhar

tentativas = 0

while True:
    numChute = input("Adivinhe o numero: ") 
    if numChute.isdigit():
        numChute = int(numChute)
    else:
        print("Erro valor informado não é um número favor informe um numero !!")
        continue  # O continue ignora todo o codigo abaixo e volta para o começo do while

    tentativas = tentativas + 1
    
    if numChute == random_numero:
        print("Acertou!")
        break  # break quebra o loop do while
    elif numChute > random_numero:
        print("Chutou alto, o numero randomico e menor que isso...")
    else:
        print("Chutou baixo, o numero randomico e maior que isso...")
    
print("N* de tentativas: "+ str(tentativas)) # o str() printa a variavel