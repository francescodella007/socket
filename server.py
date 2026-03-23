import socket

SERVER_IP = "127.0.0.1"  # Indirizzo IP locale (localhost)
SERVER_PORT = 5005       # Porta su cui il server resta in ascolto
BUFFER_SIZE = 1024       # Dimensione massima dei dati ricevuti in un singolo pacchetto

# 1. Creazione del socket UDP
# AF_INET indica l'uso di IPv4, SOCK_DGRAM indica che si usa il protocollo UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Associazione (bind) del socket all'IP e alla porta scelti
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

# 3. Ciclo di ascolto infinito
while True:
    # Ricezione dei dati dal client. Restituisce il messaggio (data) e l'indirizzo del mittente (addr)
    data, addr = sock.recvfrom(BUFFER_SIZE)
    
    # Stampa a schermo del messaggio decodificato
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")
    
    # 4. Invio di una risposta (pong) al mittente
    reply = "pong"
    # Il messaggio va codificato in byte (encode) prima di essere inviato
    sock.sendto(reply.encode(), addr)