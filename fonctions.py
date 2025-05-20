"""Ce module permet de fournir des fonctions pour le chiffrement de César
"""

import unicodedata, os

#enlever les accents
def enlever_caracteres_speciaux(mot):
    # Solution obtenue sur https://www.geeksforgeeks.org/how-to-remove-string-accents-using-python-3/
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word if not unicodedata.combining(char)])

#ouvrir le fichier et renvoyer la liste, exemple lire_fichier("texte_code.txt")
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

#écrire dans le fichier le contenu
def ecrire_fichier(contenu, fichier):
    # tester si le fichier existe
    if not os.path.isfile(fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {fichier} !')
    #lire le fichier
    f = open(fichier, "w", encoding='utf-8')
    #enlever le contenu
    f.truncate()
    #écrire le nouveau
    f.seek(0)
    f.write(contenu)
    f.close()

#Fonction qui crypte le texte en entrée:
def cryptage(liste, cle_de_cryptage):
    # texte = "motdepasse"
    # texte_chiffre = list(texte)
    # cle_de_chiffrage = 5
    alphabet = string.ascii_lowercase
    # print("alphabet: ", alphabet)

    for indice in range(len(liste)):
        # print("indice", indice)
        # print("texte_chiffre[indice]", texte_chiffre[indice])
        index = alphabet.find(liste[indice])
        # print("Index", index)
        decalage = index + cle_de_cryptage
        if decalage > 25:
            decalage = decalage - 26
        elif decalage < -26:
            decalage = decalage + 25

        new_character = alphabet[decalage]
        # print("new_character", new_character)
        liste[indice] = new_character
    return liste

def decryptage(cle,fichier="message_encrypte.txt"):
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    cle %= 26
    liste_texte = lire_fichier(fichier)

    for i in range(len(liste_texte)):
        for j in liste_alphabet:
            if liste_texte[i].lower() == j:
                liste_texte[i] = alphabet[liste_alphabet.index(j) - cle]
    texte=""
    for i in liste_texte:
        texte += i
    print(texte)
    return texte
