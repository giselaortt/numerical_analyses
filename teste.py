# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


import numpy as np
import euler_explicito
import euler_implicito
import newton
import trapezio
import matplotlib.pyplot as plt


#uma função com primitiva ocnhecida, usada para testar métodos de uma dimenssão
def dy_dx( t, x ):

	return math.exp(t)*( math.sin( 2.0 * t ) + 2.0*math.cos( 2.0 * t ) )


#primitiva da função anterior
def primitiva( t ):

	return math.exp( t )*( math.sin( 2.0 * t ) ) + 1


#plotar a convergência do método para diferentes valores do passo de integração
def teste_1dim( metodo ):
	deltas_t = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]
	colors = [ 'b', 'r', 'c', 'y', 'k', 'm' ]

	for i in range(6):
		x = metodo( dy_dx, 1, delta_t = deltas_t[i], y_inicial = 1 )
		tempo = np.arange( 0, 1 + deltas_t[i], deltas_t[i] )
		plt.plot( tempo, x, color = colors[i] )
		tempo = np.arange( 0, tempo_final, 0.000001 )
		plt.plot( tempo, [ primitiva(t) for t in tempo ], linewidth = 2, label = 'Sol. Exata' )
		plt.show()


'''
x ̇(t)=0.87x(t)−0.27x(t)y(t) 
y ̇(t) = −0.0, 38 y(t) + 0.25 y(t)x(t)
x(0) = 3.5
y(0) = 2.7.
'''

#vector should be an array with size 2
def x_um_linha( tempo, vector ):

	return 0.87 * vector[0] - 0.27 * vector[0] * vector[1]


#vector should be an array with size 2
def x_dois_linha( tempo, vector ):

	return -0.038 * vector[1] + 0.25 * vector[1] * vector[0]


def teste_multidim( metodo ):

	x_inicial = 3.5
	y_inicial = 2.7
	###############
	answer = metodo( valores_iniciais = np.array([x_inicial, y_inicial]), t_inicial = 0.0, t_final = 1.0, derivadas =  [x_um_linha, x_dois_linha], deltah = 1.0/500.0, num_iteracoes = 500 )

	#TODO how to plot with 3 variables?
	tempo = np.arange( 0.0, 1.0, 1.0/500.0 )
	#print( len(aprox_x), len(tempo) )
	plt.plot( tempo, answer[0], color = 'green' )
	plt.plot( tempo, answer[1], color = 'red' )
	plt.xlabel('tempo')
	plt.ylabel('aproximações')
	plt.show()

teste_multidim( euler_explicito.euler_modificado_multidim )

	


