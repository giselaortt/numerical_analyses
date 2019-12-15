# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.

#primeiro teste do algoritmo de euler para python 2.7
#nesta versao nao me preocupei com a eficiencia e nem com o rigor, a intencao era apenas testar o algoritmo de euler.
import matplotlib.pyplot as plt
import math
import numpy as np


#calcula o erro para os parametros escolhidos do metodo de euler
# e( t, delta_t ) = ( euler( t, 2*delta_t ) - euler( t, delta_t ) )
def erro_euler( dy_dx, delta_t, t ):

	return metodo_euler( dy_dx, 2*delta_t, t ) - metodo_euler( dy_dx, delta_t, t )



#uma funcao que retorna o tamanho do delta_h para que se tenha o numero de passos desejados
def calcula_delta_t( t_inicial, t_final, numero_de_iteracoes ):

	#return (t_final - t_inicial) / numero_de_iteracoes
	return float(t_final - t_inicial) / float(numero_de_iteracoes)




#dx_dy é a derivada da funcao que vamos aproximar
def metodo_euler( dy_dx, t_final, t_inicial = 0, delta_t = None, numero_de_iteracoes = None, y_inicial = 0  ):

	y = [y_inicial]

	if(delta_t is None):
		delta_t = (t_final - t_inicial) / numero_de_iteracoes

	tempo = np.arange( t_inicial, t_final, delta_t )
	for t in  tempo :
		y.append( y[-1] + delta_t*dy_dx(t, y[-1]) )

	return y



def metodo_euler_modificado( dy_dx, t_final, t_inicial = 0, numero_de_iteracoes = None, delta_t = None, y_inicial = 0 ):

	y = [y_inicial]
	if(delta_t is None):
		delta_t = float(t_final)/float(numero_de_iteracoes)

	tempo = np.arange( t_inicial, t_final, delta_t )
	for t in  tempo :
		k1 = dy_dx(t, y[-1])
		k2 = dy_dx(t + delta_t, y[-1] + delta_t * k1 )
		y.append( y[-1] + (delta_t / 2.0) * ( k1 + k2 ))

	return y



#valores_iniciais é um numpy array com os valores iniciais de X1, X2, X3, em diante.
#derivadas é um numpy array de funções que deve ter o mesmo tamanho que inícios.
#tempo inicial, tempo final: Float
#num_iteracoes: inteiro

#Euler explicito para várias dimenssões

def euler_multidim( valores_iniciais, derivadas, t_inicial = 0, t_final = None, delta_h = None, num_iteracoes = None ):

	if( delta_h == None ):
		delta_h = ( t_final - t_inicial)/num_iteracoes
	elif( num_iteracoes == None ):
		num_iteracoes = int( ( t_final - t_inicial)/delta_h )

	num_dim = len( valores_iniciais )
	answer = np.zeros(( num_dim, num_iteracoes ))
	answer[ :, 0] = valores_iniciais
	tempo = np.arange( t_inicial, t_final, delta_h )

	for i in range(1,num_iteracoes):
		for dim in range(num_dim):
			answer[ dim ][ i ] = answer[dim] [i-1] + delta_h * derivadas[dim]( answer[:, i-1], tempo[i] )

	return answer


#TODO testar
#If nome do arquivo == None, a função retorna os valores das integrais.
#CAso o contrário, a função escreverá esses valores no arquivo.
#valores iniciais: Numpy array
def euler_modificado_multidim( valores_iniciais, derivadas, t_inicial = 0, t_final = None, delta_h = None, num_iteracoes = None ):

	if( delta_h == None ):
		delta_h = ( t_final - t_inicial)/num_iteracoes
	elif( num_iteracoes == None ):
		num_iteracoes = int( ( t_final - t_inicial)/delta_h )

	ndim = valores_iniciais.shape[0]
	answer = np.zeros(( ndim, num_iteracoes ))
	answer[ :, 0 ] = valores_iniciais
	t = t_inicial


	for i in range( num_iteracoes - 1 ):

		d1 = np.array( [ derivadas[j]( t, answer[ : , i] ) for j in range(ndim) ] )
		d2 = np.array( [ derivadas[j]( t + delta_h, answer[ : , i ] + delta_h*d1 ) for j in range(ndim) ] )
		answer[ : , i+1 ] = answer[ : , i] + delta_h * (( d1 + d2 ) / 2.0)
		t = t + delta_h


	return answer





