# Test de socket serveur basique #

import socket
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = 'localhost' # l'ip locale de l'ordinateur
Port = 15550    # choix d'un port
 
# on bind notre socket :
Sock.bind((Host,Port))
 
# On est a l'ecoute d'une seule et unique connexion :
Sock.listen(1)
print("Lancement du serveur")
print("En attente de connexion...")
# Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
client, adresse = Sock.accept() # accepte les connexions de l'exterieur
print("L'adresse",adresse,"vient de se connecter au serveur !")
while 1:
        RequeteDuClient = client.recv(255) # on recoit 255 caracteres grand max
        if not RequeteDuClient: # si on ne recoit plus rien
                break
        msg = "Bien reçu :",RequeteDuClient.decode()
        Sock.send(msg.encode())