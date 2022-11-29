import sys
import numpy as np

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
  

def solDP(m,k):
    caminos=0
    dist=1
    lg=m
    div=k
    mat=[[[False for x in range(m)] for y in range(k+1)] for z in range(m)]
    #[pagina dist act][k][long]
    for x in range(m):
        for y in range(k+1):
            for z in range(m):
                
                if (z+1)%(k+y)==0 and (x+1)%(z+1)==0 :
                    
                    mat[x][y][z]=True
            print(mat[x][y])    
        print(" ")

   

    return caminos

def solSeguroDP(m,k):
    contador=0
    aux1=[]
    aux2=[]
    #inicializa aux
    for i in range(1,m+1):
        if k*i<=m:
            aux1.append(k*i)
    if m in aux1:
        contador+=1
        aux1.remove(m)

    
    for i in range(m):
        k+=1
        for j in aux1:
            factor=1
            while  (factor*k) +j<=m:
                aux2.append((factor*k) +j)
                factor+=1
        veces=aux2.count(m)
        contador=contador+veces
                
        print("a1:",aux1)

        print("a2:",aux2)

        for x in range(veces):
            aux2.remove(m)
        print(aux2)
        
        aux1=aux2
        aux2=[]
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
        print(solSeguroDP(m,k))
        #print(saltoDivRecursivo(m,0, k, total))
main()
