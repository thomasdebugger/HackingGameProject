# Test de socket client basique #

import socket # on importe le module
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
 
# definition des informations :
Host = 'localhost'
Port = 15550
 
# on se connecte sur le serveur avec les informations ci-dessus
# assurez-vous d'avoir mis en marche le serveur !
Sock.connect((Host,Port))
 
# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
while True:
        msg = input('>> ')  # on rentre des donnees
        Sock.send(msg.encode()) # on envoie ces donnees
 
# regardez ce qui se passe du cote serveur.
