"""Ce module permet de fournir des fonctions pour le chiffrement de César
"""

import unicodedata, os
import string

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
def cryptage(liste, cle_de_cryptage):           #Fonction qui crypte le texte avec le chiffrement de César
    alphabet = string.ascii_lowercase           #On créé une chaîne de caractères qui contient l'alphabet
    for indice in range(len(liste)):            #On parcourt la liste de mots à crypter
        index = alphabet.find(liste[indice])    #On récupère la position dans l'alphabet de la lettre issu de la liste
        decalage = index + cle_de_cryptage      #On récupère le décalage souhaité en fonction de la clé de cryptage
        if decalage > 25:                       #Les indices de l'alphabet vont de 0 à 25, on veut rester dans cette marge
            decalage = decalage - 26            #En retranchant 26 on revient au début de l'alphabet
        elif decalage < -26:                    #Si la clé est négative, décalage vers la gauche dans l'alphabet
            decalage = decalage + 25            #On rajoute 25, pour rester dans l'alphabet
        new_character = alphabet[decalage]      #La lettre cryptée est prise dans l'alphabet avec sa nouvelle position
        liste[indice] = new_character           #La lettre initiale est remplacée par la lettre cryptée.
    return liste                                #On retourne la liste crypté

def decryptage(cle,fichier="message_encrypte.txt"):
    import string
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    liste_texte = lire_fichier(fichier)

    for i in range(len(liste_texte)):
        for lettre in liste_alphabet:
            if liste_texte[i].lower() == lettre:
                index_original = alphabet.index(lettre)
                index_dechiffre = index_original - cle
                if index_dechiffre < 0:
                    index_dechiffre %= 26
                liste_texte[i] = alphabet[index_dechiffre]
                break
    texte=""
    for i in liste_texte:
        texte += i
    print(texte)
    return texte

#deviner si le texte est francais grâce à un dictionnaire trouvé sur https://github.com/chrplr/openlexicon/blob/master/datasets-info/Liste-de-mots-francais-Gutenberg/liste.de.mots.francais.frgut.txt
def prévoir_bon_texte(liste_lettres):
    score=0
    texte = ''.join(liste_lettres)
    # lire le dico (preciser l’encoding pour les accents)
    f = open("liste.de.mots.francais.frgut.txt", "r", encoding='utf-8')
    # recuperation des mots sous forme de liste
    mots = f.read().split("\n")
    f.close()
    for i in mots:
        if i in texte:
            score+=1
    #on compte le nombre de mots dans le texte
    nb_mots=len(texte.split(" "))
    #le texte est francais si plus de 80% des mots sont détectés comme francais
    if score>0.8*nb_mots:
        return True
    else:
        return False