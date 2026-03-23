import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

# Creazione del socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

print("Server Calcolatrice v1.0 in attesa di calcoli...")

while True:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    
    data = data.decode('utf-8')
    dati_json = json.loads(data) # da stringa a un dizionario Python
    
    primoNumero = dati_json["primoNumero"]
    operazione = dati_json["operazione"]
    secondoNumero = dati_json["secondoNumero"]

    print(f"Richiesta da {addr}: {primoNumero} {operazione} {secondoNumero}")

    # Logica della calcolatrice
    risultato = 0
    errore = None

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
            errore = "Impossibile dividere per zero!"
    else:
        errore = "Operazione non riconosciuta!"

    # risposta in un nuovo dizionario
    risposta = {
        "risultato": risultato,
        "errore": errore
    }

    # Trasformiamo la risposta in JSON, poi la inviamo
    risposta_json = json.dumps(risposta)
    s.sendto(risposta_json.encode('utf-8'), addr)