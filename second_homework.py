# -*- coding: utf-8 -*-


'''
ALUNA:  GISELA MOREIRA ORTT
NUSP:   8937761

'''

import matplotlib.pyplot as plt
import numpy as np
import math



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



def integral( t ):

	return math.exp( t )*( math.sin( 2.0 * t ) ) + 1



def dy_dx( t, x ):

	return math.exp(t)*( math.sin( 2.0 * t ) + 2.0*math.cos( 2.0 * t ) )



def question_three():

	deltas = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]

	for delta_t in deltas:
		teste = method_euler_modified( dy_dx, 1, delta_t = delta_t, y_initial = 1 )
		#stop + step se faz necessario uma vez que a biblioteca numpy faz um intervalo aberto
		plt.plot( np.arange( 0, 1 + delta_t, delta_t ), teste )
		plt.show()


	time = np.arange( 0,1+delta_t, delta_t )
	plt.plot( time, [ integral( t ) for t in time ], linewidth = 2, label = 'Sol. Exata' )

	plt.show()



def question_two( time_final = 1 ):

	deltas_t = [ 0.1/pow( 2.0, m ) for m in range(0, 6) ]
	colors = [ 'b', 'r', 'c', 'y', 'k', 'm' ]

	for i in range(6):
		x = [1]
		delta_t = deltas_t[i]

		#stop + step se faz necessario uma vez que a biblioteca numpy faz um intervalo aberto
		time = np.arange( 0, time_final + delta_t, delta_t )
		for t in  time[:-1] :
			x.append( x[-1] + delta_t * ( -100*x[-1] ) ) 
		plt.plot( time, x, color = colors[i] )
		time = np.arange( 0, time_final, 0.000001 )
		plt.plot( time, [ math.exp( -100*t ) for t in time ], linewidth = 2, label = 'Sol. Exata' )
		plt.show()


#question_three()

#question_two( )


