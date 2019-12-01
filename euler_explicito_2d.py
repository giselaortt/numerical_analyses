# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


'''
ALUNA:  GISELA MOREIRA ORTT
NUSP:   8937761
'''


import numpy as np 
import matplotlib.pyplot as plt
import math


'''
z = |x| 
    |y|

zi = zi-1 + h * z`( zi-1 )

zi+1 = | xi | + h * | x`(xi, yi, ti) |
       | yi |       | y`(xi, yi, ti) |

'''


def x_um_linha( x_um, x_dois, tempo ):

	return 0.87 * x_um - 0.27 * x_um * x_dois



def x_dois_linha( x_um, x_dois, tempo ):

	return -0.038 * x_dois + 0.25 * x_dois * x_um


#tempo inicial, tempo final: Float
#num_iteracoes: inteiro
#apenas um teste
def euler( inicio_um, inicio_dois, tempo_inicial, tempo_final, derivada_um, derivada_dois, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial )/float(num_iteracoes)
	answer_um = [inicio_um]
	answer_dois = [inicio_dois]

	for i in range(1,num_iteracoes):
			answer_um.append( answer_um[i-1] + delta_h * derivada_um( answer_um[i-1], answer_dois[i-1], float(i-1)*delta_h ) )
			answer_dois.append( answer_dois[i-1] + delta_h * derivada_dois( answer_um[i-1], answer_dois[i-1], float(i-1)*delta_h ) )
	return answer_um, answer_dois


def main():
	x_inicial = 3.5
	y_inicial = 2.7
	n = 500

	aprox_x, aprox_y = euler( x_inicial, y_inicial, 0.0, 1.0, x_um_linha, x_dois_linha, num_iteracoes = n )

	tempo = np.arange( 0.0, 1.0, 1.0/float(n) )
	print( len(aprox_x), len(tempo) )
	plt.plot( tempo, aprox_x, color = 'green' )
	plt.plot( tempo, aprox_y, color = 'red' )
	plt.xlabel('tempo')
	plt.ylabel('aproximações')
	plt.show()
	

main()

