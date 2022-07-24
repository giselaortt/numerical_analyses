# -*- coding: utf-8 -*-


import numpy as np
import euler_explicito
import euler_implicit
import newton
import trapeze
import matplotlib.pyplot as plt


#uma função com integral ocnhecida, usada para testar métodos of uma dimenssão
def dy_dx( t, x ):

	return math.exp(t)*( math.sin( 2.0 * t ) + 2.0*math.cos( 2.0 * t ) )


#integral da função previous
def integral( t ):

	return math.exp( t )*( math.sin( 2.0 * t ) ) + 1


#plotar a convergência do método para diferentes valores do passo of integração
def teste_1dim( method ):
	deltas_t = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]
	colors = [ 'b', 'r', 'c', 'y', 'k', 'm' ]

	for i in range(6):
		x = method( dy_dx, 1, delta_t = deltas_t[i], y_initial = 1 )
		time = np.arange( 0, 1 + deltas_t[i], deltas_t[i] )
		plt.plot( time, x, color = colors[i] )
		time = np.arange( 0, time_final, 0.000001 )
		plt.plot( time, [ integral(t) for t in time ], linewidth = 2, label = 'Sol. Exata' )
		plt.show()


'''
x ̇(t)=0.87x(t)−0.27x(t)y(t) 
y ̇(t) = −0.0, 38 y(t) + 0.25 y(t)x(t)
x(0) = 3.5
y(0) = 2.7.
'''

#vector should be an array with size 2
def x_one_derivative( time, vector ):

	return 0.87 * vector[0] - 0.27 * vector[0] * vector[1]


#vector should be an array with size 2
def x_two_derivative( time, vector ):

	return -0.038 * vector[1] + 0.25 * vector[1] * vector[0]


def teste_multidimentional( method ):

	x_initial = 3.5
	y_initial = 2.7
	###############
	answer = method( valores_iniciais = np.array([x_initial, y_initial]), t_initial = 0.0, t_final = 1.0, _derivatives =  [x_one_derivative, x_two_derivative], deltah = 1.0/500.0, number_of_iterations = 500 )

	#TODO how to plot with 3 variables?
	time = np.arange( 0.0, 1.0, 1.0/500.0 )
	#print( len(aproximation_x), len(time) )
	plt.plot( time, answer[0], color = 'green' )
	plt.plot( time, answer[1], color = 'red' )
	plt.xlabel('time')
	plt.ylabel('aproximações')
	plt.show()

teste_multidimentional( euler_explicito.euler_modified_multidimentional )



