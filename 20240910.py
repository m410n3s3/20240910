#coding: utf-8
import math as m

def Eq2grau(a,b,c): 
	Delta = m.pow(b,2)-4*a*c
	x1 = None
	x2 = None
	if (Delta>0): 
		#Há duas raizes reais distintas
		x1 = (-b-pow(Delta, 0.5))/(2*a)
		x2 = (-b+pow(Delta, 0.5))/(2*a)
		
	elif (Delta == 0):
		print("Há raiz única, Delta = ", Delta)
		
	else:
		print("Raízes complexas, Delta = ", Delta)
			
	return x1,x2,Delta
		
		
	
	
if __name__=="__main__": 
    saida = Eq2grau(1,4,4)
    print(saida)
    print("Quantidade de termos: ", len(saida))
    print("Primeiro termo", saida[0])
    print("Segundo termo", saida[1])
    print("Terceiro termo", saida[2])
        