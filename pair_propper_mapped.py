#!/usr/bin/env python3


counter =+0

flag = 2, 16, 32 et si position [6] 

 f16 = 16
 f32 = 32
  for key,value in dico.items():
    if int(value[0][0]) & 2==2 and int(value[1][0]) & 2==2 :
        if int(value[0][0]) & 16==16 or int(value[1][0]) & 16==16 and int(value[0][0]) & 32==32 or int(value[1][0]) & 32==32 :
            if ((value [0][2])-(value[1][2])<=sys.argv[2]
            counter += 1
    else : 
        pair_not_proper_mapped={key,value}
