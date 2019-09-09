import time
import numpy as np
import random

def generate_matrix(line, column):
    i, j = line, column
    return [[random.randint(0, 9) for x in range(i)] for y in range(j)]


def soma(matrix_one, matrix_two):
	linhas = len(matrix_one)
	colunas = len(matrix_one[0])

	results = np.zeros((linhas, colunas))
	for i in range(linhas):
		for j in range(colunas):
			results[i][j] = matrix_one[i][j] + matrix_two[i][j]
	return results	


def mult(matrix_one, matrix_two):
	linhas = len(matrix_one)
	colunas = len(matrix_one[0])
	results = np.zeros((linhas, colunas))
	for i in range(linhas):
		for k in range(colunas):
			for j in range(colunas):
				results[i][j] += matrix_one[i][k] * matrix_two[k][i]	
	return results			


if __name__ == "__main__":

	tamanho = [2, 3, 4, 5, 6, 8, 10, 20, 30, 40, 50, 75, 100]

	tempo_soma = []
	tempo_mult = []
	aux = 0
	for i in range(len(tamanho)):
		aux = 0
		for j in range(20):
			matrix_one = generate_matrix(tamanho[i],tamanho[i])
			matrix_two = generate_matrix(tamanho[i],tamanho[i])
			start_time = time.time()
			res = soma(matrix_one, matrix_two)
			tempo = time.time() - start_time
			aux += tempo
		tempo_soma.append(aux / 20)	
	f = open("tempo_soma_sequencial.txt","w+")


	for i in range(len(tamanho)):
		print(tempo_soma[i])
		f.write("%d %f \n" %(tamanho[i], tempo_soma[i]))

	f.close()

	for i in range(len(tamanho)):
		aux = 0
		for j in range(20):
			matrix_one = generate_matrix(tamanho[i],tamanho[i])
			matrix_two = generate_matrix(tamanho[i],tamanho[i])
			start_time = time.time()
			res = mult(matrix_one, matrix_two)
			tempo = time.time() - start_time
			aux += tempo
		tempo_mult.append(aux/20)

	f = open("tempo_mult_sequencial.txt","w+")


	for i in range(len(tamanho)):
		print(tempo_mult[i])
		f.write("%d %f \n" %(tamanho[i], tempo_mult[i]))

	f.close()