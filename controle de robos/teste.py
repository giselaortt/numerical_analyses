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
			answer.append( ( erro_quadrático( saidas, self.saidas_esperadas ) ) )

		return np.array(answer)


def toy_problem():
	np.random.seed( int(time.time()) )
	pop = [ genetic.Controle( 2, 3, 1 ) for _ in range(1000) ]
	fitness = fitness_para_teste(  )
	genetic.GeneticAlgorithm( fitness,  population = pop, population_size = 1000, max_iteration = 6000, episilon = 0.02 )


def erro_quadrático( array1, array2 ):

	#print( -1 * np.sum( (array1 - array2)**2 ) )
	return -1 * np.sum( (array1 - array2)**2 )

'''


 '''

if __name__ == '__main__':
	#toy_problem()
	neural = neural.Network( 2,3,1, hiddenLayer = np.array([[ 5.26039061, 5.31781714, 4.70746083], [-4.69605835, -4.86718701, -4.85090653], [-3.18544409, 2.17933334, -3.31325609]]), outputLayer = np.array([[-4.56310107], [ 6.15418054], [-3.18097799], [-2.62864848]]))
	saidas = neural.run_multiple( np.array([ [0,1], [1,1], [0, 0] , [1, 0]]) )
	print( saidas )
	print( "saida esperada" , [ 0,1,1,0 ] )


