#!/usr/bin/env python3

X=1000
a = {}
if X-2048 >=0:
     X=X-2048
     a[1]=  2048  
if X-1024 >=0:
    X=X-1024
    a[2] = 1024
if X-512 >=0:
     X=X-512
     a[3]= 512
if X-256 >=0:
     X=X-256
     a[4]= 256
if X-128 >=0:
    X=X-128
    a[5]= 128
if X-64 >=0:
     X=X-64
     a[6]= 64
if X-32 >=0:
     X=X-32
     a[7]= 32 
if X-16 >=0:
    X=X-16
    a[8]= 16 
if X-8 >=0:
     X=X-8
     a[9]= 8
if X-4 >=0:
     X=X-4
     a[10]= 4
if X-2 >=0:
    X=X-2
    a[11]= 2
if X-1 >=0:
     X=X-1
     a[12]= 1
print (X)
a
    
    
 #dictionnaire 
 flag = {2048: "Supplementary alignment", 1024: "Read is PCR or optical duplicate",1: "Read paired", 2:	"Read mapped in proper pair", 4: "Read unmapped", 8: "Mate unmapped", 16: "Read reverse strand", 32: "Mate reverse strand", 64:	"First in pair", 128:	"Second in pair", 256:	"Not primary alignment", 512:	"Read fails platform/vendor quality checks" }
flag= [a]
