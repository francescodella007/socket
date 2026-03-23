import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

# Creazione del socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("--- CALCOLATRICE UDP v1.0 ---")

while True:
    try:
        primoNumero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione (simbolo +, -, *, /): ")
        secondoNumero = float(input("Inserisci il secondo numero: "))

        messaggio = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }

        messaggio_json = json.dumps(messaggio)
        s.sendto(messaggio_json.encode("utf-8"), (SERVER_IP, SERVER_PORT))

        # risultato dal server in attesa
        data, addr = s.recvfrom(1024)
        
        # Decodifichiamo e apriamo il JSON ricevuto
        risposta = json.loads(data.decode("utf-8"))

        # controllo se c'è un errore
        if risposta["errore"]:
            print(f"ATTENZIONE: {risposta['errore']}\n")
        else:
            print(f"RISULTATO: {risposta['risultato']}\n")

        # Chiediamo se vuole continuare
        continua = input("Vuoi fare un altro calcolo? (s/n): ")
        if continua.lower() != 's':
            print("Arrivederci!")
            break

    except ValueError:
        print("Errore: Inserisci solo numeri validi!\n")

# Chiusura del socket
s.close()