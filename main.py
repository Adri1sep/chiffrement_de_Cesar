
'''---------------Mini-Projet A - Chiffrement de César----------------------

    - Kilian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
'''

#PROGRAMME PRINCIPAL

from fonctions import *

#PROGRAMME PRINCIPAL
if __name__ == "__main__":

    print("\nBienvenue sur le chiffrement de César")

    while True:
        choix = input("\nVoulez-vous crypter (0) ou décrypter (1)? ")
        if choix in ("0", "1"):
            break
        print("Veuillez entrer 0 ou 1.")

    if choix == "0":
        while True:
            console_ou_fichier = input("Voulez-vous crypter un fichier ou écrire votre message ? Fichier (0) / Écrire (1) : ")
            if console_ou_fichier in ("0", "1"):
                break
            print("Veuillez entrer 0 ou 1.")

        if console_ou_fichier == "0":
            fichier = input("Spécifiez le fichier à crypter: ")         #message.txt
            liste = lire_fichier(fichier)

        elif console_ou_fichier == "1":
            liste = list(input("Ecrivez votre message: "))
            # print("message en liste", liste)

        cle_str = input("Rentrez votre clé de cryptage : ")
        while not cle_str.isdigit():
            print("Veuillez entrer un nombre entier.")
            cle_str = input("Rentrez votre clé de cryptage : ")
        cle = int(cle_str)

        liste_crypte = cryptage(liste, cle)
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)
        maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
        if maj1 == "1":
            ecrire_fichier(liste_crypte, "message.txt")
            print("Le fichier a été mis à jour ! ")

    elif choix == "1":
        while True:
            cle_connue = input("Connaissez vous la clé de décryptage? Oui (1) / Non (0): ")
            if cle_connue in ("0", "1"):
                break
            print("Veuillez entrer 0 ou 1.")

        if cle_connue == "1":
            cle_str = input("Quelle est votre clé de décryptage? ")
            while not cle_str.isdigit():
                print("Veuillez entrer un nombre entier.")
                cle_str = input("Quelle est votre clé de décryptage ? ")
            cle = int(cle_str)

            fichier = input("Spécifier le fichier à décrypter: ")
            liste = lire_fichier(fichier)
            texte_decrypte = decryptage(cle, liste)

            print("\nVotre message décrypté est le suivant:")

            print(texte_decrypte)

            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                ecrire_fichier(texte_decrypte, fichier)
                print("Le fichier a été mis à jour ! ")


        elif cle_connue == "0":

            fichier = input("Spécifier le fichier à décrypter en brute force: ")
            liste = lire_fichier(fichier)
            message = brute_force(liste)[1]

            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                ecrire_fichier(message, fichier)
                print("Le fichier a été mis à jour ! ")