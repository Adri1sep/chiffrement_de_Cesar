"""Ce module permet de fournir des fonctions pour le chiffrement de César
"""

import unicodedata, os, string

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

# Écrire dans le fichier le contenu
def ecrire_fichier(contenu, fichier):
    # tester si le fichier existe
    if not os.path.isfile(fichier):
        raise RuntimeError(f'Je ne trouve pas le fichier {fichier} !')
    #lire le fichier
    f = open(fichier, "w", encoding='utf-8')
    #enlever le contenu
    f.truncate()
    # Ecrire le nouveau
    f.seek(0)
    f.write(contenu)
    f.close()
#Fonction qui crypte le texte en entrée :
def cryptage(liste, cle_de_cryptage):           #Fonction qui crypte le texte avec le chiffrement de César
    import string
    alphabet = string.ascii_lowercase           #On crée une chaîne de caractères qui contient l'alphabet
    if cle_de_cryptage < 0 or cle_de_cryptage > 25:
        cle_de_cryptage %= 26
    for indice in range(len(liste)):
        liste[indice] = enlever_caracteres_speciaux(liste[indice])
        #On parcourt la liste de mots à crypter
        if liste[indice].lower() in alphabet:           #Si la lettre est dans l'alphabet, permet de ne pas crypter les ponctuations
            index = alphabet.find(liste[indice].lower())    #On récupère la position dans l'alphabet de la lettre issu de la liste
            # print("Indice dans la liste : ", indice, "Lettre", liste[indice], "Index alphabet", index)
            decalage = index + cle_de_cryptage      #On récupère le décalage souhaité en fonction de la clé de cryptage
            if decalage > 25:                       #Les indices de l'alphabet vont de 0 à 25, on veut rester dans cette marge
                decalage %= 26                      #En retranchant 26 on revient au début de l'alphabet
            # elif decalage < -26:                    #Si la clé est négative, décalage vers la gauche dans l'alphabet
            #     decalage = decalage + 25            #On rajoute 25, pour rester dans l'alphabet
            new_character = alphabet[decalage]      #La lettre cryptée est prise dans l'alphabet avec sa nouvelle position
            liste[indice] = new_character           #La lettre initiale est remplacée par la lettre cryptée.
    texte_crypte = ""                               #On crée une chaîne de caractères vides destinée à recevoir le msg
    for i in liste:                                 #On parcourt notre liste
        texte_crypte += i                           #Chaque caractère de la liste est ajouté à notre texte
    return texte_crypte                             #On retourne la chaine cryptée


def decryptage(cle, liste):
    # On fait une copie de la liste de caractères pour ne pas modifier l'originale
    liste = liste.copy()
    # On définit l'alphabet en minuscules (de "a" à "z")
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    # On s'assure que la clé est comprise entre 0 et 25.
    if cle < 0 or cle > 25:
        cle %= 26  # Pour que la clé reste dans les bornes de l'alphabet
    # Parcours de chaque caractère de la liste
    for i in range(len(liste)):
        # On compare chaque caractère à chaque lettre de l'alphabet
        for lettre in liste_alphabet:
            # Si le caractère (en minuscule) correspond à une lettre de l'alphabet
            if liste[i].lower() == lettre:
                index_original = alphabet.index(lettre)  # Position de la lettre dans l'alphabet
                index_dechiffre = index_original - cle   # On recule de 'cle' positions
                # Si on tombe en-dessous de 0, on revient à la fin de l'alphabet (rotation circulaire)
                if index_dechiffre < 0:
                    index_dechiffre %= 26
                # On remplace la lettre dans la liste par la lettre déchiffrée
                liste[i] = alphabet[index_dechiffre]
                break  # On sort de la boucle sur l'alphabet une fois qu'on a trouvé la correspondance
    # On reconstruit le texte final à partir de la liste de caractères modifiée
    texte = ""
    for i in liste:
        texte += i
    return texte  # On retourne le texte déchiffré


#deviner si le texte est francais grâce à un dictionnaire trouvé sur https://github.com/chrplr/openlexicon/blob/master/datasets-info/Liste-de-mots-francais-Gutenberg/liste.de.mots.francais.frgut.txt
def prevoir_bon_texte(liste_lettres):
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
    if score>0.9*nb_mots:
        return True
    else:
        return False


def brute_force(liste):
    # Récupère l'alphabet en minuscules ("a" à "z")
    alphabet = string.ascii_lowercase
    liste_alphabet = list(alphabet)
    # On teste toutes les clés possibles (de 0 à 25).
    for i in range(len(liste_alphabet)):
        # On tente de décrypter avec la clé i, et on vérifie si le texte résultant semble correct
        if prevoir_bon_texte(decryptage(i, liste)):
            print(f"La clé pour décrypter le fichier est : {i}")
            print(f"Le message décrypté est le suivant : \n{decryptage(i, liste)}")
            # Si c'est bon, on retourne la clé et le message décrypté
            return i, decryptage(i, liste)
        else:
            continue  # Sinon, on continue avec la clé suivante
    # Si aucune clé ne fonctionne, on retourne None
    return None


def choix_utilisateur(action):
    # Action 1 : crypter ou décrypter
    if action == 1:
        while True:
            choix = input("Voulez-vous crypter ou decrypter ? Crypter (0) / Decrypter (1) : ")
            if choix in ("0", "1"):  # Vérifie que l'utilisateur entre bien 0 ou 1.
                return choix
            print("Veuillez entrer 0 ou 1.")

    # Action 2 : fichier ou texte saisi
    elif action == 2:
        while True:
            choix = input("Voulez-vous crypter un fichier ou écrire votre message ? Fichier (0) / Écrire (1) : ")
            if choix in ("0", "1"):
                return choix
            print("Veuillez entrer 0 ou 1.")

    # Action 3 : clé connue ou non
    elif action == 3:
        while True:
            choix = input("Connaissez-vous la clé de décryptage ? Non (0) / Oui (1) : ")
            if choix in ("0", "1"):
                return choix
            print("Veuillez entrer 0 ou 1.")

    # Par défaut (action invalide)
    return None


def choix_cle():
    # Demande à l'utilisateur de saisir la clé
    cle_str = input("Quelle est votre clé de décryptage? ")
    # Tant que ce n'est pas un entier (ou un entier négatif), on redemande
    while not (cle_str.isdigit() or (cle_str[0] == "-" and cle_str[1:].isdigit())):
        print("Veuillez entrer un nombre entier.")
        cle_str = input("Quelle est votre clé de décryptage ? ")
    # Conversion de la clé en entier
    cle = int(cle_str)
    return cle
