from socket import *
from constCS import *
from datetime import datetime
import threading
import random

NUM_REQUISICOES = 1000
NUM_THREADS = 50

def enviarRequisicao(id):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))

        num = random.randint(1, 100)
        msg = f'num: {num}'.encode()

        t1 = datetime.now()
        s.send(msg)
        data = s.recv(1024)
        t2 = datetime.now()

        print(f"[Thread {id}] {data.decode()} | Tempo: {t2 - t1}")

        s.close()

    except Exception as e:
        print(f"Erro thread {id}: {e}")


def benchmark():
    threads = []
    t_inicio = datetime.now()

    for i in range(NUM_REQUISICOES):
        t = threading.Thread(target=enviarRequisicao, args=(i,))
        threads.append(t)
        t.start()

        # controla paralelismo
        if len(threads) >= NUM_THREADS:
            for t in threads:
                t.join()
            threads = []

    # garante finalização
    for t in threads:
        t.join()

    t_fim = datetime.now()
    print("\n===== RESULTADO =====")
    print(f"Total de requisições: {NUM_REQUISICOES}")
    print(f"Tempo total: {t_fim - t_inicio}")


if __name__ == "__main__":
    benchmark()