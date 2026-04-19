from socket  import *
from constCS import * #-
from datetime import datetime
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

def enviar_numero():
    global s
    num = randint(0,1000)
    msg = str.encode(f'num: {num}')
    s.send(msg)  
    data = s.recv(1024) 
    print(f'Resposta do Servidor: {bytes.decode(data)}')            # print the result

t1_tot = datetime.now()

for i in range(1000):
    enviar_numero()

msg = str.encode('get media')
s.send(msg)  
data = s.recv(1024) 
print(f'Resposta do Servidor: {bytes.decode(data)}')            # print the result
    
t2_tot = datetime.now()

print(f'Tempo total {t2_tot-t1_tot}')

s.close()
