import random,os

num_secreto = random.randint(1,100)
tentativas = 0
while True:
    numero = int(input('Tente adivinha o numero secreto: '))
    os.system('cls' or 'clear')
    tentativas +=1
    if(numero==num_secreto):
        print(f'Parabéns você acertou o Numero Secreto')
        print(f'/n Em {tentativas} Tentativas')
        break
    elif(numero<num_secreto):
        print(f'O numero secreto é Maior - {tentativas} Tentativas ')
    else:
        print(f'O numero Secreto é Menor - {tentativas} Tentativas')
        
