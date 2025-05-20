"""Ce module permet de fournir des fonctions pour le chiffrement de César
"""

import unicodedata, os

#enlever les accents
def enlever_caracteres_speciaux(mot):
    # Solution obtenue sur https://www.geeksforgeeks.org/how-to-remove-string-accents-using-python-3/
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word if not unicodedata.combining(char)])

#ouvrir le fichier et renvoyer la liste
def lire_fichier(fichier):
    #tester si le fichier existe
    if not os.path.isfile(fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {fichier} !')
    #lire le fichier
    f = open(fichier, "r", encoding='utf-8')
    texte_fichier=enlever_caracteres_speciaux(f.read())
    liste=list(texte_fichier)
    f.close()
    return liste

def decryptage(cle,fichier="message_encrypte.txt"):
    import string
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    cle %= 26
    liste_texte = lire_fichier(fichier)

    for i in range(len(liste_texte)):
        for j in liste_alphabet:
            if liste_texte[i] == j:
                liste_texte[i] = alphabet[liste_alphabet.index(j) - cle]
                print(liste_texte)
decryptage(-22,"test_texte.txt")

def decryptage(cle,fichier="message_encrypte.txt"):
    import string
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    cle %= 26
    liste_texte = lire_fichier(fichier)

    for i in range(len(liste_texte)):
        for j in liste_alphabet:
            if liste_texte[i] == j:
                liste_texte[i] = alphabet[liste_alphabet.index(j) - cle]
                print(liste_texte)