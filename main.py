
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
        fichier = input("Spécifiez le fichier à crypter: ")         #texte_code.txt
        liste = lire_fichier(fichier)
        # print(liste)
        liste_crypte = cryptage(liste, cle)
        print("\nVotre message crypté est le suivant:")
        print(liste_crypte)

    elif choix == 0:
        cle_connue = int(input("Connaissez vous la clé de décryptage? Oui (1) / Non (0): "))
        if cle_connue == 1:
            cle = int(input("Quelle est votre clé de décryptage? "))
            fichier = input("Spécifier le fichier à décrypter: ")
            texte_decrypte = decryptage(cle)
            print("\nVotre message décrypté est le suivant:")
            print(texte_decrypte)
        elif cle_connue == 0:
            fichier = input("Spécifier le fichier à décrypter en brute force: \n")
            brute_force(fichier)