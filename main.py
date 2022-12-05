#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#___________authors_____________ ==> Tiago CAMACHO HENRIQUES and Allyson MOUREAUX 
#___________contact_____________ ==> tiago.camacho-henriques@etu.umontpellier.fr and allyson.moureaux@etu.umontpellier.fr
#___________version_____________ ==> 1.0
#___________date________________ ==> 06/12/2022
# We provide you a programm that sort your data from a sam file to extract reads properly mapped, mated, with the quality that you asked 
# and undred percent aligned. We do not certify that the quality of our programm is optimal and without errors. We can't be responsible for any use of it 
# but we hope that it can be useful. You can modify or share this programm as much as you like. 

########################################################## Module importation #######################################################################################
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
    else :
        print("Please give a .sam file")
else : 
    ("please give a file and not a directory")
print("Your file seems correct")
  
##################################################### create a dictionnary of your file.sam  ########################################################################

dico = {}
file = open(sys.argv[1], "r")
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
    number_total_of_data_counter += len(value)#counting all your reads in the dico that we created
print("you have "+number_total_of_data_counter+" reads in total")#number total of reads

#counting the total number of paired reads
number_of_paired_reads_data_counter += 0
for key, value in dico.items(): 
   if value in dico.item() (value != 2) : #if the key does not contains 2 values
    number_of_paired_reads_data_counter += 0#it didn't count the key because the read is not mated
   else :
    number_of_paired_reads_data_counter += 1 
print("you have "+number_of_paired_reads_data_counter+" paired reads")


######################################################### counting your number of mapped read  #####################################################################
pair_not_proper_mapped={}
pair_mapped_counter += 0
for key, value in dico.items() : 
  for v in value : #for the columns in the list contained in the value 
    if v[0] & 4 != 4 : #if the flag (column 1) does not contains 4 (binary reading) 
        pair_mapped_counter += 0
        pair_not_proper_mapped[key] = value #the read is stored in an other dictionnary in case you need it
        del dico[key]#the key is erased from the starting dictionnary 
    else : 
        pair_mapped_counter += 1
print("you have "+pair_mapped_counter+" pair mapped")

        
################################################################## mapping quality #################################################################################
bad_mapping_quality={}
good_mapping_quality_number += 0
      
for key, value in dico.items() : 
    for v in value :
        if v[3] < sys.argv[3] or v[3] != [0-9] or v[3] != [0-9][0-9] or v[3] != [0-9][0-9][0-9]: #if mapping quality colon is under your exigence or not a number 
            bad_mapping_quality[key] = value #the read is stored in an other dictionnary in case you need it
            del dico[key] #the key is erased from the starting dictionnary 
        else : 
            good_mapping_quality_number += 1
print("you have "+good_mapping_quality_number+" mapping of good quality")
      
################################################################### number of pair proper mapped  ###################################################################
pair_not_proper_mapped={}
pair_poper_mapped_counter += 0
for key,value in dico.items():
    if int(value[0][0]) & 2==2 and int(value[1][0]) & 2==2 :#if your flag = 2 in both of your mate reads
        if (int(value[0][0]) & 16==16 and int(value[1][0]) & 32==32) or (int(value[0][0]) & 32==32 and int(value[1][0]) & 16==16) :#if they are mated
            if abs((value [0][2])-(value[1][2]))<=sys.argv[2]: #and if the distance is < or = your exigence
               pair_poper_mapped_counter += 1
            continue 
    else :
        pair_not_proper_mapped[key] = value #the read is stored in an other dictionnary in case you need it
        del dico[key] #the key is erased from the starting dictionnary 
print("you have "+pair_poper_mapped_counter+" pair proper mapped")

#####################################################################  totally aligned read  ########################################################################
not_totally_aligned_read={}
totally_aligned_read_counter +=0
for key, value in dico.items() : 
    for v in value :
        if v[4] != ("[0-9][0-9][0-9]M" or "[0-9][0-9]M"): #if your CIGAR column does not contain 2 or 3 number followed by the letter M
           not_totally_aligned_read[key] = value #the value not totally aligned is stored in an other dictionnary in case you need it
           del dico[key] #the key is erased from the starting dictionnary
        else : 
            totally_aligned_read_counter += 1
print("you have "+totally_aligned_read_counter+" read totally aligned ")
#####################################################################  printing the final result ####################################################################
print(dico)
