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



#inicios é um numpy array com os valores iniciais de X1, X2, X3, em diante.
#derivadas é um numpy array de funções que deve ter o mesmo tamanho que inícios.
#tempo inicial, tempo final: Float
#num_iteracoes: inteiro

#Euler explicito para várias dimenssões

def euler_multidim( inicios, tempo_inicial, tempo_final, derivadas, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial)/num_iteracoes
	num_dim = len( inicios )
	answer = np.zeros( num_dim, num_iteracoes )
	answer[ :, 0] = inicios
	tempo = np.arange( tempo_inicial, tempo_final, delta_h )

	for i in range(1,num_iteracoes):
		for dim in num_dim:
			answer[ dim ][ i ] = answer[dim] [i-1] + delta_h * derivadas[dim]( answer[:, i-1], tempo[i] )

	return answer


#If nome do arquivo == None, a função retorna os valores das integrais.
#CAso o contrário, a função escreverá esses valores no arquivo.
#TODO adaptar para várias variáveis
def euler_modificado_2d( x_inicial, y_inicial, derx, dery, deltah, t_inicial= 0, t_final = None ,nome_do_arquivo = None ):

	if(nome_do_arquivo is None):
		x = [x_inicial]
		y = [y_inicial]

	else:
		arquivo = open( nome_do_arquivo, 'w')
		arquivo.writelines( '{} {}\n'.format( x_inicial, y_inicial ) )

	t = t_inicial
	x_atual, y_atual= x_inicial, y_inicial

	while( t <= t_final ):
		t = t + deltah

		dx1 = derx( t, x_atual, y_atual )
		dy1 = dery( t, x_atual, y_atual )
		dy2 = dery( t + deltah , x_atual + deltah*dx1, y_atual + deltah*dy1 )
		dx2 = derx( t + deltah, x_atual + deltah*dx1, y_atual + deltah*dy1 )

		y_atual = y_atual + 0.5*deltah*( dy1 + dy2 )
		x_atual = x_atual + 0.5*deltah*( dx1 + dx2 )

		if( nome_do_arquivo is None ):
			x.append( x_atual )
			y.append( y_atual )

		else:
			arquivo.writelines( '{}	{}	{}\n'.format( t, x_atual, y_atual ) )


	if( nome_do_arquivo is None ):
		return x, y

	else:
		arquivo.close()

#TODO testar
#If nome do arquivo == None, a função retorna os valores das integrais.
#CAso o contrário, a função escreverá esses valores no arquivo.
#valores iniciais: Numpy array
def euler_modificado_multidim( valores_iniciais, derivadas, deltah, t_inicial = 0, t_final = None, nome_do_arquivo = None ):

	#if(nome_do_arquivo is None):
	num_iteracoes = ( t_final - t_inicial )/deltah
	answer = np.zeros(( ndim, num_iteracoes ))

#	else:
#		arquivo = open( nome_do_arquivo, 'w')
#		arquivo.writelines( valores_iniciais )

	t = t_inicial
	ndim = valores_iniciais.shape[0]
	#x_atual, y_atual= x_inicial, y_inicial

	for i in range( num_iteracoes ):

		#dx1 = derx( t, x_atual, y_atual )
		#dy1 = dery( t, x_atual, y_atual )
		d1 = [ der[j]( t, answer[ : ][ i ] ) for j in ndim ]

		#dy2 = dery( t + deltah , x_atual + deltah*dx1, y_atual + deltah*dy1 )
		#dx2 = derx( t + deltah, x_atual + deltah*dx1, y_atual + deltah*dy1 )

		d2 = [ der[j]( t + deltah, answer[ : ][ i ] + deltah*d1 ) ]

		#y_atual = y_atual + 0.5*deltah*( dy1 + dy2 )
		#x_atual = x_atual + 0.5*deltah*( dx1 + dx2 )

		answer[ : ][ i+1 ] = answer[ : ][i] + deltah * (( d1 + d2 ) / 2.0)

		#if( nome_do_arquivo is None ):
		#	x.append( x_atual )
		#	y.append( y_atual )

		#else:
		#	arquivo.writelines( '{}	{}	{}\n'.format( t, x_atual, y_atual ) )

		t = t + deltah


	return answer





