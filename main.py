
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

    choix = int(input("\nVoulez-vous crypter (0) ou décrypter (1)? "))

    if choix == 0:
        console_ou_fichier = int(input("Voulez-vous crypter un fichier ou écrire votre message? Fichier (0) / Ecrire (1): "))
        if console_ou_fichier == 0:
            fichier = input("Spécifiez le fichier à crypter: ")         #message.txt
            liste = lire_fichier(fichier)
        elif console_ou_fichier == 1:
            liste = list(input("Ecrivez votre message: "))
            # print("message en liste", liste)

        cle = int(input("Rentrez votre clé de cryptage: "))

        liste_crypte = cryptage(liste, cle)
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)
        maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
        if maj1 == "1":
            ecrire_fichier(liste_crypte, "message.txt")

    elif choix == 1:

        cle_connue = int(input("Connaissez vous la clé de décryptage? Oui (1) / Non (0): "))

        if cle_connue == 1:

            cle = int(input("Quelle est votre clé de décryptage? "))

            fichier = input("Spécifier le fichier à décrypter: ")

            texte_decrypte = decryptage(cle, fichier)

            print("\nVotre message décrypté est le suivant:")

            print(texte_decrypte)

            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                ecrire_fichier(texte_decrypte, fichier)


        elif cle_connue == 0:

            fichier = input("Spécifier le fichier à décrypter en brute force: ")

            message = brute_force(fichier)[1]

            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")

            if maj1 == "1":
                ecrire_fichier(message, fichier)