import socket
import json

HOST = '127.0.0.1'
PORT = 5005

# Creazione del socket TCP usando il costrutto 'with'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server calcolatrice in attesa di connessioni...")
    
    # Accetta la connessione del client
    conn, addr = s.accept()
    
    # Gestione della connessione con il client con un altro 'with'
    with conn:
        print(f"Connesso con il client: {addr}")
        
        # Riceve i dati
        data = conn.recv(1024)
        if data:
            # Decodifica la stringa byte e la trasforma in un dizionario Python
            messaggio_ricevuto = json.loads(data.decode('utf-8'))
            
            # Estrae le variabili
            primoNumero = messaggio_ricevuto["primoNumero"]
            operazione = messaggio_ricevuto["operazione"]
            secondoNumero = messaggio_ricevuto["secondoNumero"]
            
            # Esegue il calcolo
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
            else:
                risultato = "Errore: operazione non riconosciuta."
            
            # Prepara il risultato in JSON e lo invia al client
            risposta = json.dumps({"risultato": risultato})
            conn.sendall(risposta.encode('utf-8'))
            print("Risultato calcolato e inviato al client.")