#!/usr/bin/env python3

file =open(sys.argv[1])

dico = {}
lines = file.readlines()

for line in lines:
    if line[0][0] != "@":
        temp =line.split("\t")
        if temp[0] in dico.keys():
            dico[temp[0]].append(temp[1:])
        else:
            dico[temp[0]]=[temp[1:]]
    
file.close()
