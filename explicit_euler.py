# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.

#primeiro teste do algoritmo of euler para python 2.7
#nesta versao nao me preocupei com a eficiencia e nem com o rigor, a intencao era apenas testar o algoritmo of euler.
import matplotlib.pyplot as plt
import math
import numpy as np


#calcula o erro para os parametros escolhidos do method of euler
# e( t, delta_t ) = ( euler( t, 2*delta_t ) - euler( t, delta_t ) )
def erro_euler( dy_dx, delta_t, t ):

	return method_euler( dy_dx, 2*delta_t, t ) - method_euler( dy_dx, delta_t, t )



#uma funcao que retorna o tamanho do delta_h para que se tenha o number of passos ofsejados
def calcula_delta_t( t_initial, t_final, number_of_iterations ):

	#return (t_final - t_initial) / number_of_iterations
	return float(t_final - t_initial) / float(number_of_iterations)



#dx_dy é a _derivative da funcao que vamos aproximar
def method_euler( dy_dx, t_final, t_initial = 0, delta_t = None, number_of_iterations = None, y_initial = 0  ):

	y = [y_initial]

	if(delta_t is None):
		delta_t = (t_final - t_initial) / number_of_iterations

	time = np.arange( t_initial, t_final, delta_t )
	for t in  time :
		y.append( y[-1] + delta_t*dy_dx(t, y[-1]) )

	return y



def method_euler_modified( dy_dx, t_final, t_initial = 0, number_of_iterations = None, delta_t = None, y_initial = 0 ):

	y = [y_initial]
	if(delta_t is None):
		delta_t = float(t_final)/float(number_of_iterations)

	time = np.arange( t_initial, t_final, delta_t )
	for t in  time :
		k1 = dy_dx(t, y[-1])
		k2 = dy_dx(t + delta_t, y[-1] + delta_t * k1 )
		y.append( y[-1] + (delta_t / 2.0) * ( k1 + k2 ))

	return y



#valores_iniciais é um numpy array com os valores iniciais of X1, X2, X3, em diante.
#_derivatives é um numpy array of funções que ofve ter o mesmo tamanho que inícios.
#time initial, time final: Float
#number_of_iterations: inteiro

#Euler explicito para várias dimenssões

def euler_multidimentional( valores_iniciais, _derivatives, t_initial = 0, t_final = None, delta_h = None, number_of_iterations = None ):

	if( delta_h == None ):
		delta_h = ( t_final - t_initial)/number_of_iterations
	elif( number_of_iterations == None ):
		number_of_iterations = int( ( t_final - t_initial)/delta_h )

	number_of_dim = len( valores_iniciais )
	answer = np.zeros(( number_of_dim, number_of_iterations ))
	answer[ :, 0] = valores_iniciais
	time = np.arange( t_initial, t_final, delta_h )

	for i in range(1,number_of_iterations):
		for dim in range(number_of_dim):
			answer[ dim ][ i ] = answer[dim] [i-1] + delta_h * _derivatives[dim]( answer[:, i-1], time[i] )

	return answer


#TODO testar
#If nome do arquivo == None, a função retorna os valores das integrais.
#CAso o contrário, a função escreverá esses valores no arquivo.
#valores iniciais: Numpy array
def euler_modified_multidimentional( valores_iniciais, _derivatives, t_initial = 0, t_final = None, delta_h = None, number_of_iterations = None ):

	if( delta_h == None ):
		delta_h = ( t_final - t_initial)/number_of_iterations
	elif( number_of_iterations == None ):
		number_of_iterations = int( ( t_final - t_initial)/delta_h )

	ndim = valores_iniciais.shape[0]
	answer = np.zeros(( ndim, number_of_iterations ))
	answer[ :, 0 ] = valores_iniciais
	t = t_initial


	for i in range( number_of_iterations - 1 ):

		d1 = np.array( [ _derivatives[j]( t, answer[ : , i] ) for j in range(ndim) ] )
		d2 = np.array( [ _derivatives[j]( t + delta_h, answer[ : , i ] + delta_h*d1 ) for j in range(ndim) ] )
		answer[ : , i+1 ] = answer[ : , i] + delta_h * (( d1 + d2 ) / 2.0)
		t = t + delta_h


	return answer





