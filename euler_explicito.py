# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.

#primeiro teste do algoritmo de euler para python 2.7
#nesta versao nao me preocupei com a eficiencia e nem com o rigor, a intencao era apenas testar o algoritmo de euler.


import matplotlib.pyplot as plt
import math
import numpy as np


#calcula o erro para os parametros escolhidos do metodo de euler
# e(t,h) = ( euler(t,2*delta_t) - euler(t,delta_t) )
def erro_euler( dy_dx, delta_t, t ):

	return metodo_euler( dy_dx, 2*delta_t, t ) - metodo_euler( dy_dx, delta_t, t )


#uma derivada usada apenas para testar o metodo de euler com uma funcao mais simples
#aqui estamos simulando uma funcao com derivada constante
def dy_dx_teste( t ):

	return 0.5


#uma funcao que retorna o tamanho do delta_h para que se tenha o numero de passos desejados
def calcula_delta_t( t_inicial, t_final, numero_de_iteracoes ):

	#return (t_final - t_inicial) / numero_de_iteracoes
	return float(t_final - t_inicial) / float(numero_de_iteracoes)


#derivada da funcao que queremos aproximar no exercicio da tarefa 1
# e^t * (sen(2t) + 2(cos2t))
def dy_dx( t ):

	return math.exp(t)*( math.sin(2*t) + 2*math.cos(2*t) )


#dx_dy é a funcao que representa a devirada
#delta_t eh o tamanho do passo
#y é a funcao que queremos aproximar
def metodo_euler( dy_dx, delta_t, numero_de_iteracoes, y_inicial = 0  ):

	#y_discretizada eh uma lista com os valores que y assume durante as iterações
	y_discretizada = [y_inicial]


	#o menos 1 se deve ao fato de eu considerar o y_inicial como a primeira iteracao
	for i in range(numero_de_iteracoes-1): 
		y_discretizada.append( y_discretizada[-1] + delta_t*dy_dx( y_discretizada[-1] ) )


	return y_discretizada



#eu sei que python nao precisa de main, estou colocando apenas para fins esteticos
def main():

	#este foi o meu primeiro teste, apenas para checar se a sintaxe do programa funcionava
	#teste = metodo_euler( dy_dx_teste, delta_t =  1, numero_de_iteracoes = 5, y_inicial = 1 )
	#print( teste )
	#plt.plot( range(5) , teste, 'ro' )
	#plt.figure()

	#testando com a funcao dy_dx
	#teste_dois = metodo_euler( dy_dx, 0.5, 2, 1 )
	#print(teste_dois)
	#plt.plot( range(2) , teste_dois, 'ro' )
	#plt.plot( range(2) , teste_dois )
	#plt.show()


	#testando a funcao calcula_delta_t
	#for i in range(10):
	#	iteracoes = 2**i 
	#	delta_t = calcula_delta_t( 0, 1, iteracoes)
	#	print(iteracoes, delta_t)


	#resolucao do problema
	for i in range(5, 10):
		numero_de_iteracoes = 2**i
		delta_t = calcula_delta_t(0, 1, numero_de_iteracoes)
		y_aproximada = metodo_euler( dy_dx, delta_t, numero_de_iteracoes, y_inicial = 1 )
		plt.plot( np.arange( 0, 1, delta_t ), y_aproximada )

	plt.show()

main()