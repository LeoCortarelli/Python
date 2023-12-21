print("Bem vido ao quiz do Leo")
answer_user = input("Quer começar? (S/N) ") # Variavel recebendo o imput do usuario

if answer_user != "s" :
    quit()                   # o quit ele encerra o programa

pontuacao = 0
print("Começando...")

print("Quem desenvolveu o jogo GTA ? \n (A) Rockstar Games \n (B) Ubsoft \n (C) Activision \n (D) EA \n")
resp1 = input("Resposta: ")

if resp1 == "a":
    print("Correto")
    pontuacao = pontuacao + 1
else:
    print("Incorreto")
    
# PERGUNTA 2

print("Qual e o protagonista do GTA San Andres ? \n (A) Carl Jhon \n (B) Carl Jhonson \n (C) Carl Jaqueline \n (D) Carlos JhonJhon \n")
resp2 = input("Resposta: ")

if resp2 == "b":
    print("Correto")
    pontuacao = pontuacao + 1 
else:
    print("Incorreto")
    
print(f"Quiz acabou... Pontuação: {pontuacao}/2") # o /2 e porque são 2 perguntas que ele pode responder
# (F) antes das aspas para poder colocar a variavel; A variavel deve ser colocada entre {} para funcionar