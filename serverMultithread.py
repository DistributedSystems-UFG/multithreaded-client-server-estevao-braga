from socket import *
from constCS import *
import re
import threading

lock = threading.Lock()
tot, n = 0, 0

def extrairNumero(s):
    match = re.search(r"^num:\s*(-?\d+(?:\.\d+)?)$", s)
    if match:
        return float(match.group(1)) if '.' in match.group(1) else int(match.group(1))
    return None

def handleClient(conn, addr):
    global tot, n
    print(f"[NOVA CONEXÃO] {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        data = data.decode()

        if data == 'get media':
            with lock:
                if n == 0:
                    response = "Sem números para calcular a média"
                else:
                    response = f"Média: {(tot/n):.2f}"

            conn.send(response.encode())

        else:
            num = extrairNumero(data)

            if num is not None:
                with lock:
                    tot += num
                    n += 1

            conn.send(f"Número {num} recebido".encode())

    conn.close()
    print(f"[DESCONECTADO] {addr}")


s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen()

print("Servidor multithread rodando...")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handleClient, args=(conn, addr))
    thread.start()