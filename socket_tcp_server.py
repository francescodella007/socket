import socket

HOST = '127.0.0.1'  # Indirizzo IP locale
PORT = 65432        # Porta di ascolto

# 1. Apre il socket del server con 'with'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server in ascolto...")
    
    # 2. Accetta la connessione del client (il codice si blocca qui finché non arriva qualcuno)
    conn, addr = s.accept()
    
    # 3. Usa un altro 'with' per gestire la connessione specifica col client
    with conn:
        print(f"Client connesso da: {addr}")
        while True:
            data = conn.recv(1024) # Riceve i dati
            if not data:
                break              # Se non ci sono più dati, esce dal ciclo
            print(f"Ricevuto dal client: {data.decode()}")
            conn.sendall(data)     # Rimanda indietro gli stessi dati (Echo)

# Fine del blocco: i socket 's' e 'conn' sono già stati chiusi in automatico.