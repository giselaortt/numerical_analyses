
#!/bin/python

from math import cos
from math import sin
import random
import numpy as np
import matplotlib.pyplot as plt

#from map2220_animation_v3 import gen_anim
#Aluna Gisela Moreira Ortt nusp 8937761



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


def euler_2d( x_inicial, y_inicial, derx, dery, deltah, nome_do_arquivo ):

	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_atual, y_atual= x_inicial, y_inicial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_atual, y_atual ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_atual ) and ( x_atual < 150.0 ) and ( -150.0 < y_atual) and ( y_atual < 150.0 )  ):
		t = t + deltah
		x_anterior, y_anterior = x_atual, y_atual
		x_atual =  x_anterior + deltah*derx( t, x_anterior, y_anterior ) 
		y_atual = y_anterior + deltah*dery( t, x_anterior, y_anterior ) 
		distancia_percorrida = distancia_percorrida + norma3d( x_anterior, y_anterior, fi(x_anterior, y_anterior), x_atual, y_atual, fi( x_atual, y_atual ) )
		arquivo.writelines( '{}	{}	{}\n'.format( t, x_atual, y_atual ) )

	arquivo.close()


def euler_2d_modificado( x_inicial, y_inicial, derx, dery, deltah, nome_do_arquivo = None ):

	if(nome_do_arquivo is None):
		x = [x_inicial]
		y = [y_inicial]

	else:
		arquivo = open( nome_do_arquivo, 'w')
		arquivo.writelines( '{} {}\n'.format( x_inicial, y_inicial ) )

	distancia_percorrida = 0.0
	t = 0.0
	x_atual, y_atual= x_inicial, y_inicial

	while( distancia_percorrida < 850.0 and ( -150.0 < x_atual ) and ( x_atual < 150.0 ) and ( -150.0 < y_atual) and ( y_atual < 150.0 ) ):
		t = t + deltah

		dx1 = derx( t, x_atual, y_atual )
		dy1 = dery( t, x_atual, y_atual )
		dy2 = dery( t + deltah , x_atual + deltah*dx1, y_atual + deltah*dy1 )
		dx2 = derx( t + deltah, x_atual + deltah*dx1, y_atual + deltah*dy1 )

		y_proximo = y_atual + 0.5*deltah*( dy1 + dy2 )
		x_proximo = x_atual + 0.5*deltah*( dx1 + dx2 )

		distancia_percorrida = distancia_percorrida + norma3d( x_atual, y_atual, fi( x_atual, y_atual ), x_proximo, y_proximo, fi( x_proximo, y_proximo ) )
		x_atual, y_atual = x_proximo, y_proximo

		if( nome_do_arquivo is None ):
			x.append( x_atual )
			y.append( y_atual )
		else:
			arquivo.writelines( '{}	{}	{}\n'.format( t, x_atual, y_atual ) )


	if( nome_do_arquivo is None ):
		return x, y
	else:
		arquivo.close()



def euler_2d_interpolacao( x_inicial, y_inicial, derx, dery, deltah, nome_do_arquivo, inter ):
	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_atual, y_atual= x_inicial, y_inicial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_atual, y_atual ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_atual ) and ( x_atual < 150.0 ) and ( -150.0 < y_atual) and ( y_atual < 150.0 )):
		t = t + deltah
		x_anterior, y_anterior = x_atual, y_atual
		x_atual =  x_anterior + deltah*derx( t, x_anterior, y_anterior, inter ) 
		y_atual = y_anterior + deltah*dery( t, x_anterior, y_anterior, inter ) 

		distancia_percorrida = distancia_percorrida + norma3d( x_anterior, y_anterior, inter.interpolar(x_anterior, y_anterior), x_atual, y_atual, inter.interpolar( x_atual, y_atual ) )
		arquivo.writelines( '{}	{}	{}\n'.format( t, x_atual, y_atual ) )

	arquivo.close()



def euler_2d_modificado_interpolacao( x_inicial, y_inicial, derx, dery, deltah, nome_do_arquivo, interpolacao ):
	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_atual, y_atual= x_inicial, y_inicial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_atual, y_atual ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_atual ) and ( x_atual < 150.0 ) and ( -150.0 < y_atual) and ( y_atual < 150.0 ) ):
		t = t + deltah

		dx1 = derx( t, x_atual, y_atual, interpolacao )
		dy1 = dery( t, x_atual, y_atual, interpolacao )
		dy2 = dery( t + deltah , x_atual + deltah*dx1, y_atual + deltah*dy1, interpolacao )
		dx2 = derx( t + deltah, x_atual + deltah*dx1, y_atual + deltah*dy1, interpolacao )

		y_proximo = y_atual + 0.5*deltah*( dy1 + dy2 )
		x_proximo = x_atual + 0.5*deltah*( dx1 + dx2 )

		distancia_percorrida = distancia_percorrida + norma3d( x_atual, y_atual, interpolacao.interpolar( x_atual, y_atual ), x_proximo, y_proximo, interpolacao.interpolar( x_proximo, y_proximo ) )
		x_atual, y_atual = x_proximo, y_proximo
		arquivo.writelines( '{}	{}\n'.format(x_atual, y_atual ) )
		pass

	arquivo.close()


def xlinha( t, x, y ):

	return (( 0.001 - fi( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )



def ylinha( t, x, y ):

	return (( -0.001 - fi(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


def xlinha_interpolacao( t, x, y, interpolacao ):

	return (( 0.001 - interpolacao.interpolar( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )


def ylinha_interpolacao( t, x, y, interpolacao ):

	return (( -0.001 - interpolacao.interpolar(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


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



def main():

	#tarefa 4 parte 1
	x_inicial, y_inicial = gerar_posicao_inicial()
	deltah = 0.001
	euler_2d_modificado(  x_inicial, y_inicial, xlinha, ylinha, deltah, "posicao do robo m explicito.txt"  )

	#animar( "posicao do robo.txt" )

	#tarefa 4 parte 2
	inter = Bilinear( x_inicial = -150, x_final = 150, y_inicial = -150, y_final = 150, delta = 0.5, psy = fi )
	inter.gerar_malha() 
	euler_2d_modificado_interpolacao( x_inicial, y_inicial, xlinha_interpolacao, ylinha_interpolacao, deltah, "posicao do robo (interpolacao).txt", inter )



if __name__ == '__main__':
	main()


