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


def x_um_linha( x_um, x_dois, tempo ):

	return 0.87 * x_um - 0.27 * x_um * x_dois


def x_dois_linha( x_um, x_dois, tempo ):

	return -0.038 * x_dois + 0.25 * x_dois * x_um


# fi(x) = x - f(x) / f'(x)
# jacobiano : array de funcoes!
# x_anterior : numpy array
# x_atual : array type, sized ndim
# f: Array type, size equals ndim.
# Duvida: Qual vai ser a minha condição de parada?
def newton_multidim( ndim, x_anterior, x_atual, jacobiano, f, precision = 0.0001 ):

	#Dowhile em python?
	while( ( abs(x_anterior - x_atual ).any() > precision ) ):

		x_atual = x_anterior - jacobiano[ 0 ][ 0 ]( x_anterior )*f1( x_anterior, x_atual ) - jacobiano[ 0 ][ 1 ]( x_anterior )*f2( x_anterior, x_atual )
		y_atual = y_anterior - jacobiano[ 1 ][ 0 ]( x_anterior )*f1( x_anterior, x_atual ) - jacobiano[ 1 ][ 1 ]( x_anterior )*f2( x_anterior, x_atual )

	return x_atual, y_atual


#
#
def trapezio_2d( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes, jacobiano ):

	delta_h = ( tempo_final - tempo_inicial )/float(num_iteracoes)
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]


	for i in range( 1, num_iteracoes ):

		x_atual, y_atual = 
		answer_dois.append( x_atual )
		answer_um.append( y_atual )


	return answer_um, answer_dois


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

def euler_implicito_2d( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes, jacobiano ):

	delta_h = ( tempo_final - tempo_inicial )/float(num_iteracoes)
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]


    jacobiano = [ lanbda x, y:  ]

	for i in range( 1, num_iteracoes ):

		xnext, ynext = newton_d2( answer_um[-1], answer_dois[-1], jacobiano, f1, f2 )
		answer_um.append( x_atual )
		answer_dois.append( y_atual )

	return answer_um, answer_dois


if __name__ == '__main__':
	x_inicial = 3.5
	y_inicial = 2.7
	###############
	aprox_x, aprox_y = trapezio( x_inicial, y_inicial, 0.0, 1.0, x_um_linha, x_dois_linha, num_iteracoes = 500 )
	#TODO how to plot with 3 variables?
	tempo = np.arange( 0.0, 1.0, 1.0/500.0 )
	print( len(aprox_x), len(tempo) )
	plt.plot( tempo, aprox_x, color = 'green' )
	plt.plot( tempo, aprox_y, color = 'red' )
	plt.xlabel('tempo')
	plt.ylabel('aproximações')
	plt.show()
