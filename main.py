#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os
###########################################################  verification of your file  #############################################################################
if os.path.isdir(sys.argv[1]) == 1: #if your path is a directory 
    if (sys.argv[1]).split(".")[-1] == "sam" :#if your filoe is a .sam
        if os.path.getsize(sys.argv[1]) != 0 :#if it's not empty
            file = open(sys.argv[1], "r")#it open the file
            for line in file :
                line_col = line.split("\t")#split the line
                    if len(line_col) >= 11 :#verify that the format look like a sam format with the minimal number of columns
                        pass   
                    else  : 
                    print("Your file is not a .sam format")
                    break
        else :
            print("your file is empty")
            break
    else :
        print("Please give a .sam file")
        break
else : 
    ("please give a file and not a directory")
    break
print("Your file seems correct")
  
##################################################### create a dictionnary of your file.sam  ########################################################################

dico = {}
lines = file.readlines()#read line by line your file

for line in lines:
    if line[0][0] != "@":#avoid first lines that are not reads
        temp =line.split("\t") #create a temporary variable that contain your line splited in columns
           if temp[0] in dico.keys():#if the first column : the name of your read already exist in the dico 
               dico[temp[0]].append(temp[1:])#it add all the other columns in the value as a list 
                  else:
                        dico[temp[0]]=[temp[1:]]#if it does not exist, create the key with the nam of the read and the list associated in value 
    
file.close()

################################################################## counting your starting data number  ##############################################################

number_total_of_data_counter = 0
for key, value in dico.items(): 
number_total_of_data_counter += len(valeur)#counting all your reads in the dico that we created
print("you have "+number_total_of_data_counter+" reads in total")#number total of reads

#counting the total number of paired reads
number_of_paired_reads_data_counter += 0
for key, value in dico.items(): 
   if key, value in dico.item() (!= 2) : #if the key does not contains 2 values
    number_of_paired_reads_data_counter += 0#it didn't count the key because the read is not mated
    else :
        number_of_paired_reads_data_counter += 1 
print("you have "+number_of_paired_reads_data_counter+"paired reads)


######################################################### counting your number of mapped read  #####################################################################
pair_not_proper_mapped={}
pair_proper_mapped_counter += 0
for key, value in dico.items() : 
  for v in value : #for the columns in the list contained in the value 
    if v[0] & 4 != 4 : #if the flag (column 1) does not contains 4 (binary reading) 
        pair_proper_mapped_counter += 0
        pair_not_proper_mapped[key] = value #the read is stored is an other dictionnary in case you need it
        del dico[key]#the key is erased from the starting dictionnary 
    else : 
        pair_proper_mapped_counter += 1
print("you have "+pair_proper_mapped_counter+" pair proper mapped")

        
################################################################## mapping quality #################################################################################
bad_mapping_quality={}
for key, value in dico.items() : 
    for v in value :
        if v[3] < sys.argv[3] or != [0-9] or != [0-9][0-9] or != [0-9][0-9][0-9]: #if mapping quality colon is under your exigence or not a number 
            bad_mapping_quality[key] = value #the read is stored is an other dictionnary in case you need it
            del dico[key] #the key is erased from the starting dictionnary 
################################################################### number of pair proper mapped  ###################################################################
pair_not_proper_mapped={}
counter =+0

flag = 2, 16, 32 et si position [6] 

  for key,value in dico.items():
    if int(value[0][0]) & 2==2 and int(value[1][0]) & 2==2 :
        if (int(value[0][0]) & 16==16 and int(value[1][0]) & 32==32) or (int(value[0][0]) & 32==32 and int(value[1][0]) & 16==16) :
            if abs((value [0][2])-(value[1][2]))<=sys.argv[2]
               counter += 1
               continue 
     else :
        pair_not_proper_mapped[key] = value
        del dico[key]

#####################################################################  totaly aligned read  ########################################################################

for key, value in dico.items() : 
    for v in value :
        if v[4] != ([0-9][0-9][0-9]M or [0-9][0-9]M)
           not_totaly_aligned_read[key] = value
            del dico[key]

    
