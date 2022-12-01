#!/usr/bin/env python3

import sys, os
###########################################################  verification of your file  #############################################################################
if os.path.isdir(sys.argv[1]) == 1:
    print("veuillez donner un fichier et non pas un répertoire")
    return "F"

if (sys.argv[1]).split(".")[-1] != "sam" :
    print("veuillez donner un fichier dont l'extension est .sam")
    return "F"

if os.path.getsize(sys.argv[1]) == 0:
    print("Le fichier est vide")
    return "F"
return "T"
  exit()
else : 
  print("fichier ok")
  
##################################################### create a dictionnary of your file.sam  ########################################################################
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

################################################################## counting your starting data number  ##############################################################

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

######################################################### counting your number of mapped read  #####################################################################
for cle, valeur in dico.items() : 
  for v in valeur :
    if v[0] & 4 != 4 : 
      del dico cle valeur
      
pour savoir si deux clones sont bien mappés en face  : 
  
  f16 = 16
  F32 = 32
  for key,value in dico.items():
    if int(value[0][0]) & 16 or int(value[1][0]) & 32 and int(value[1][0]) & 32 or int(value[0][0]) :
        
        
################################################################## mapping quality #################################################################################
si la colonne 3 de notre value dans le dico > ou = à sys.argv[3]
compter faire un dico et supprimer dans le grand dico

################################################################### number of pair proper mapped  ###################################################################

pair_not_proper_mapped={}
counter =+0

flag = 2, 16, 32 et si position [6] 

 f16 = 16
 f32 = 32
  for key,value in dico.items():
    if int(value[0][0]) & 2==2 and int(value[1][0]) & 2==2 :
        if (int(value[0][0]) & 16==16 and int(value[1][0]) & 32==32) or (int(value[0][0]) & 32==32 and int(value[1][0]) & 16==16) :
            if abs((value [0][2])-(value[1][2]))<=sys.argv[2]
               counter += 1
               continue 
     pair_not_proper_mapped[key] = value
     del dico[key]

#####################################################################  totaly aligned read  ########################################################################

#test CIGAR = nombre de 1,2 ou 3 chiffre)+M veut dire que c'est totalement mappé  TIAGO !
#si != M pas bien mappé 
#[1-500]M
#[0-9][0-9][0-9]M ou [0-9][0-9]M

#on selectionne seulement les lignes qui vérifie cette information 



#Pour i de 0 a n+1 par pas de 1
#si colone cigar = 100M alors 
#compteur +1
#i+1
#sinon 
#i+1
for key,value in dico.items():
  a finir 
  
  
  
  
  
totally_aligned = [];
valeur = dico.values()
for  valeur in dico 
  if (colone5) != ([0-9][0-9][0-9]M or [0-9][0-9]M);
     del dico[key]
