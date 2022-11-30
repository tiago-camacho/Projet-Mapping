#!/usr/bin/env python3

#est-ce que ces lignes de code prennent bien en compte la 1er élément de la valeur du dico
X = cle,valeur in dico.items() [0]

a = {}
if X-2048 >=0:
     X=X-2048
     a[2048]= "Supplementary alignment" 
if X-1024 >=0:
    X=X-1024
    a[1024] = "Read is PCR or optical duplicate"
if X-512 >=0:
     X=X-512
     a[512]= "Read fails platform/vendor quality checks"
if X-256 >=0:
     X=X-256
     a[256]= "Not primary alignment"
if X-128 >=0:
    X=X-128
    a[128]= "Second in pair"
if X-64 >=0:
     X=X-64
     a[64]= "First in pair"
if X-32 >=0:
     X=X-32
     a[32]= "Mate reverse strand"
if X-16 >=0:
    X=X-16
    a[16]= "Read reverse strand"
if X-8 >=0:
     X=X-8
     a[8]= "Mate unmapped"
if X-4 >=0:
     X=X-4
     a[4]= "Read unmapped"
if X-2 >=0:
    X=X-2
    a[2]= "Read mapped in proper pair"
if X-1 >=0:
     X=X-1
     a[1]= "Read paired"
a
