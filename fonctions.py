"""Ce module permet de fournir des fonctions pour le chiffrement de C
Il est écrit par Marlene Sanjose dans le cadre du cours MGA802
"""


def lire_liste_mots(fichier="mots_pendu.txt", dossier="./ressources"):
    import os

    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

    # Transforme la chaine de caracteres en liste
    # le saut de ligne sert de separateur de champs
    word_list = words.split('\n')

    # retourne la liste de mots
    return word_list


def enlever_caracteres_speciaux(mot):
    import unicodedata

    # Solution obtenue sur https://www.geeksforgeeks.org/how-to-remove-string-accents-using-python-3/
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word if not unicodedata.combining(char)])


def ouverture_fichier(fichier="texte_code.txt"):
    # teste si le fichier existe
    """full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')"""

# Ouvrir le fichier en mode lecture
    with open("texte_code.txt", "r", encoding = "utf-8") as fio:
# Lire le contenu du fichier
        contenu = fio.read()
        print(contenu)

# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fio:
    contenu=""
    fio.write(contenu)

ouverture_fichier()


alphabet = string.ascii_lowercase

print(alphabet)

alphabet.find("t")

new_character = alphabet[8]

print(new_character)

