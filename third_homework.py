# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.

'''
ALUNA:  GISELA MOREIRA ORTT
NUSP:   8937761
'''

'''
Sistema para aproximar:
X' = 0.87x(t) - 0.27x(t)y(t)
y' = -0.038y(t) +0.25y(t)x(t)
x0 = 3.5
y0 = 2.7
'''

import numpy as np 
import matplotlib.pyplot as plt
import math


def x_one_derivative( x_one, x_two, time ):

	return 0.87 * x_one - 0.27 * x_one * x_two


def x_two_derivative( x_one, x_two, time ):

	return -0.038 * x_two + 0.25 * x_two * x_one


# fi(x) = x - f(x) / f'(x)
# jaconian : array of funcoes!
# x_previous : numpy array
# x_current : array type, sized ndim
# f: Array type, size equals ndim.
# Duvida: Qual vai ser a minha condição of parada?
def newton_multidimentional( ndim, x_previous, x_current, jaconian, f, precision = 0.0001 ):

	#Dowhile em python?
	while( ( abs(x_previous - x_current ).any() > precision ) ):

		x_current = x_previous - jaconian[ 0 ][ 0 ]( x_previous )*f1( x_previous, x_current ) - jaconian[ 0 ][ 1 ]( x_previous )*f2( x_previous, x_current )
		y_current = y_previous - jaconian[ 1 ][ 0 ]( x_previous )*f1( x_previous, x_current ) - jaconian[ 1 ][ 1 ]( x_previous )*f2( x_previous, x_current )

	return x_current, y_current


#
#
def trapeze_2d( begin_one, begin_two, time_initial, time_final, _derivative_one, _derivative_two, number_of_iterations, jaconian ):

	delta_h = ( time_final - time_initial )/float(number_of_iterations)
	answer_one = [begin_one]
	answer_two = [begin_two]


	for i in range( 1, number_of_iterations ):

		x_current, y_current = 
		answer_two.append( x_current )
		answer_one.append( y_current )


	return answer_one, answer_two


# z i  = z i-1 + deltah * f'( t, zi )

#x ̇(t) = 0.87x(t) − 0.27x(t)y(t)
#y ̇(t) = −0.38 y(t) + 0.25 y(t)x(t)

# xi = x i-1 + h * ( 0.87x(t) − 0.27x(t)y(t) )
# xi = x i-1 + h *  0.87x(t) − h * 0.27x(t)y(t)
#
#
#

# F1 = Xn + H*( 0.087-1 )*Xn+1 - H * ( 0.027 ) * Xn+1 Yn+1 = 0
# F2 = Yn - H *( 0.38 + 1 ) * Yn+1 + H* 0.25 Yn+1*Xn+1 = 0

# F1 / dx   F1 / dy
# F2 / dx   F2 / dy  ===}  calcular e inverter

# df1 / dx = h*(0.087-1) - h*(0.027)*yn1
# df1 / dy = - h * ( 0.027 ) * xn_1
# df2 / dx = h * 0.25 yn_1
# df2 / dy = - h *( 0.038 + 1 ) + h * 0.25 * xn_1

def euler_implicit_2d( begin_one, begin_two, time_initial, time_final, _derivative_one, _derivative_two, number_of_iterations, jaconian ):

	delta_h = ( time_final - time_initial )/float(number_of_iterations)
	answer_one = [begin_one]
	answer_two = [begin_two]


    jaconian = [ lanbda x, y:  ]

	for i in range( 1, number_of_iterations ):

		xnext, ynext = newton_d2( answer_one[-1], answer_two[-1], jaconian, f1, f2 )
		answer_one.append( x_current )
		answer_two.append( y_current )

	return answer_one, answer_two


if __name__ == '__main__':
	x_initial = 3.5
	y_initial = 2.7
	###############
	aproximation_x, aproximation_y = trapeze( x_initial, y_initial, 0.0, 1.0, x_one_derivative, x_two_derivative, number_of_iterations = 500 )
	#TODO how to plot with 3 variables?
	time = np.arange( 0.0, 1.0, 1.0/500.0 )
	print( len(aproximation_x), len(time) )
	plt.plot( time, aproximation_x, color = 'green' )
	plt.plot( time, aproximation_y, color = 'red' )
	plt.xlabel('time')
	plt.ylabel('aproximações')
	plt.show()
