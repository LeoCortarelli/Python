import random

pontosUsuario = 0
pontosComputador = 0

opcao = ["r", "t", "p"] #Listas 

while True:
    opcaoUsuario = input("Escolha R(Rocha)/T(Tesoura)/P(Papel) ou Q para sair.").lower()
            # O .lower() faz com que todos os caracteres que sejam transformados na sua versão MINUSCULA
            
    if opcaoUsuario == "q":
        break
    
    if opcaoUsuario not in opcao:
        continue
    
    escolheComputador = random.randint(0, 2)
    # 0:R , 1:T , 2:P
    opcaoDoComputador = opcao[escolheComputador]
    
    print("O computador escolheu "+ str(opcaoDoComputador))
    
    if opcaoUsuario == opcaoDoComputador:
        print("Empate!!")
    elif opcaoUsuario == "r" and opcaoDoComputador == "t":
        print("Você ganhou !!")
        pontosUsuario = pontosUsuario + 1
    elif opcaoUsuario == "p" and opcaoDoComputador == "r":
        print("Você ganhou !!")
        pontosUsuario = pontosUsuario + 1
    elif opcaoUsuario == "t" and opcaoDoComputador == "p":
        print("Você ganhou !!")
        pontosUsuario = pontosUsuario + 1
    else:
        print("Você perdeu !!")
        pontosComputador = pontosComputador + 1
    
print("\n\n")
print("Sua pontuação foi: " + str(pontosUsuario))
print("Pontuação do computador: "+ str(pontosComputador))
    
if pontosUsuario > pontosComputador:
    print("Vitoria !!")
elif pontosUsuario == pontosComputador:
    print("Empate !!")
else:
    print("Derrota !!")