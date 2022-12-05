import sys
import numpy as np
import time
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
    #inicializa aux
    for i in range(1,m+1):
        a=(k*i)%998244353
        if a<=m:
            aux1.append(a)
    if m%k==0:
        contador+=1
   
    
    fc=0
    for i in range(m):
        k+=1
        fc+=1
        #print("len aux1: ",len(aux1))
        
        if len(aux1)==0:
            print("iter: ",fc)
            break
        for j in aux1:
            factor=1
            lim=(factor*k) +j
        
            while  lim<=m :
                if lim==m:
                    contador=(contador+1)%998244353
               
                else:
                    if lim+k+1<=m:
                     aux2.append(lim)
                factor+=1
                lim=((factor*k) +j)%998244353
        
       
             

        
        
        aux1=aux2
        aux2=[]
    return contador

def test(m,k):
    
        
    contador=0
    aux1=[]
    aux2=[]
    #inicializa aux
    for i in range(1,m+1):#m/k
        a=(k*i)%998244353
        if a<=m:
            aux1.append(a)
    if m%k==0:
        contador+=1
   
    
    for i in range(4*k):
        k+=1
        j=0
        print(aux1)
        while len(aux1)>j:
            factor=1
            
            g=aux1[j]
            lim=(factor*k) +g
        
            while  lim<=m :
                if lim==m:
                    contador=(contador+1)%998244353
               
                else:
                    if lim+k+1<=m:
                     aux2.append(lim%998244353)
                factor+=1%998244353
                lim=((factor*k) +aux1[j-1])%998244353
            j+=1
       
             

        
        
        aux1=aux2[:]
        aux2.clear
    return contador

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
        print(solSeguroDP(m,k))
        print("--- %s seconds ---" % (time.time() - start_time))
        #print(test(m, k))
        #print(saltoDivRecursivo(m,0, k, total))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
