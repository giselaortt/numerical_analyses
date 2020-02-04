#!/usr/bin/env/ python
# -*- coding: utf-8 -*-


import neural
import controle
import genetic
import numpy as np
import math
import time

#TODO testar a representação binária na rede neural
#TODO implementar o crossover uniforme

class fitness_para_teste:
	def __init__( self ):
		self.entradas = np.array([ [0,1], [1,1], [0, 0] , [1, 0]])
		self.saidas_esperadas = np.array([[ 0,1,1,0 ]]).T


	def fit( self, population, max_iteration = 5000 ):
		answer = []
		for robot in population:
			saidas = robot.neural.run_multiple( self.entradas )
			answer.append(erro_quadratico( saidas, self.saidas_esperadas ))

		return np.array(answer)



#Testando a evolução de redes neurais a partir de um problema simples
def toy_problem_evolucao_neurais():
	np.random.seed( int(time.time()) )
	pop = [ genetic.Controle( 2, 3, 1 ) for _ in range(1000) ]
	fitness = fitness_para_teste(  )
	genetic.GeneticAlgorithm( fitness,  population = pop, population_size = 1000, max_iteration = 6000, episilon = 0.02 )



def teste_do_controle():
	#input size é o numero dos sensores do robo. nesse caso, serão oito
	#output size é o numero de destinos que o robo pode escolher. nesse caso serão quatro.
	n = neural.Network( inputSize = 8, hiddenSize = 10, outputSize = 4 )
	x, y = controle.gerar_posicao_inicial(  )
	inter = controle.Bilinear(  x_inicial = -20, x_final = 20, y_inicial = -20, y_final = 20, delta = 1, psy = controle.fi )
	controle.controle( neural = n, interpolacao = inter, xlinha = controle.xlinha_interpolacao , ylinha = controle.ylinha_interpolacao, deltah = 1, obstaculos = None, nome_do_arquivo = 'isso_eh_um_teste')



def erro_quadratico( array1, array2 ):

	return -1 * np.sum( (array1 - array2)**2 )


if __name__ == '__main__':
	#toy_problem_evolucao_neurais()
	teste_do_controle()





