
'''---------------Mini-Projet A - Chiffrement de César----------------------

    - Killian Berteaud
    - Adrien Sepierre
    - Cyril Traineau

Cours MGA802, Session Été 2025
'''

#PROGRAMME PRINCIPAL



import string
import os
def ouverture_fichier(fichier="texte_code.txt"):
    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

# Ouvrir le fichier en mode lecture
    with open("message.txt", "r", encoding = "utf-8") as fio:
# Lire le contenu du fichier
        contenu = fio.read()

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

