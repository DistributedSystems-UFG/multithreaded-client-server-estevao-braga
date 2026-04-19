from socket  import *
from constCS import * #-
from datetime import datetime

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

while True:
    print('===== Escolha uma opção ========')
    print("1 - Enviar um número para o servidor")
    print("2 - Calcular a média dos números")
    print("3 - Terminar conexão")

    x = int(input())

    if x == 1:
        num = int(input('Digite um número inteiro: '))
        msg = str.encode(f'num: {num}')
        t1 = datetime.now()
        s.send(msg)  
        data = s.recv(1024) 
        t2 = datetime.now()
        print(f'Resposta do Servidor: {bytes.decode(data)}')            # print the result
        print(f'Tempo de resposta: {t2-t1}')
    elif x == 2:
        msg = str.encode('get media')
        t1 = datetime.now()
        s.send(msg)  
        data = s.recv(1024) 
        t2 = datetime.now()
        print(f'Resposta do Servidor: {bytes.decode(data)}')            # print the result
        print(f'Tempo de resposta: {t2-t1}')
    else:
        s.close()
        break
