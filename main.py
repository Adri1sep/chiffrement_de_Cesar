"""---------------Mini-Projet A - Chiffrement de César----------------------

    - Kilian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
"""

#PROGRAMME PRINCIPAL

from fonctions import *

#PROGRAMME PRINCIPAL
if __name__ == "__main__":

    print("\nBienvenue sur le chiffrement de César")

    choix = choix_utilisateur(1)

    if choix == "0":

        console_ou_fichier = choix_utilisateur(2)

        if console_ou_fichier == "0":
            fichier = input("Spécifiez le fichier à crypter: ")         #message.txt
            liste = lire_fichier(fichier)

        elif console_ou_fichier == "1":
            liste = list(input("Écrivez votre message: "))
            # print("message en liste", liste)

        cle = choix_cle()

        liste_crypte = cryptage(liste, cle)
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)
        maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
        if maj1 == "1":
            ecrire_fichier(liste_crypte, "message.txt")
            print("Le fichier a été mis à jour ! ")

    elif choix == "1":

        cle_connue = choix_utilisateur(3)

        if cle_connue == "1":

            cle = choix_cle()

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