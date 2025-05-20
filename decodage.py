import string
alphabet = string.ascii_lowercase
liste_alphabet = list(alphabet)
cle=4
cle = cle%26
with open("test_texte.txt", "r", encoding = "utf-8") as fio:
# Lire le contenu du fichier
    texte = fio.read()
    liste_texte = list(texte)
    print(liste_texte)

for i in range(len(liste_texte)):
    for j in liste_alphabet:
        if liste_texte[i] == j:
