"""---------------Mini-Projet A - Chiffrement de César----------------------

    - Kilian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
"""

from fonctions import *

#PROGRAMME PRINCIPAL
if __name__ == "__main__":

    print("\nBienvenue sur le chiffrement de César")

    # L'utilisateur choisit : crypter (0) ou décrypter (1).
    choix = choix_utilisateur(1)

    # Si l'utilisateur veut crypter un message
    if choix == "0":

        # Choix entre saisir un message (1) ou lire un fichier (0)
        console_ou_fichier = choix_utilisateur(2)

        if console_ou_fichier == "0":  # Lecture fichier
            fichier = input("Spécifiez le fichier à crypter: ")  # Nom du fichier
            liste = lire_fichier(fichier)  # Conversion en liste

        elif console_ou_fichier == "1":  # Saisie du message
            liste = list(input("Écrivez votre message: "))  # Saisie et conversion

        # L'utilisateur entre la clé de chiffrement
        cle = choix_cle()

        liste_crypte = cryptage(liste, cle)  # Chiffrement
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)  # Affichage

        # Proposition de mise à jour du fichier
        maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
        if maj1 == "1":
            # Écriture du message chiffré dans le fichier message.txt
            ecrire_fichier(liste_crypte, "message.txt")
            print("Le fichier a été mis à jour ! ")

    # Si l'utilisateur veut décrypter un message
    elif choix == "1":

        # Demande si l'utilisateur connaît la clé de déchiffrement
        cle_connue = choix_utilisateur(3)

        # Si la clé est connue
        if cle_connue == "1":

            cle = choix_cle()  # Saisie

            fichier = input("Spécifier le fichier à décrypter: ")  # Nom du fichier
            liste = lire_fichier(fichier)  # Lecture du fichier
            texte_decrypte = decryptage(cle, liste)  # Déchiffrement du message

            print("\nVotre message décrypté est le suivant:")
            print(texte_decrypte)  # Affichage du message déchiffré

            # Proposition de mise à jour du fichier
            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                # Écriture du message déchiffré dans le même fichier
                ecrire_fichier(texte_decrypte, fichier)
                print("Le fichier a été mis à jour ! ")

        # Si la clé est inconnue
        elif cle_connue == "0":

            fichier = input("Spécifier le fichier à décrypter en brute force: ")  # Nom du fichier
            liste = lire_fichier(fichier)  # Lecture du fichier
            # Brute force : essai de toutes les clés possibles, on récupère le message
            message = brute_force(liste)[1]

            # Proposition de mise à jour
            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                # Écriture du message déchiffré dans le fichier
                ecrire_fichier(message, fichier)
                print("Le fichier a été mis à jour ! ")