#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import numpy as np
from random import randint
import random
from math import sin
from math import pi
from math import acos



class Bilinear:

	def __init__( self, x_inicial, x_final, y_inicial, y_final, delta, psy, epislon = 0.00001 ):

		self.x_inicial = x_inicial
		self.x_final = x_final
		self.y_inicial = y_inicial
		self.y_final = y_final
		self.delta = delta
		self.psy = psy
		self.size_x = int( float( x_final - x_inicial )/delta ) + 1
		self.size_y = int( float( y_final - y_inicial )/delta ) + 1
		self.malha = np.zeros(( self.size_x , self.size_y ))
		self.epislon = epislon


	def up( self, x ):

	    return int(x) + 1


	#delta, x e y devem estar definidos como float
	# funcao: um ponteiro para a funcao que usaremos como relevo
	def gerar_malha( self ):

		#more efficient if substituted for arrange
		for i in np.arange( self.x_inicial, self.x_final + self.delta, self.delta ):
			for j in np.arange( self.y_inicial, self.y_final + self.delta, self.delta ):

				#print(self.psy( i, j ))
				self.malha[i][j] = self.psy( i, j )

	# malha deve NECESSARIAMENTe se um numpy array
	# x_inicial, y_inicial, delta, x e y devem estar definidos como float
	def interpolar( self, x, y ):

		x_menor = int((x - self.x_inicial)/self.delta)
		x_maior = self.up((x - self.x_inicial)/self.delta)
		y_menor = int((y - self.y_inicial)/self.delta)
		y_maior = self.up((y - self.y_inicial)/self.delta)

		return (( x_maior - x )*( y_maior - y )/(self.delta*self.delta) )*self.malha[x_menor][y_menor] + ((x - x_menor)*(y_maior - y)/(self.delta*self.delta)) * self.malha[y_menor][x_maior] + (( x_maior - x )*( y - y_menor )/(self.delta*self.delta)) * self.malha[y_maior][x_menor] + (( x - x_menor )*( y - y_menor )/(self.delta*self.delta)) * self.malha[y_maior][x_maior]



def fi( x, y ):

	return cos( x/25.0 )*sin( y/25.0 )



def norma( x, y ):

	return ( x*x + y*y ) ** 0.5



def norma3d( xi, yi, zi, xf, yf, zf ):

	return ( (xi-xf)*(xi-xf) + (yi-yf)*(yi-yf) + (zi-zf)*(zi-zf) ) ** 0.5



#returns an random 2d point between [-150, 150]x[-150, 150]
def gerar_posicao_inicial( ):
	x = random.uniform( -150, 150 )
	y = random.uniform( -150, 150 )

	return x, y


#tunando o valor de delta h
def plot():

	deltas_t = [ 1/pow( 2.0, m ) for m in range(0, 6) ]
	x_inicial, y_inicial = gerar_posicao_inicial()

	for delta_t in deltas_t:

		x, y = euler_2d_modificado( x_inicial, y_inicial, xlinha, ylinha, delta_t, None)
		tempo = np.arange( 0, (len(x))*delta_t, delta_t )

		plt.xlim(-150, 150)
		plt.ylim(-150, 150)

		plt.plot( tempo, x, color = 'r', label = 'posicao em x' )
		plt.plot( tempo, y, color = 'b', label = 'posicao em y' )
		plt.title('tragetorias x e y para delta_h = {}'.format(delta_t))
		#plt.savefig( "tarefa 4 para h = {0}".format(str(delta_t)))
		plt.show()


def xlinha_interpolacao( t, x, y, interpolacao ):

	return (( 0.001 - interpolacao.interpolar( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )


def ylinha_interpolacao( t, x, y, interpolacao ):

	return (( -0.001 - interpolacao.interpolar(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


#todo dado um angulo em radianos saber em qual direcao esta o robo
def transform():

	pass


def verifica_colisao( posicoes, tamanho_do_robo ):

		ans = False

		for i in range( len(posicoes) ):
			for j in range( i+1, len(posicoes)):

				if( ((( posicoes[i][0] - posicoes[j][0] )**2 + ( posicoes[i][1] - posicoes[j][1] )**2 )**0.5) < tamanho_do_robo ):
					ans = True

		return ans


#vetor deve ser um numpy array de tamanho 2
def modulo( vetor ):

	return ( vetor[0]*vetor[0] + vetor[1]*vetor[1] )**0.5


def produto_escalar( vetor, vetor2 ):

	return ( vetor[0]*vetor2[0] + vetor[1]*vetor2[1] )


'''
neural: uma rede neural, da classe Network, que traduz a estratégia do robô em virar de acordo com os obstáculos.
interpolacao:  classe Bilinear. método para se aproximar a altura da função fi.
metodo: o metodo de discretização escolhido. para esse caso, o método de euler explícito. pela facilidade em implementa-lo.
xlinha, ylinha: derivadas. tragetória normal o robô para quando não há um obstáculo.
nrobos: ao menos dois, afinal, caso o contrário não poderia haver colisões
'''
def controle( neural, interpolacao, xlinha, ylinha, deltah, obstaculos, nome_do_arquivo, alcance_sensor = 10, nrobos = 2, t_max = 10000 ):

	posicoes = np.random.rand( nrobos, 2 ) #iniciando-os em posicoes aleatorias
	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = np.zeros( (nrobos) )
	t = 0.0
	arquivo.writelines( str(posicoes) )
	colisao  = False

	while( distancia_percorrida.max() < 850.0 and t <= t_max and colisao == False ):
		t = t + deltah
		posicao_anterior = posicoes
		
		for i in range( nrobos ):

			#verificar qual / quais robos estao no alcance do sensor uns dos outros
			adjacencia = False
			visao_do_robo = np.zeros((8))

			for j in range( nrobos ):
				if( j != i and ((( posicoes[i][0] - posicoes[j][0] )**2 + ( posicoes[i][1] - posicoes[j][1] )**2 )**0.5) < alcance_sensor ):
					adjacencia = True

					#fazer o calculo do angulo entre os dois robos, em radianos
					angulo = acos( produto_escalar( posicoes[i], posicoes[j] ) / (modulo(posicoes[i])*modulo(posicoes[j])))

					# 0			1					2		3				4	5					6			7
					# Frente / Frente direita / direita / Direita tras / Tras / Esquerda Tras / Esquerda / esquerda frente

					#se o robo está  na frente
					if( angulo <= pi/8.0 ):
						visao_do_robo[0] = 1

					#se o robo está atras
					elif(angulo >= pi - pi/8.0 ):
						visao_do_robo[4] = 0

					#um pouco de algebra linear para determinarse o robo está na direita ou na esquerda
					else:
						a = (posicoes[i][1] - posicao_anterior[i][1])/(posicoes[i][0] - posicao_anterior[i][0])
						b = posicoes[i][1] - a*posicoes[0]
						#se o robo j esta a direita do robo i
						print( 'a = ', a, 'b = ', b)
						if( a * posicoes[j][0] + b  > posicoes[j][1] ):

							#frente-direita
							if( pi/18.0 < angulo and angulo <= 3.0*pi/8.0 ):
								visao_do_robo[1] = 1

							#direita
							elif( 3.0*pi/8.0 < angulo and angulo <= 5.0 * pi / 8.0 ):
								visao_do_robo[2] = 1

							#direita-tras
							elif( 5.0 * pi / 8.0 < angulo and angulo <= 7.0 * pi / 8.0 ):
								visao_do_robo[3] = 1

						#se o robo j esta a esquerda do robo i
						else:
							#frente-esquerda
							if( pi/18.0 < angulo and angulo <= 3.0*pi/8.0 ):
								visao_do_robo[7] = 1

							#esquerda
							elif( 3.0*pi/8.0 < angulo and angulo <= 5.0 * pi / 8.0 ):
								visao_do_robo[6] = 1

							#esquerda-tras
							elif( 5.0 * pi / 8.0 < angulo and angulo <= 7.0 * pi / 8.0 ):
								visao_do_robo[5] = 1


			#se não ha robo na adjacencia, o robo seguirá o caminho normal definido pela tarefa anterior
			if( adjacencia == False ):

				posicoes[i][0] =  posicao_anterior[i][0] + deltah*xlinha( t, posicao_anterior[i][0], posicao_anterior[i][1], interpolacao )
				posicoes[i][1] =  posicao_anterior[i][1] + deltah*ylinha( t, posicao_anterior[i][0], posicao_anterior[i][1], interpolacao ) 

			#caso o contrário, será acionada a rede que vai tratar de virar o robô na direçao desejada pra que se evite a colisão. a velocidade do robo permanecerá constante.
			else: 

				comando = np.argmax(neural.run_line( visao_do_robo ))

				if( comando == 0 ):
					posicoes[ j ][ 0 ] = posicoes[ j ][ 0 ] + velocity[ j ][ 0 ]
					posicoes[ j ][ 1 ] = posicoes[ j ][ 1 ] + velocity[ j ][ 1 ]

				#virar 90 graus a direita
				if( comando == 1 ):
					posicoes[ j ][ 0 ] = posicoes[ j ][ 0 ] + velocity[ j ][ 0 ]
					posicoes[ j ][ 1 ] = posicoes[ j ][ 1 ] - velocity[ j ][ 1 ]

				#virar noventa graus a esquerda
				if( comando == 2 ):
					posicoes[ j ][ 0 ] = posicoes[ j ][ 0 ] - velocity[ j ][ 0 ]
					posicoes[ j ][ 1 ] = posicoes[ j ][ 1 ] + velocity[ j ][ 1 ]

				#dar meia volta
				if( comando == 3 ):
					posicoes[ j ][ 0 ] = posicoes[ j ][ 0 ] - velocity[ j ][ 0 ]
					posicoes[ j ][ 1 ] = posicoes[ j ][ 1 ] - velocity[ j ][ 1 ]

			distancia_percorrida[i] = distancia_percorrida[i] + norma3d( posicao_anterior[i][0], posicao_anterior[i][1], interpolacao.interpolar(posicao_anterior[i][0], posicao_anterior[i][1]), posicoes[i][0], posicoes[i][1], interpolacao.interpolar( posicoes[i][0], posicoes[i][1] ) )

		colisao = verifica_colisao( posicoes )
		arquivo.writelines( str(posicoes) )

	arquivo.close()



if __name__ == '__main__':
	pass





