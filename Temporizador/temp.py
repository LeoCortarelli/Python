import time
temp = input("Digite o tempo (EM SEGUNDOS): ")

if temp.isdigit():
    temp = int(temp)
else:
    print("Erro ao digitar um numero")
    quit()
    
# 120 / 60min = 2min
# 150 / 60min = 2min e 30seg


while temp != 0:
    # ESTA FUNÇÃO RETORNA A DIVISAO ELE PEGA (a / b) ele retorna dois resultados o resultado e o resto
    minutos , segundos = divmod(temp, 60) # VC pode colocar ele em duas variaveis
    # SEMPRE NESSA FUNÇÃO A PRIMEIRO RETORNO QUE E O RESULTADO ELE ARMAZENA NA PRIMEIRA VARIAVEL
    # O SEGUNDO RESULTADO ELE VAI ARMAZENAR NA SEGUNDA VARIAVEL

    timer = "{:02d}:{:02d}".format(minutos,segundos) #FORMATANDO PARA MINITOS E SEGUNDOS
    print(timer, end="\r")
    # O (\r) ele reescreve
    time.sleep(1) # ESSA FUNÇÃO DESACELERA O CODIGO
    temp = temp - 1 
    
print("TEMPO ACABOU")