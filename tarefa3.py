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




def baskara( a, b, c ):
	delta = b*b - 4.0*a*c
#	print( a, b, c )
	if( delta < 0 ):
		print( "delta negativoooo" )
#	print(delta)
	x1 = ( -b + math.sqrt( delta ) ) / 2.0*a
	x2 = ( -b - math.sqrt( delta ) ) / 2.0*a
	return x1, x2


def x_um_linha( x_um, x_dois, tempo ):

	return 0.87 * x_um - 0.27 * x_um * x_dois



def x_dois_linha( x_um, x_dois, tempo ):

	return -0.038 * x_dois + 0.25 * x_dois * x_um


'''
trapezio
yk+1 = yk + h*0.5*( f(tk, yk) + f( tk+1, yk+1 ) )


X1 = X0 + H*fi( X1, Y1, T1 )
Y1 = Y0 + H*fi( Y1, X1, T1 )

X1 = X0 + H*1/2*( X'( X0, Y0 ) + X'(X1, Y1) )
Y1 = Y0 + H*1/2*( Y'(Y0, X0) + Y'(X1, Y1) )

X1 = X0 + H*1/2*( 0.87*X0 - 0.27*X0*Y0 + 0.87*X1 - 0.27*X1*Y1 )
Y1 = Y0 + H*1/2*( -0.038*Y0 +0.25*Y0*X0 - 0.038*Y1 + 0.25*Y1*X1 )

X1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 - H*1/2*0.27*X1*Y1         (*0.25)     SOMA AS DUAS
Y1 = Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 - H*1/2*0.038*Y1 + H*1/2*0.25*Y1*X1      (*0.27)


X1 + Y1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 - H*1/2*0.038*Y1
Y1 + H*1/2*0.038*Y1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 
Y1( 1 + H*1/2*0.038 ) = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 
Y1 = ( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 )    (EQ 1)


X1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 - H*1/2*0.27*X1*Y1         (SUBSTITUI 1)
X1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 - H*1/2*0.27*X1*( ( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 ) )
X1 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 - H*1/2*0.27*X1*( ( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 +  Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 ) ) + H*1/2*0.27*X1*(X1 + H*1/2*0.87*X1)/( 1 + H*1/2*0.038 )

0 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + H*1/2*0.87*X1 -X1 - H*1/2*0.27*X1*( ( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 +  Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 ) ) +  X1*X1*H*1/2*0.27*( 1 + H*1/2*0.87)/( 1 + H*1/2*0.038 )


0 = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1*( H*1/2*0.87 -1 - H*1/2*0.27*( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 +  Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 )) +  X1*X1 (*H*1/2*0.27*( 1 + H*1/2*0.87)/( 1 + H*1/2*0.038 ))

C = X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0
B = ( H*1/2*0.87 -1 - H*1/2*0.27*( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 +  Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 ))
A = (H*1/2*0.27*( 1 + H*1/2*0.87)/( 1 + H*1/2*0.038 ))


'''

def trapezio( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial )/float(num_iteracoes)
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]

	A = (delta_h*0.5*0.27*( 1 + delta_h*0.5*0.87)/( 1 + delta_h*0.5*0.038 ))
	B = ( delta_h*0.5*0.87 -1 - delta_h*0.5*0.27*( inicio_um + delta_h*0.5*0.87*inicio_um - delta_h*0.5*0.27*inicio_um*inicio_dois + inicio_dois + delta_h*0.5*-0.038*inicio_dois + delta_h*0.5*0.25*inicio_dois*inicio_um )/( 1 + delta_h*0.5*0.038 ))
	C =  inicio_um + delta_h*0.5*0.87*inicio_um - delta_h*0.5*0.27*inicio_um*inicio_dois

	for i in range( 1, num_iteracoes ):
		x1, x2 = baskara( A, B, C )
		if( x1>x2 ):
			maior = x1
		else:
			maior = x2

		#Y1 = ( X0 + H*1/2*0.87*X0 - H*1/2*0.27*X0*Y0 + X1 + H*1/2*0.87*X1 + Y0 + H*1/2*-0.038*Y0 + H*1/2*0.25*Y0*X0 )/( 1 + H*1/2*0.038 )
		answer_dois.append(( answer_um[-1] + delta_h*0.5*0.87*answer_um[-1] - delta_h*0.5*0.27*answer_um[-1]*answer_dois[-1] + maior + delta_h*0.5*0.87*maior + answer_dois[-1] + delta_h*0.5*-0.038*answer_dois[-1] + delta_h*0.5*0.25*answer_dois[-1]*answer_um[-1] )/( 1.0 + delta_h*0.5*0.038 ))
		answer_um.append( maior )


		B = ( delta_h*0.5*0.87 -1 - delta_h*0.5*0.27*( answer_um[-1] + delta_h*0.5*0.87*answer_um[-1] - delta_h*0.5*0.27*answer_um[-1]*answer_dois[-1] + answer_dois[-1] + delta_h*0.5*-0.038*answer_dois[-1] + delta_h*0.5*0.25*answer_dois[-1]*answer_um[-1] )/( 1 + delta_h*0.5*0.038 ))
		C =  answer_um[-1] + delta_h*0.5*0.87*answer_um[-1] - delta_h*0.5*0.27*answer_um[-1]*answer_dois[-1]

	return answer_um, answer_dois




'''
X' = 0.87*X - 0.27*X*Y
Y' = -0.0038*Y + 0.25*X*Y


X1 = X0 + H*X'( X1, Y1, T1 )
Y1 = Y0 + H*Y'( Y1, X1, T1 )

X1 = X0 + H*0.87X1 - H*0.27X1*Y1
Y1 = Y0 - H* 0.0038*Y1 + H*0.25*X1*Y1


0.25X1 = 0.25*X0 + 0.25*H*0.87X1 - 0.25*H*0.27X1*Y1
0.27Y1 = 0.27*Y0 - 0.27*H* 0.0038*Y1 + 0.27*H*0.25*X1*Y1

0.25X1 + 0.27Y1 = 0.25*X0 + 0.27*Y0 - 0.27*H* 0.0038*Y1+ 0.25*H*0.87*X1
0.27Y1 - 0.27*H*0.0038*Y1 = 0.25*X0 + 0.27*Y0 + 0.25*H*0.87*X1 + 0.25X1
Y1( 0.27 - 0.27*H*0.038 ) = 0.25*X0 + 0.27*Y0 + 0.25*H*0.87*X1 + 0.25X1
Y1 = ( 0.25*X0 + 0.27*Y0 + 0.25*H*0.87*X1 + 0.25X1 )/ ( 0.27 - 0.27*H*0.038 )

X1 = X0 + H*0.87X1 - H*0.27X1*Y1
X1 = X0 + H*0.87X1 - H*0.27X1*( 0.25*X0 + 0.27*Y0 + 0.25*H*0.87*X1 + 0.25X1 )/ ( 0.27 - 0.27*H*0.038 )

X1 = X0 + H*0.87X1 - H*0.27X1*( 0.25*X0 + 0.27*Y0 )/ ( 0.27 - 0.27*H*0.038 ) + X1*X1*( H*0.27*0.25*H*0.87 + H*0.27*0.25 )/( 0.27 - 0.27*H*0.038 )
0 = X0 - X1 + H*0.87X1 - H*0.27X1*( 0.25*X0 + 0.27*Y0 )/ ( 0.27 - 0.27*H*0.038 ) + X1*X1*( H*0.27*0.25*H*0.87 + H*0.27*0.25 )/( 0.27 - 0.27*H*0.038 )


    C        b   																				A
0 = X0 + X1*( -1 + H*0.87 - H*0.27*( 0.25*X0 + 0.27*Y0 )/ ( 0.27 - 0.27*H*0.038 ) ) + X1*X1*( H*0.27*0.25*H*0.87 + H*0.27*0.25 )/( 0.27 - 0.27*H*0.038 )


Y1 + H* 0.0038*Y1 - H*0.25*X1*Y1 = Y0 
Y1*( 1 + H* 0.0038 - H*0.25*X1 ) = Y0
Y1 = Y0/( 1 + H * 0.0038 - H*0.25*X1 )

'''


def euler_implicito_presa_predador( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial )/float(num_iteracoes)
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]
	A = ( delta_h*0.27*0.25*delta_h*0.87 + delta_h*0.27*0.25 )/( 0.27 - 0.27*delta_h*0.038)
	B = ( -1.0 + delta_h*0.87 - delta_h*0.27*( 0.25*inicio_um + 0.27*inicio_dois ))/( 0.27 - 0.27*delta_h*0.038 )
	C = inicio_um

	for i in range( 1, num_iteracoes ):
		x1, x2 = baskara( A, B, C )
		if( x1>x2 ):
			maior = x1
		else:
			maior = x2
		answer_um.append( maior )
		answer_dois.append( answer_dois[-1]/( 1.0 + delta_h*0.038 - delta_h*0.25*maior) )

		B = ( -1.0 + delta_h*0.87 - delta_h*0.27*( 0.25*maior + 0.27*answer_dois[-1]))/( 0.27 - 0.27*delta_h*0.038 )
		C = maior

	return answer_um, answer_dois


#tempo inicial, tempo final: Float
#num_iteracoes: inteiro
#apenas um teste
def euler_presa_predador( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial )/num_iteracoes
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]

	for i in range(1,num_iteracoes):
			answer_um.append( answer_um[-1] + derivada_um( answer_um[-1], answer_dois[-1], float(i-1)*delta_h ) )
			answer_dois.append( answer_dois[-1] + derivada_dois( answer_um[-1], answer_dois[-1], float(i-1)*delta_h ) )
	return answer_um, answer_dois



#print( baskara( 1, -2, -1 ) )


def main():
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
	

main()












