# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


'''
ALUNA:  GISELA MOREIRA ORTT
NUSP:   8937761

'''

import matplotlib.pyplot as plt
import numpy as np
import math


def metodo_euler_modificado( dy_dx, t_final, t_inicial = 0, numero_de_iteracoes = None, delta_t = None, y_inicial = 0 ):

	y = [y_inicial]
	if(delta_t is None):
		delta_t = float(t_final)/float(numero_de_iteracoes)
	t = 0


	tempo = np.arange( t_inicial, t_final, delta_t )
	for t in  tempo :
		y.append( y[-1] + delta_t*((dy_dx(t) + dy_dx(t + delta_t))/2.0))

	return y



def primitiva( t ):

	return math.exp( t )*( math.sin( 2.0 * t ) ) + 1



def dy_dx( t ):

	return math.exp(t)*( math.sin( 2.0 * t ) + 2.0*math.cos( 2.0 * t ) )



def questao_tres():

	deltas = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]

	for delta_t in deltas:
		teste = metodo_euler_modificado( dy_dx, 1, delta_t = delta_t, y_inicial = 1 )
		#stop + step se faz necessario uma vez que a biblioteca numpy faz um intervalo aberto
		plt.plot( np.arange( 0, 1 + delta_t, delta_t ), teste )


	tempo = np.arange( 0,1+delta_t, delta_t )
	plt.plot( tempo, [ primitiva( t ) for t in tempo ], linewidth = 2, label = 'Sol. Exata' )

	plt.show()



def questao_dois( tempo_final = 1 ):

	deltas_t = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]
	colors = [ 'b', 'r', 'c', 'y', 'k', 'm' ]

	for i in range(6):
		x = [1]
		delta_t = deltas_t[i]

		#stop + step se faz necessario uma vez que a biblioteca numpy faz um intervalo aberto
		tempo = np.arange( 0, tempo_final + delta_t, delta_t )
		for t in  tempo[:-1] :
			x.append( x[-1] + delta_t * ( -100*x[-1] ) ) 
		
		plt.plot( tempo, x, color = colors[i] )
		tempo = np.arange( 0, tempo_final, 0.000001 )
		plt.plot( tempo, [ math.exp( -100*t ) for t in tempo ], linewidth = 2, label = 'Sol. Exata' )
		plt.show()


#questao_tres()

#questao_dois( )


