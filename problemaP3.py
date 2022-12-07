import sys
import numpy as np
import time
sys.setrecursionlimit(999999)
def saltoDivRecursivo(m,ini,k,count):
    aux=[] 
    
    for i in range(ini+1,m+1):
        mov=i-ini
        
     
           
        if mov%k==0 :
            aux.append(i)
          
            
    
    for e in aux:
        
        if e==m:
            
            count+=1
        elif (e+k+1)<=m:
            count+= saltoDivRecursivo(m,e, k+1, 0)
            
    return count    
  


def solSeguroDP(m,k):
    
    
    contador=0
    aux1=[]
    aux2=[]
    rep1={}
    rep2={}
    #inicializa aux
    #rep indica cuantas manera se pueden llegar a dicho numero en la ruta existente
    for i in range(1,m+1):#complejidad O(m/k)
        a=(k*i)
        if a<=m:
            aux1.append(a)
            rep1[a]=1

    if m%k==0:
        rep1[m]=1
    else:
        rep1[m]=0
    
    
    s=1
    while s<=m:#es la iteracion sobre k, s es el numero de movimientos
                #es en su peor caso teorico O(m/2)
        
        
        for e in aux1:#esto en peor caso, teoricamente m/k
            act=e+k+s
            while act<=m:#esto es m/k peor caso
                if act not in rep2:
                    
                    aux2.append(act)
                    rep2[act]=rep1[e]
                else:
                    rep2[act]+=rep1[e]
                act+=(s+k)
        
        if len(rep2)==0:
            break
        if m in rep2:
            
            rep2[m]+=rep1[m]%998244353
        else:
            rep2[m]=rep1[m]
        
        
        rep1=rep2.copy()#cada uno de estos es m/k peor caso
        rep2.clear()
        
        aux1=aux2.copy()
        aux2.clear()
        s=s+1
        
        
       
             

        
    #esto deberia ser O(m^3 /k^2)
       
    
    return rep1[m]



                
   

def main():
    linea = sys.stdin.readline()
    casos = int(linea)
    linea = sys.stdin.readline()
    comp= []
    for i in range(0,casos):
        
        datastr =linea.split()
        m=int(datastr[0])
        k=int(datastr[1])
        linea=sys.stdin.readline()
        total =0
        start_time = time.time()
        print(solSeguroDP(m, k))
      


main()

