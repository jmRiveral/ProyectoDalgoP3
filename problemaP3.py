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
    for i in range(1,m+1):
        a=(k*i)
        if a<=m:
            aux1.append(a)
            rep1[a]=1

    if m%k==0:
        rep1[m]=1
    else:
        rep1[m]=0
    
    
    s=1
    while s<=m:
        
        
        for e in aux1:
            act=e+k+s
            while act<=m:
                if act not in rep2:
                    
                    aux2.append(act)
                    rep2[act]=rep1[e]
                else:
                    rep2[act]+=rep1[e]
                act+=(s+k)
        
        if len(rep2)==0:
            break
        if m in rep2:
            
            rep2[m]+=rep1[m]
        else:
            rep2[m]=rep1[m]
        
        
        rep1=rep2.copy()
        rep2.clear()
        
        aux1=aux2.copy()
        aux2.clear()
        s=s+1
        
        
       
             

        
        
       
    
    return rep1[m]




def putamierda(m,k):
    
        
    aux1={}
    aux2={}
    aux3={}
    #inicializa aux
    for i in range(1,m+1):
        a=(k*i)%998244353
        if a<=m:
            aux1[a]=1
            aux3[a]=1
    
    for i in range(1,m):#iterador numero movimentos
        if len(aux1)==0:
            break
        act=0
        for elem in aux1:#iterar sobre lista 1
            act+= (k+i)
            print(aux3)
            sig=act+elem
            if sig==m:
                aux3[m]+=aux1[elem]
            if sig in aux1:
                aux3[sig]+=aux1[elem]
            else: 
                aux2[sig]=1
                aux3[sig]=1
        print(aux2)
        aux1=aux2.copy()
        aux2.clear()
            
                
        
        
            
   
    return aux3[m]


def dicSol(m,k):
    
    contador=0
    aux1={}
    aux2={}
    #inicializa aux
    for i in range(1,m+1):
        a=(k*i)
        if a<=m:
            aux1[a]=1
    
   
    fc=0
    for i in range(m):
        k+=1
       
        #print("len aux1: ",len(aux1))
        
        if len(aux1)==0:
        
            break
        aux3=list(aux1.keys())[:]
        for j in aux3:
            factor=1
            sig=(factor*k) +j
            
            while  sig<=m :
            
                if sig in aux1:
                    aux1[sig]+=aux1[j]
                    aux1[j]=0
                    if aux1[sig]==0:
                        aux1[sig]=1
                else:
                    aux1[sig]=1
                factor+=1
                sig=((factor*k) +j)
        print(aux1)
        
        
       
    return aux1[m]

def test(m,k):
    contador=0
    aux1={}
    #inicializa aux
    for i in range(1,m+1):
        a=(k*i)
        if a<=m:
            aux1[a]={0:0}
    
   
    fc=0
    for i in range(m):#crea arbol
        k+=1
       
        #print("len aux1: ",len(aux1))
        
        if len(aux1)==0:
        
            break
        aux3=list(aux1.keys())[:]
        for j in aux3:
            factor=1
            sig=(factor*k) +j
            
            while  sig<=m :
            
                if sig in aux1:
                    if j not in aux1[sig]:
                        aux1[sig][j]=0
                   
                   
                else:
                    aux1[sig]={}
                    aux1[sig][j]=0
                factor+=1
                sig=((factor*k) +j)
        print(aux1)
    
    
       
    return pls(aux1,0,m)

def pls(tredic,paths,nodo):
    
    if nodo==0:
        return 1
    
    
    for hijo in tredic[nodo]:
        paths+=pls(tredic,paths,hijo)

    return paths
    


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
        #print(m,":",dicSol(m,k))
        #print("--- %s seconds ---" % (time.time() - start_time))
        #print(test(m, k))
        #print(saltoDivRecursivo(m,0, k, total))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
