import socket

SERVER_IP = "127.0.0.1"  # Indirizzo IP del server (locale in questo caso)
SERVER_PORT = 5005       # La stessa porta configurata nel server
BUFFER_SIZE = 1024       # Dimensione del buffer di ricezione
NUM_MESSAGES = 5         # Numero di messaggi da inviare

# 1. Creazione del socket UDP del client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Ciclo per inviare più messaggi
for i in range(NUM_MESSAGES):
    
    # Preparazione del messaggio da inviare
    message = "ping"
    
    # 3. Invio del messaggio codificato in byte all'indirizzo e porta del server
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Messaggio inviato al server: {message}")
    
    # 4. Attesa e ricezione della risposta dal server
    data, addr = sock.recvfrom(BUFFER_SIZE)
    
    # Stampa della risposta ricevuta
    print(f"Messaggio ricevuto dal server {addr}: {data.decode()}")

# 5. Chiusura finale del socket per liberare le risorse
sock.close()