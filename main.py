
'''---------------Mini-Projet A - Chiffrement de César----------------------

    - Kilian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
'''

#PROGRAMME PRINCIPAL

from fonctions import *
import string

#PROGRAMME PRINCIPAL
if __name__ == "__main__":
    print("Bienvenue sur le chiffrement de César")
    int(input("\nVoulez crypter (1) ou décrypter (0): "))
    cle = int(input("Quelle est votre clé de décryptage: "))
    decryptage(cle)
    # liste = lire_fichier("texte_code.txt")
    # print(liste)
    """texte = "motdepasseacrypter"
    liste = list(texte)
    liste_crypte = cryptage(liste, cle)

# texte = "motdepasseacrypter"
# liste = list(texte)

