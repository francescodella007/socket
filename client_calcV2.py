import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005

# Input dell'utente
primoNumero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")
secondoNumero = float(input("Inserisci il secondo numero: "))

# Creazione del dizionario e conversione in formato JSON
messaggio = {
    "primoNumero": primoNumero,
    "operazione": operazione,
    "secondoNumero": secondoNumero
}
messaggio_json = json.dumps(messaggio)

# Creazione del socket TCP del client con 'with'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connessione al server
    s.connect((SERVER_IP, SERVER_PORT))
    
    # Invio del messaggio
    s.sendall(messaggio_json.encode('utf-8'))
    print("Dati inviati al server per il calcolo...")
    
    # Ricezione della risposta dal server
    data = s.recv(1024)
    
    # Decodifica della risposta JSON
    risposta_json = json.loads(data.decode('utf-8'))
    
    # Stampa del risultato
    print(f"\nIl risultato del calcolo è: {risposta_json['risultato']}")