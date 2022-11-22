#!/usr/bin/env python3

#Vérifier que ce n'est pas un répertoire mais bien un fichier



if os.path.isdir(file) == 1:
    print("veuillez donner un fichier et non pas un répertoire")
    return "F"

#Vérifier que l'extention est un .SAM si .bam message d'erreur demandant à l'utilisateur de mettre un .sam 

if file_name.split(".")[-1] != "sam" :
    print("veuillez donner un fichier dont l'extension est .sam")
    return "F"
    
#Vérifier que ce n'est pas un fichier vide 

if os.path.getsize(file_name) == 0:
    print("Le fichier est vide")
    return "F"

return "T"
