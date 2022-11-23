#!/usr/bin/env python3

dico = {}
file =open(sys.argv[1])
lines = file.readlines()

for line in lines:
    if line[0][0] != "@":
        temp =line.split("\t")
          #pour la colone 1 de la ligne lus si modulo de son calcul de flag =  4 (unmapped) ou 8 (mate unmapped) alors on ne prend pas la ligne.
             for i in (tableau de valeur associé au flag dans flag_calcul) if temps[1] 
                
        if temp[0] in dico.keys():
            dico[temp[0]].append(temp[1:])
        else:
            dico[temp[0]]=[temp[1:]]
    
file.close()
