import os
import shutil
import csv
import extension

path = 'C:/Users/Olivier/Downloads'
fichier_ext = extension.extension_paths

def log(nom, destination):
    with open('C:/Users/Olivier/Downloads/Log/Log_Telechargement.csv', 'a',
               newline='') as record:
        
        ecrire = csv.writer(record)
        ecrire.writerow([nom, destination])

def deplacer(nom, cible):
    repertoire = os.path.join(path, cible)
    os.makedirs(repertoire, exist_ok=True)
    try:
        shutil.move(f"{path}/{nom}", f"{repertoire}/{nom}")
        print(f'{nom} : Fichier transféré.')
        log(nom, repertoire)
    except:
        print("Une erreur est survenue ....")
        print(nom)


files = os.listdir(path)
for name in files:
    f_nom, f_ext = os.path.splitext(name)
    for cle, cible in fichier_ext.items():
        if f_ext == cle:
            deplacer(name, cible)

    
