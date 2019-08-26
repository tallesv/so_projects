
import numpy as np

def soma(args, results):
	linhas = len(args)
	colunas = len(args[0])
	
	aux = []
	for i in range(linhas):
		del aux[:]
		for k in range(colunas):
			aux.append(args[i][k] + args[i][k])
			print(aux)
		results.append(aux)
		


def mult(ags, results):
	linhas = len(args)
	colunas = len(args[0])
	aux = []
	for i in range(linhas):
		for k in range(colunas):
			for j in range(colunas):
			aux += args[i][k] * args[k][i]	


res = []
matrix = np.random.randint(10,size=(3,3))
soma(matrix, res)
print(matrix)
print(res)
