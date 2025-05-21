
'''---------------Mini-Projet A - Chiffrement de César----------------------

    - Kilian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
'''

from fonctions import *

#PROGRAMME PRINCIPAL
if __name__ == "__main__":

    print("\nBienvenue sur le chiffrement de César")

    choix = int(input("\nVoulez crypter (1) ou décrypter (0)? "))

    if choix == 1:
        cle = int(input("Rentrez votre clé de cryptage: "))
        fichier = input("Spécifiez le fichier à crypter: ")         #message.txt
        liste = lire_fichier(fichier)
        # print(liste)
        liste_crypte = cryptage(liste, cle)
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)
        maj1=input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
        if maj1 == "1":
            ecrire_fichier(liste_crypte,fichier)

    elif choix == 0:
        cle_connue = int(input("Connaissez vous la clé de décryptage? Oui (1) / Non (0): "))
        if cle_connue == 1:
            cle = int(input("Quelle est votre clé de décryptage? "))
            fichier = input("Spécifier le fichier à décrypter: ")
            texte_decrypte = decryptage(cle,fichier)
            print("\nVotre message décrypté est le suivant:")
            print(texte_decrypte)
            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
            if maj1 == "1":
                ecrire_fichier(texte_decrypte, fichier)

        elif cle_connue == 0:
            fichier = input("Spécifier le fichier à décrypter en brute force: \n")
            message=brute_force(fichier)[1]
            maj1 = input("Voulez-vous mettre à jour le fichier texte avec cette version? Oui(1) / Non (0): ")
            if maj1 == "1":
                ecrire_fichier(message, fichier)