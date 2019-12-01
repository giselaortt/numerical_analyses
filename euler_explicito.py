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
#suponho que a contagem do tempo se inicie no tempo zero
#TODO adaptar a funcao para definir o delta_t na chamada
def metodo_euler( dy_dx, t_final, t_inicial = 0, delta_t = None, numero_de_iteracoes = None, y_inicial = 0  ):

	y = [y_inicial]

	if(delta_t is None):
		delta_t = t_final / numero_de_iteracoes

	tempo = np.arange( t_inicial, t_final, delta_t )
	for t in  tempo :
		y.append( y[-1] + delta_t*dy_dx(t) )

	return y



def metodo_euler_modificado( dy_dx, t_final, t_inicial = 0, numero_de_iteracoes = None, delta_t = None, y_inicial = 0 ):

	y = [y_inicial]
	if(delta_t is None):
		delta_t = float(t_final)/float(numero_de_iteracoes)

	tempo = np.arange( t_inicial, t_final, delta_t )
	for t in  tempo :
		y.append( y[-1] + delta_t*((dy_dx(t) + dy_dx(t + delta_t))/2.0))

	return y



#é necessaria uma analise prévia que garanta:
#	a derivada nos pontos inicial e final tenham sinais diferentes
#	haja apenas uma solucao no intervalo
# mais ou menos como uma busca binaria?
def dicotomia( dy_dx, inicio_do_intervalo, fim_do_intervalo, precisao = 0.0001 ):

	if( dy_dx(fim_do_intervalo) >= 0 and dy_dx(inicio_do_intervalo) <=0 ):
		concavidade = True

	elif( dy_dx(fim_do_intervalo)  <= 0 and dy_dx(inicio_do_intervalo) >= 0 ):
		concavidade = False

	else:
		print('Erro!')
		return


	pivo = (inicio_do_intervalo + fim_do_intervalo)/2.0
	derivada = dy_dx(pivo)

	while( -1.0*precisao >= derivada and derivada >= precisao ):

		if( derivada >= 0 ):
			if( concavidade is True ):
				inicio_do_intervalo = pivo
			else:
				fim_do_intervalo = pivo
		else:
			if( concavidade is True ):
				fim_do_intervalo = pivo
			else:
				inicio_do_intervalo = pivo

		pivo = (inicio_do_intervalo + fim_do_intervalo)/2.0
		derivada = dy_dx(pivo)

	return pivo




#inicios é um numpy array com os valores iniciais de X1, X2, X3, em diante.
#derivadas é um numpy array de funções que deve ter o mesmo tamanho que inícios.
#tempo inicial, tempo final: Float
#num_iteracoes: inteiro
def euler_presa_predador( inicios, tempo_inicial, tempo_final, derivadas, num_iteracoes ):

	delta_h = ( tempo_final - tempo_inicial)/num_iteracoes
	num_dim = len( inicios )
	answer = np.zeros( num_dim, num_iteracoes )
	answer[ :, 0] = inicios
	tempo = np.arange( tempo_inicial, tempo_final, delta_h )

	for i in range(1,num_iteracoes):
		for dim in num_dim:
			answer[ dim ][ i ] = answer[dim] [i-1] + derivadas[dim]( answer[:, i-1], tempo[i] )

	return answer



#TODO
def newton():
	pass


#TODO
def newton_multidimensional():
	pass


