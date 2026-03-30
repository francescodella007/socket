import socket
import json
from threading import Thread

def ricevi_comandi(sock_service, addr_client):
    with sock_service as sock_client:
        print(f"Connessione stabilita con {addr_client}")
        
        # legge i dati inviati dal client
        data = sock_client.recv(DIM_BUFFER).decode()
        if not data:
            return
            
        data = json.loads(data) # converto i dati da JSON a dizionario Python
        primoNumero = data["primoNumero"]
        operazione = data["operazione"]
        secondoNumero = data["secondoNumero"]
        print(f"{primoNumero} {operazione} {secondoNumero}") # stampo i dati ricevuti per debug    

        if operazione == '+':
            risultato = primoNumero + secondoNumero
        elif operazione == '-':
            risultato = primoNumero - secondoNumero 
        elif operazione == '*':
            risultato = primoNumero * secondoNumero
        elif operazione == '/':
            if secondoNumero != 0:
                risultato = primoNumero / secondoNumero
            else:
                risultato = "Errore: divisione per zero!"
        
        # stampa il messaggio ricevuto
        print(f"Messaggio ricevuto dal client {addr_client}: {data}")

        print("Risultato server: ", risultato) # stampo il risultato per debug
        ris = "Risultato dell'operazione Client: " + str(risultato)
        
        # ERRORE RISOLTO: aggiunto .encode() alla fine della stringa
        sock_client.sendall(f"Messaggio ricevuto dal server {ris}\n".encode())
        
        sock_client.sendall(str(risultato).encode())

def ricevi_connessioni(sock_listen):
    sock_service, address_client = sock_listen.accept() # accetto la connessione
    try:
        Thread(target=ricevi_comandi, args=(sock_service, address_client)).start() # creo un thread
    except Exception as e:
        print(e)

def avvia_server(indirizzo, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
        sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock_server.bind((indirizzo, porta))
        sock_server.listen(5)
        
        print("Server avviato. In attesa del primo client...")

        while True:
            ricevi_connessioni(sock_server)
            print(f"---- Server in ascolto su {indirizzo}:{porta} ----")

# configurazione del server
IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

if __name__ == "__main__":
    avvia_server(IP, PORTA)