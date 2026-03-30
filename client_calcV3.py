import socket
import json

HOST = '127.0.0.1'
PORT = 65432  # Deve coincidere ESATTAMENTE con la porta del tuo file sistema.py

def avvia_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # 1. Il client si CONNETTE (non fa bind o listen)
            s.connect((HOST, PORT))
            print("Connesso al Server Calcolatrice!")
            
            # 2. Chiediamo i dati all'utente
            primo = float(input("Inserisci il primo numero: "))
            operazione = input("Inserisci l'operazione (+, -, *, /): ")
            secondo = float(input("Inserisci il secondo numero: "))
            
            # 3. Impacchettiamo i dati in un dizionario
            dati_da_inviare = {
                "primoNumero": primo,
                "operazione": operazione,
                "secondoNumero": secondo
            }
            
            # 4. Trasformiamo in stringa JSON, codifichiamo in byte e spediamo
            messaggio_json = json.dumps(dati_da_inviare)
            s.sendall(messaggio_json.encode('utf-8'))
            
            # 5. Aspettiamo il risultato dal server e lo stampiamo
            risposta = s.recv(1024).decode('utf-8')
            print(f"\n{risposta}")
            
        except ConnectionRefusedError:
            print("Errore di connessione: assicurati di aver avviato PRIMA il server!")
        except ValueError:
            print("Errore: devi inserire dei numeri validi.")

if __name__ == "__main__":
    avvia_client()