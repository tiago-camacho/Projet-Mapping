#!/usr/bin/env python3
Pour toutes les valeurs dans le dico 
     si flag=4 (unmapped) ou si flag=
X=1000 #X de test à changer en focntion du flag 
a = {}
if X-2048 >=0:
     X=X-2048
     a[1]=  2048
#else:
  #   X=X

if X-1024 >=0:
    X=X-1024
    a[2] = 1024
#else:
 #   X=X
  
if X-512 >=0:
     X=X-512
     a[3]= 512
    
else :
    X=X

if X-256 >=0:
     X=X-256
     a[4]= 256
   
else:
     X=X
  
if X-128 >=0:
    X=X-128
    a[5]= 128
    
    
else:
    X=X
  
if X-64 >=0:
     X=X-64
     a[6]= 64
     
    
else :
    X=X
if X-32 >=0:
     X=X-32
     a[7]= 32
     
else:
     X=X
  
if X-16 >=0:
    X=X-16
    a[8]= 16
    
    
else:
    X=X
  
if X-8 >=0:
     X=X-8
     a[9]= 8
     
    
else :
    X=X
if X-4 >=0:
     X=X-4
     a[10]= 4
    
     
else:
     X=X
  
if X-2 >=0:
    X=X-2
    a[11]= 2
  
    
else:
    X=X
  
if X-1 >=0:
     X=X-1
     a[12]= 1
    
else :
    X=X

print (X)
a
