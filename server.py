from socket  import *
from constCS import * #-

import re

def extrair_numero(s):
    match = re.search(r"^num:\s*(-?\d+(?:\.\d+)?)$", s)
    if match:
        return float(match.group(1)) if '.' in match.group(1) else int(match.group(1))
    return None

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client

tot, n = 0, 0

while True:                # forever
    data = conn.recv(1024)   # receive data from client
    if not data: 
        print("Desconectando...")
        break 
    data = bytes.decode(data)

    if data == 'get media':
        if n == 0:
            print("Sem Média...")
            conn.send(str.encode("Sem números para calcular a média"))
        else:
            print("Enviando Média...")
            conn.send(str.encode(f'Média: {(tot/n):.2f}'))
    else:
        num = extrair_numero(data)
        if num is not None:
            tot += num
            n += 1
        conn.send(str.encode(f'Número {num} recebido'))
        print(f'Número {num} recebido')
        
conn.close()               # close the connection
