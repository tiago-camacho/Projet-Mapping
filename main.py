#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#___________authors_____________ ==> Tiago CAMACHO HENRIQUES and Allyson MOUREAUX 
#___________contact_____________ ==> tiago.camacho-henriques@etu.umontpellier.fr and allyson.moureaux@etu.umontpellier.fr
#___________version_____________ ==> 1.0
#___________date________________ ==> 06/12/2022
# We provide you a programm that sort your data from a sam file to extract reads properly mapped, mated, with the quality that you askedÂ 
# and undred percent aligned. We do not certify that the quality of our programm is optimal and without errors. We can't be responsible for any use of it 
# but we hope that it can be useful. You can modify or share this programm as much as you like. 

########################################################## Module importation #######################################################################################
import sys, os, re

###########################################################  verification of your file  #############################################################################
if os.path.isdir(sys.argv[1]) == 1: #if your path is a directory
    if (sys.argv[1]).split(".")[-1] == "sam" :#if your file is a .sam
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
        temp = line.split("\t") #create a temporary variable that contain your line splited in columns
        if temp[0] in dico.keys():#if the first column : the name of your read already exist in the dico
            dico[temp[0]].append(temp[1:])#it add all the other columns in the value as a list
        else:
            dico[temp[0]]=[temp[1:]]#if it does not exist, create the key with the name of the read and the list associated in value
    
file.close()
################################################################## counting your starting data number  ##############################################################

number_total_of_data_counter = 0
for key, value in dico.items():
    number_total_of_data_counter += len(value)#counting all your reads in the dico that we created
print("you have "+str(number_total_of_data_counter)+" reads in total")#number total of reads

#counting the total number of paired reads
number_of_paired_reads_data_counter = 0
for key, value in dico.items():
   if len(value) == 2 : #if the key does contains 2 values
    number_of_paired_reads_data_counter += 1 #count the key
print("you have "+str(number_of_paired_reads_data_counter)+" paired reads")


######################################################### counting your number of mapped read  #####################################################################
final_data={}
pair_mapped_counter = 0
for key in dico.items() :
  for v in value : #for the columns in the list contained in the value
    if int(v[0]) & 4 != 4 : #if the flag (column 1) does not contains 4 (binary reading)
        if key in final_data.keys():#if the first column : the name of your read already exist in the dico
            final_data[key].append([value])#it add all the other columns in the value as a list
        else:
            final_data[key]=[[value]]#if it does not exist, create the key with the name of the read and the list associated in value
    pair_mapped_counter +=1
print("you have "+str(pair_mapped_counter)+" pair mapped")

        
################################################################## mapping quality #################################################################################
good_mapping_quality_number = 0

for key, value in dico.items() :
    for v in value :
        if (int(v[3]) >= int(sys.argv[3])): #if mapping quality colon is > or = your exigence
            if key in final_data.keys():#if the first column : the name of your read already exist in the dico
                final_data[key].append([value])#it add all the other columns in the value as a list
            else:
                final_data[key]=[[value]]#if it does not exist, create the key with the name of the read and the list associated in value
         good_mapping_quality_number += 1
print("you have "+str(good_mapping_quality_number)+" mapping of good quality")
      
################################################################### number of pair proper mapped  ###################################################################
pair_proper_mapped_counter = 0
for key,value in dico.items():
    if int(value[0][0]) & 2==2 and int(value[1][0]) & 2==2 :#if your flag = 2 in both of your mate reads
        if (int(value[0][0]) & 16==16 and int(value[1][0]) & 32==32) or (int(value[0][0]) & 32==32 and int(value[1][0]) & 16==16) :#if they are mated
            if abs((int(value[0][2]))-(int(value[1][2])))<=int(sys.argv[2]): #and if the distance is < or = your exigence
                if key in final_data.keys():#if the first column : the name of your read already exist in the dico
                    final_data[key].append([value])#it add all the other columns in the value as a list
                else:
                    final_data[key]=[[value]]#if it does not exist, create the key with the name of the read and the list associated in value
            pair_proper_mapped_counter += 1
print("you have "+str(pair_proper_mapped_counter)+" pair proper mapped")

#####################################################################  totally aligned read  ########################################################################
totally_aligned_read_counter = 0
for key, value in dico.items() :
    for v in value :
        if re.match("[0-9]+M", v[4]) : #if your CIGAR column contain numbers followed by the letter M
            if key in final_data.keys():#if the first column : the name of your read already exist in the dico
                final_data[key].append([value])#it add all the other columns in the value as a list
            else:
                final_data[key]=[[value]]#if it does not exist, create the key with the name of the read and the list associated in value
        totally_aligned_read_counter += 1
print("you have "+str(totally_aligned_read_counter)+" read totally aligned ")
#####################################################################  printing the final result ####################################################################
print(final_data)
