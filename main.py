#!/usr/bin/env python3

import sys, os

if os.path.isdir(sys.argv[1]) == 1:
    print("veuillez donner un fichier et non pas un répertoire")
    return "F"

#Vérifier que l'extention est un .SAM si .bam message d'erreur demandant à l'utilisateur de mettre un .sam 

if (sys.argv[1]).split(".")[-1] != "sam" :
    print("veuillez donner un fichier dont l'extension est .sam")
    return "F"
    
#Vérifier que ce n'est pas un fichier vide 

if os.path.getsize(sys.argv[1]) == 0:
    print("Le fichier est vide")
    return "F"
return "T"
  exit()
else : 
  print("fichier ok")
  
read_dico.py

number_of_data.py 

flag_calcul.py


number_of_mapped_read.py

mapping_quality.py

pair_propper_mapped.py 

totally_aligned_read.py
