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
		self.saidas_esperadas = np.array([[ 0,1,0,1 ]]).T


	def fit( self, population, max_iteration = 5000 ):
		answer = []
		for robot in population:
			saidas = robot.neural.run_multiple( self.entradas )
			answer.append( ( erro_quadrático( saidas, self.saidas_esperadas ) ) )

		return np.array(answer)


def teste_um():
	np.random.seed( int(time.time()) )
	pop = [ genetic.Controle( 2, 2, 1 ) for _ in range(100) ]
	fitness = fitness_para_teste(  )
	genetic.GeneticAlgorithm( fitness,  pop, population_size = 100, max_iteration = 1000 )


def erro_quadrático( array1, array2 ):

	#print( -1 * np.sum( (array1 - array2)**2 ) )
	return -1 * np.sum( (array1 - array2)**2 )


if __name__ == '__main__':
	teste_um()
	#print(erro_quadrático( np.array([0.0009,0.0009,0.0009,0.00009]), np.array([0,1,0,1]) ))



