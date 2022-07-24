
#!/bin/python

from math import cos
from math import sin
import random
import numpy as np
import matplotlib.pyplot as plt

#from map2220_animation_v3 import gen_anim
#Aluna Gisela Moreira Ortt nusp 8937761



class Bilinear:
	def __init__( self, x_initial, x_final, y_initial, y_final, delta, psy, epislon = 0.00001 ):
		self.x_initial = x_initial
		self.x_final = x_final
		self.y_initial = y_initial
		self.y_final = y_final
		self.delta = delta
		self.psy = psy
		self.size_x = int( float( x_final - x_initial )/delta ) + 1
		self.size_y = int( float( y_final - y_initial )/delta ) + 1
		self.malha = np.zeros(( self.size_x , self.size_y ))
		self.epislon = epislon


	def up( self, x ):

	    return int(x) + 1


	#delta, x e y ofvem estar definidos como float
	# funcao: um ponteiro para a funcao que usaremos como relevo
	def generate_grid( self ):

		#more efficient if substituted for arrange
		for i in np.arange( self.x_initial, self.x_final + self.delta, self.delta ):
			for j in np.arange( self.y_initial, self.y_final + self.delta, self.delta ):

				#print(self.psy( i, j ))
				self.malha[i][j] = self.psy( i, j )

	# malha ofve NECESSARIAMENTe se um numpy array
	# x_initial, y_initial, delta, x e y ofvem estar definidos como float
	def interpolate( self, x, y ):

		x_smaller = int((x - self.x_initial)/self.delta)
		x_bigger = self.up((x - self.x_initial)/self.delta)
		y_smaller = int((y - self.y_initial)/self.delta)
		y_bigger = self.up((y - self.y_initial)/self.delta)

		return (( x_bigger - x )*( y_bigger - y )/(self.delta*self.delta) )*self.malha[x_smaller][y_smaller] + ((x - x_smaller)*(y_bigger - y)/(self.delta*self.delta)) * self.malha[y_smaller][x_bigger] + (( x_bigger - x )*( y - y_smaller )/(self.delta*self.delta)) * self.malha[y_bigger][x_smaller] + (( x - x_smaller )*( y - y_smaller )/(self.delta*self.delta)) * self.malha[y_bigger][x_bigger]



def fi( x, y ):

	return cos( x/25.0 )*sin( y/25.0 )



def norma( x, y ):

	return ( x*x + y*y ) ** 0.5



def norma3d( xi, yi, zi, xf, yf, zf ):

	return ( (xi-xf)*(xi-xf) + (yi-yf)*(yi-yf) + (zi-zf)*(zi-zf) ) ** 0.5



#returns an random 2d point between [-150, 150]x[-150, 150]
def gerar_posicao_initial( ):
	x = random.uniform( -150, 150 )
	y = random.uniform( -150, 150 )

	return x, y


def euler_2d( x_initial, y_initial, ofrx, ofry, deltah, nome_do_arquivo ):

	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_current, y_current= x_initial, y_initial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_current, y_current ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_current ) and ( x_current < 150.0 ) and ( -150.0 < y_current) and ( y_current < 150.0 )  ):
		t = t + deltah
		x_previous, y_previous = x_current, y_current
		x_current =  x_previous + deltah*ofrx( t, x_previous, y_previous ) 
		y_current = y_previous + deltah*ofry( t, x_previous, y_previous ) 
		distancia_percorrida = distancia_percorrida + norma3d( x_previous, y_previous, fi(x_previous, y_previous), x_current, y_current, fi( x_current, y_current ) )
		arquivo.writelines( '{}	{}	{}\n'.format( t, x_current, y_current ) )

	arquivo.close()


def euler_2d_modified( x_initial, y_initial, ofrx, ofry, deltah, nome_do_arquivo = None ):

	if(nome_do_arquivo is None):
		x = [x_initial]
		y = [y_initial]

	else:
		arquivo = open( nome_do_arquivo, 'w')
		arquivo.writelines( '{} {}\n'.format( x_initial, y_initial ) )

	distancia_percorrida = 0.0
	t = 0.0
	x_current, y_current= x_initial, y_initial

	while( distancia_percorrida < 850.0 and ( -150.0 < x_current ) and ( x_current < 150.0 ) and ( -150.0 < y_current) and ( y_current < 150.0 ) ):
		t = t + deltah

		dx1 = ofrx( t, x_current, y_current )
		dy1 = ofry( t, x_current, y_current )
		dy2 = ofry( t + deltah , x_current + deltah*dx1, y_current + deltah*dy1 )
		dx2 = ofrx( t + deltah, x_current + deltah*dx1, y_current + deltah*dy1 )

		y_proximo = y_current + 0.5*deltah*( dy1 + dy2 )
		x_proximo = x_current + 0.5*deltah*( dx1 + dx2 )

		distancia_percorrida = distancia_percorrida + norma3d( x_current, y_current, fi( x_current, y_current ), x_proximo, y_proximo, fi( x_proximo, y_proximo ) )
		x_current, y_current = x_proximo, y_proximo

		if( nome_do_arquivo is None ):
			x.append( x_current )
			y.append( y_current )
		else:
			arquivo.writelines( '{}	{}	{}\n'.format( t, x_current, y_current ) )


	if( nome_do_arquivo is None ):
		return x, y
	else:
		arquivo.close()



def euler_2d_interpolacao( x_initial, y_initial, ofrx, ofry, deltah, nome_do_arquivo, inter ):
	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_current, y_current= x_initial, y_initial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_current, y_current ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_current ) and ( x_current < 150.0 ) and ( -150.0 < y_current) and ( y_current < 150.0 )):
		t = t + deltah
		x_previous, y_previous = x_current, y_current
		x_current =  x_previous + deltah*ofrx( t, x_previous, y_previous, inter ) 
		y_current = y_previous + deltah*ofry( t, x_previous, y_previous, inter ) 

		distancia_percorrida = distancia_percorrida + norma3d( x_previous, y_previous, inter.interpolate(x_previous, y_previous), x_current, y_current, inter.interpolate( x_current, y_current ) )
		arquivo.writelines( '{}	{}	{}\n'.format( t, x_current, y_current ) )

	arquivo.close()



def euler_2d_modified_interpolacao( x_initial, y_initial, ofrx, ofry, deltah, nome_do_arquivo, interpolacao ):
	arquivo = open( nome_do_arquivo, 'w')
	distancia_percorrida = 0.0
	t = 0.0
	x_current, y_current= x_initial, y_initial
	arquivo.writelines( '{}	{} {}\n'.format( t, x_current, y_current ) )

	while( distancia_percorrida < 850.0 and ( -150.0 < x_current ) and ( x_current < 150.0 ) and ( -150.0 < y_current) and ( y_current < 150.0 ) ):
		t = t + deltah

		dx1 = ofrx( t, x_current, y_current, interpolacao )
		dy1 = ofry( t, x_current, y_current, interpolacao )
		dy2 = ofry( t + deltah , x_current + deltah*dx1, y_current + deltah*dy1, interpolacao )
		dx2 = ofrx( t + deltah, x_current + deltah*dx1, y_current + deltah*dy1, interpolacao )

		y_proximo = y_current + 0.5*deltah*( dy1 + dy2 )
		x_proximo = x_current + 0.5*deltah*( dx1 + dx2 )

		distancia_percorrida = distancia_percorrida + norma3d( x_current, y_current, interpolacao.interpolate( x_current, y_current ), x_proximo, y_proximo, interpolacao.interpolate( x_proximo, y_proximo ) )
		x_current, y_current = x_proximo, y_proximo
		arquivo.writelines( '{}	{}\n'.format(x_current, y_current ) )
		pass

	arquivo.close()


def xlinha( t, x, y ):

	return (( 0.001 - fi( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )



def ylinha( t, x, y ):

	return (( -0.001 - fi(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


def xlinha_interpolacao( t, x, y, interpolacao ):

	return (( 0.001 - interpolacao.interpolate( x, y ) )*( x - 100.0*cos(t) )) / norma( x - 100.0*cos(t), y - 100.0*sin(t) )


def ylinha_interpolacao( t, x, y, interpolacao ):

	return (( -0.001 - interpolacao.interpolate(x, y) )*( y - 100.0*sin(t) ) )/norma( x - 100.0*cos(t), y - 100.0*sin(t) )


#tunando o valor of delta h
def plot():
	deltas_t = [ 1/pow( 2.0, m ) for m in range(0, 6) ]
	x_initial, y_initial = gerar_posicao_initial()

	for delta_t in deltas_t:

		x, y = euler_2d_modified( x_initial, y_initial, xlinha, ylinha, delta_t, None)
		time = np.arange( 0, (len(x))*delta_t, delta_t )

		plt.xlim(-150, 150)
		plt.ylim(-150, 150)

		plt.plot( time, x, color = 'r', label = 'posicao em x' )
		plt.plot( time, y, color = 'b', label = 'posicao em y' )
		plt.title('tragetorias x e y para delta_h = {}'.format(delta_t))
		#plt.savefig( "tarefa 4 para h = {0}".format(str(delta_t)))
		plt.show()



def main():

	#tarefa 4 parte 1
	x_initial, y_initial = gerar_posicao_initial()
	deltah = 0.001
	euler_2d_modified(  x_initial, y_initial, xlinha, ylinha, deltah, "posicao do robo m explicito.txt"  )

	#animar( "posicao do robo.txt" )

	#tarefa 4 parte 2
	inter = Bilinear( x_initial = -150, x_final = 150, y_initial = -150, y_final = 150, delta = 0.5, psy = fi )
	inter.generate_grid() 
	euler_2d_modified_interpolacao( x_initial, y_initial, xlinha_interpolacao, ylinha_interpolacao, deltah, "posicao do robo (interpolacao).txt", inter )



if __name__ == '__main__':
	main()


