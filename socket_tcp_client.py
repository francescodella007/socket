import socket

HOST = '127.0.0.1'  # IP del server a cui connettersi
PORT = 65432        # Stessa porta del server

# 1. Apre il socket del client con 'with'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # 2. Si connette al server
    s.connect((HOST, PORT))
    
    # 3. Invia un messaggio (convertito in byte con 'b')
    messaggio = b"Ciao Server!"
    s.sendall(messaggio)
    print("Messaggio inviato!")
    
    # 4. Riceve la risposta dal server
    data = s.recv(1024)

# Fuori dal blocco 'with', il socket del client si chiude da solo.

# Stampa a schermo la risposta decodificata
print(f"Risposta ricevuta dal server: {data.decode()}")