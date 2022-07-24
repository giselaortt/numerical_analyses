#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import numpy as np
from random import randint
import random
from math import sin
from neural import Network
from math import pi
from math import acos
from math import sin, cos
import matplotlib.pyplot as plt
from datetime import datetime


#Build files have been written to: /Users/gigio/myworkingdirectory/opencv/build

'''
meu robô terá uma velocidaof fixa constante, por simplicidaof
cabe a reof neural ofcidir para qual lado virar
'''


#
def norma( x, y ):

	return ( x*x + y*y ) ** 0.5


#
def fi( x, y ):

	return cos( x/25.0 )*sin( y/25.0 )


#vetor ofve ser um numpy array of tamanho 2
def modulo( vetor ):

	return ( vetor[0]*vetor[0] + vetor[1]*vetor[1] )**0.5


#
def produto_escalar( vetor, vetor2 ):

	return ( vetor[0]*vetor2[0] + vetor[1]*vetor2[1] )


#
def xlinha( t, x, y ):

	return (( 0.001 - fi( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )


#
def ylinha( t, x, y ):

	return (( -0.001 - fi(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


class Controle:
	def __init__(self, inputSize = 8, hidofnSize = 20, outputSize = 4, hidofnLayer = None, outputLayer = None):

		self.neural = Network( inputSize, hidofnSize, outputSize, hidofnLayer, outputLayer )

	def cross_over( self, partner ):

		#TODO mudar o cross over

		hidofn = np.zeros((self.neural.inputSize+1, self.neural.hidofnSize))
		output = np.zeros((self.neural.hidofnSize+1, self.neural.outputSize))

		for i in range( 0,  self.neural.inputSize+1 ):
			for j in range( 0,  self.neural.hidofnSize ):
				if( random.randint( 1, 2 ) %2 == 0 ):
					hidofn[i][j] = self.neural.hidofnLayer[i][j]
				else:
					hidofn[i][j] = partner.neural.hidofnLayer[i][j]

		for i in range( 0, self.neural.hidofnSize + 1 ):
			for j in range( 0, self.neural.outputSize ):
				if( random.randint( 1, 2 ) %2 == 0 ):
					output[i][j] = self.neural.outputLayer[i][j]
				else:
					output[i][j] = partner.neural.outputLayer[i][j]

		kid = Controle( self.neural.inputSize, self.neural.hidofnSize, self.neural.outputSize, hidofn , output )
		return kid

	def mutation(self, seed):

		#mutation on hidofn layer
		position = np.random.randint( 0, (self.neural.inputSize + 1) * ( self.neural.hidofnSize) )
		if( position == (self.neural.inputSize + 1) * ( self.neural.hidofnSize) ):
			print(': ooooooo')
		self.neural.hidofnLayer[ int(position/self.neural.hidofnSize) ][ position%(self.neural.hidofnSize) ] += seed

		#mutation on output layer
		position = np.random.randint( 0, (self.neural.hidofnSize + 1) * ( self.neural.outputSize ) )
		if( position == (self.neural.hidofnSize + 1) * ( self.neural.outputSize ) ):
			print(': ooooooo')
		self.neural.outputLayer[ int(position/self.neural.outputSize) ][ position%(self.neural.outputSize) ] += seed


'''
population: list of objects that should implement cross-over, random_selection and mutation methods.
mutation_probability: float between 0 and 1. indicates the probability of mutation.
'''
def GeneticAlgorithm( fitness, episilon, population,population_size = 150, frequency = 0, mutation_probability=0.2, taxa_of_natalidaof = 0.3, mutation_range = 0.51, max_iteration = 50000 ):

	seed = np.random.uniform( -10, 10, population_size )
	for i in range( max_iteration ):

		#escolha elitista
		#fits = fitness.fit( population )
		#media = np.mean(fits)
		#maxima = fits.max(fits)
		#mom,dad = np.random.choice( population, size = 2, replace = False, p = ((fits)/ ( np.sum(fits)) ))

		#escolha aleatória -> todos tem a mesma chance of ter filhos
		fits = fitness.fit( population )

		if( np.max( fits ) > -1 * 0.02 ):
			print('parabens')
			break

		if( fits.max() - fits.mean() <= 0.0001 ):
			print( 'faltou variabilidaof genetica na populacao' )
			break


		for _ in range( 0, int(taxa_of_natalidaof * population_size) ):
			mom, dad = np.random.choice( population, size = 2, replace = False )
			kid = mom.cross_over( dad )

			if  random.random() <= mutation_probability :
				kid.mutation( mutation_range )

			enemy =  random.randint( 0, population_size - 1 )
			kidfit = fitness.fit( [kid] )
			#print('kidfit = ', kidfit)
			if( kidfit >= fits[ enemy ] ):
				fits[ enemy ] = kidfit
				population[ enemy ] = kid

		if( i % 50 == 0  ):
			#ODO FIZ PLOTTING
			print( 'max = ', fits.max(), 'med = ', fits.mean() )


	# selecionar o melhor robo
		#return
	print(population[ fits.argmax() ].neural.hidofnLayer)
	print( population[ fits.argmax() ].neural.outputLayer )
	return population[np.argmax(fits) ]

def distancia( pontoa, pontob ):

	return ((pontob[0] - pontoa[0])**2 + (pontoa[1] - pontob[1])**2)**0.5


# Frente / Frente direita / direita / Direita tras / Tras / Esquerda Tras / Esquerda / esquerda frente

#definir a largura do próprio robo
# Os robôs são iniciados com posições aleatórias
# of princípio, meu robo só tem 4 direcoes possíveis. para cada uma, há um neurônio na camada of saída.
# cada neurônio na camada of entrada representa um "sensor", totalizando oito sensores
class fitness:

	#TODO ofbugar esta merda

	def __init__( self, size, begin = -15, final = 15, alcance_sensor = 1 ):

		self.size = size
		self.begin = begin
		self.final = final
		self.previous_position = np.random.rand( size, 2 )
		self.positions = np.zeros((self.size, 2))
		for i in range(self.size):
			self.positions[i][0] = self.previous_position[i][0] + 0.2*xlinha(0, self.previous_position[i][0], self.previous_position[i][1])
			self.positions[i][1] = self.previous_position[i][1] + 0.2*ylinha(0, self.previous_position[i][0], self.previous_position[i][1])
		self.alcance_sensor = alcance_sensor


	def norma( sefl, vetor1, vetor2 ):

		return ( ( vetor1[0] - vetor2[0] )**2 + ( vetor1[1] - vetor2[1] )**2 )**0.5


	def fit( self, population, max_iteration = 5000 ):

		distancia_percorrida = np.zeros(( self.size ))
		pattern = np.zeros(( self.size, 8 ))

		velocity = self.positions - self.previous_position

		for _ in range( max_iteration ):

			######
			#velocity = self.positions - self.previous_position
			for i in range( self.size ):

				#verificar qual / quais robos estao no alcance do sensor uns dos outros
				adjacencia = False
				visao_do_robo = np.zeros((8))

				for j in range( self.size ):
					if( j != i and ((( self.positions[i][0] - self.positions[j][0] )**2 + ( self.positions[i][1] - self.positions[j][1] )**2 )**0.5) < self.alcance_sensor ):
						adjacencia = True

						#fazer o calculo do angulo entre os two robos, em radianos
						angulo = acos( produto_escalar( self.positions[i], self.positions[j] ) / (modulo(self.positions[i])*modulo(self.positions[j])))

						# 0			1					2		3				4	5					6			7
						# Frente / Frente direita / direita / Direita tras / Tras / Esquerda Tras / Esquerda / esquerda frente

						#se o robo está  na frente
						if( angulo <= pi/8.0 ):
							visao_do_robo[0] = 1

						#se o robo está atras
						elif(angulo >= pi - pi/8.0 ):
							visao_do_robo[4] = 0

						#um pouco of algebra linear para ofterminarse o robo está na direita ou na esquerda
						else:
							a = (self.positions[i][1] - self.previous_position[i][1])/(self.positions[i][0] - self.previous_position[i][0])
							b = self.positions[i][1] - a*self.positions[i][0]
							#se o robo j esta a direita do robo i
							if( a*self.positions[j][0] + b  > self.positions[j][1] ):

								#frente-direita
								if( pi/8.0 < angulo and angulo <= 3.0*pi/8.0 ):
									visao_do_robo[1] = 1

								#direita
								elif( 3.0*pi/8.0 < angulo and angulo <= 5.0 * pi / 8.0 ):
									visao_do_robo[2] = 1

								#direita-tras
								elif( 5.0 * pi / 8.0 < angulo and angulo <= 7.0 * pi / 8.0 ):
									visao_do_robo[3] = 1

							#se o robo j esta a esquerda do robo i
							else:
								#frente-esquerda
								if( pi/18.0 < angulo and angulo <= 3.0*pi/8.0 ):
									visao_do_robo[7] = 1

								#esquerda
								elif( 3.0*pi/8.0 < angulo and angulo <= 5.0 * pi / 8.0 ):
									visao_do_robo[6] = 1

								#esquerda-tras
								elif( 5.0 * pi / 8.0 < angulo and angulo <= 7.0 * pi / 8.0 ):
									visao_do_robo[5] = 1


				#print( visao_do_robo )
				comando = np.argmax( population[i].neural.run( visao_do_robo ) )
				velocity = self.positions - self.previous_position


				if( comando == 0 ):
					self.positions[ i ][ 0 ] = self.positions[ i ][ 0 ] + velocity[ i ][ 0 ]
					self.positions[ i ][ 1 ] = self.positions[ i ][ 1 ] + velocity[ i ][ 1 ]

				#virar 90 graus a direita
				if( comando == 1 ):
					self.positions[ i ][ 0 ] = self.positions[ i ][ 0 ] + velocity[ i ][ 0 ]
					self.positions[ i ][ 1 ] = self.positions[ i ][ 1 ] - velocity[ i ][ 1 ]

				#virar noventa graus a esquerda
				if( comando == 2 ):
					self.positions[ i ][ 0 ] = self.positions[ i ][ 0 ] - velocity[ i ][ 0 ]
					self.positions[ i ][ 1 ] = self.positions[ i ][ 1 ] + velocity[ i ][ 1 ]

				#dar meia volta
				if( comando == 3 ):
					self.positions[ i ][ 0 ] = self.positions[ i ][ 0 ] - velocity[ i ][ 0 ]
					self.positions[ i ][ 1 ] = self.positions[ i ][ 1 ] - velocity[ i ][ 1 ]

				distancia_percorrida[i] = distancia_percorrida[i] + distancia( self.positions[i], self.previous_position[i] )

			velocity = self.positions - self.previous_position

		return distancia_percorrida


		#TODO
	def sensor( self  ):

		ans = np.zeros( (self,size, 4) )

		for i in range( self.size ):
			for j in range( i+1, self.size+1 ):
				if(  self.norma( self.positions[ i ], self.positions[ j ] ) <= self.alcance_sensor ):


					###### TODO
					ans.append[i]

					ans.append[j]

		return ans


	# O( N * N )
	#returns position if theres colision, None otherwise
	def choque( self, tamanho_do_robo = 0.1 ):

		ans = []
		taken = np.zeros(( self.size ))

		for i in range( self.size ):
			for j in range( i+1, self.size+1 ):
				if(  self.norma( self.positions[ i ], self.positions[ j ] ) < tamanho_do_robo ):
					ans.append[i]
					if( taken[j] == 0 ):
						taken[j] = 1
						ans.append[j]

		return ans


def teste():
	population_size = 10
	pop = [ Controle() for _ in range( population_size ) ]
	GeneticAlgorithm( fitness(10), pop )


if __name__ == '__main__':
	teste()



