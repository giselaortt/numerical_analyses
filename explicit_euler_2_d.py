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


def x_one_derivative( x_one, x_two, time ):

	return 0.87 * x_one - 0.27 * x_one * x_two



def x_two_derivative( x_one, x_two, time ):

	return -0.038 * x_two + 0.25 * x_two * x_one


#time initial, time final: Float
#number_of_iterations: inteiro
#apenas um teste
def euler( begin_one, begin_two, time_initial, time_final, _derivative_one, _derivative_two, number_of_iterations ):

	delta_h = ( time_final - time_initial )/float(number_of_iterations)
	answer_one = [begin_one]
	answer_two = [begin_two]

	for i in range(1,number_of_iterations):
			answer_one.append( answer_one[i-1] + delta_h * _derivative_one( answer_one[i-1], answer_two[i-1], float(i-1)*delta_h ) )
			answer_two.append( answer_two[i-1] + delta_h * _derivative_two( answer_one[i-1], answer_two[i-1], float(i-1)*delta_h ) )
	return answer_one, answer_two


def main():
	x_initial = 3.5
	y_initial = 2.7
	n = 500

	aproximation_x, aproximation_y = euler( x_initial, y_initial, 0.0, 1.0, x_one_derivative, x_two_derivative, number_of_iterations = n )

	time = np.arange( 0.0, 1.0, 1.0/float(n) )
	print( len(aproximation_x), len(time) )
	plt.plot( time, aproximation_x, color = 'green' )
	plt.plot( time, aproximation_y, color = 'red' )
	plt.xlabel('time')
	plt.ylabel('aproximações')
	plt.show()
	

main()

