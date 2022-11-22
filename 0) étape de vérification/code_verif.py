#!/usr/bin/env python3

import sys
import os

#Vérifier que ce n'est pas un répertoire mais bien un fichier

file_name=sys.argv[1]

if os.path.isdir(file_name) == 1:
    print("veuillez donner un fichier et non pas un répertoire")
    return "F"

Vérifier que l'extention est un .SAM si .bam message d'erreur demandant à l'utilisateur de mettre un .sam Tiago
if file_name.split(".")[-1] != "sam" :
    print("veuillez donner un fichier dont l'extension est .sam")
    exit ()
    
Vérifier que ce n'est pas un fichier vide Ally

if os.path.getsize(file_name) == 0:
    print("Le fichier est vide")
    exit()

return "ok"
