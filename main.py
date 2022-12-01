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
  
## create a dictionnary of your file.sam
dico = {}
file =open(sys.argv[1])
lines = file.readlines()

for line in lines:
    if line[0][0] != "@":
        temp =line.split("\t") 
           if temp[0] in dico.keys():
               dico[temp[0]].append(temp[1:])
                  else:
                        dico[temp[0]]=[temp[1:]]
    
file.close()

## counting your starting data number

#compte toute les valeur dans le dico
number_total_of_data_counter = 0
for cle, valeur in dico.items(): 
number_total_of_data_counter += len(valeur)
print("number_total_of_data_counter ="+number_total_of_data_counter)

#compte toute les paire dans le dico
number_of_paired_reads_data_counter = 0
for cle, valeur in dico.items(): 
   if cle, valeur in dico.item() (!= 2) :
    number_of_paired_reads_data_counter += 0
    else : 
 number_of_paired_reads_data_counter += len(valeur)
print("number_of_paired_reads_data_counter =" number_of_paired_reads_data_counter)

## counting your number of mapped read
for cle, valeur in dico.items() : 
  for v in valeur :
    if v[0] & 4 != 4 : 
      del dico cle valeur
      
pour savoir si deux clones sont bien mappés en face  : 
  
  f16 = 16
  F32 = 32
  for key,value in dico.items():
    if int(value[0][0]) & 16 or int(value[1][0]) & 32 and int(value[1][0]) & 32 or int(value[0][0]) :
        
        
## mapping quality 
si la colonne 3 de notre value dans le dico > ou = à sys.argv[3]
compter faire un dico et supprimer dans le grand dico

pair_propper_mapped.py 

totally_aligned_read.py
