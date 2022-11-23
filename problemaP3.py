import sys
import numpy as np

def saltoDiv(m,k):
    distancias =np.zeros(shape=(m+1,m+1))
#crea mat de dist
    for i in range(0,m+1):
        for j in range(i,m+1):
            dist=j-i
            distancias[i][j]=dist
        i+=1
    print(distancias)
  
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
        saltoDiv(m,k)
main()
