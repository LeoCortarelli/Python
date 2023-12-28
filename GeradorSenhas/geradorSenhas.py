import random  # BIBLIOTECA QUE USAREMOS PARA FAZER A ESCOLHA ALEATORIA
import string  # E UM MODULO PARA FACILITAR A DIGITAÇÃO DE STRINGS EXEMPLOS

# PARA CRIAR UMA FUNÇÃO USAMOS O (def)
# FUNÇÃO PARA A GERAR A SENHA
def funcaoGerarSenha(len_pass = 8): # PASSANDO POR PARAMETRO (LEN_PASS) QUE E O TAMANHO DA SENHA
    ascii_options = string.ascii_letters  # GERA LETRAS 
    number_options = string.digits        # GERA NUMEROS
    punt_options = string.punctuation     # GERA CARACTERES ESPECIAIS
    
    options = ascii_options + number_options + punt_options # AGRUPANDO AS VARIAVEIS
    # EX: "oi" + "123" = "oi123"
    
    password_user = "" # VARIAVEL PARA ARMAZENAR O digit
    for i in range(0, len_pass):
        digit = random.choice(options)  # RETORNA UMA LISTA 
        password_user = password_user + digit # ELE VAI COLOCANDO CARACTER POR CARACTER ATE TERMINAR O FOR
        
    return password_user


# O PROGRAMA COMEÇA AQUI, ESSE E O EX: MAIN
resp_usuario = input("Quantos digitos na senha ? ")

if resp_usuario.isdigit(): # VERIFICANDO SE O USUARIO DIGITOU UM NUMERO
    resp_usuario = int(resp_usuario)
else:
    print("Entrada invalida")
    quit()
    
resposta = funcaoGerarSenha(len_pass = resp_usuario)
print(f"Senha gerada: \n {resposta}")