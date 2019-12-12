#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import numpy as np
from random import randint
import random
from math import sin


'''
Pesquisar:
	Variaveis globais ou define em python
	funções de ativação e suas características

	
'''

#funcao de ativacao linear?
class Network:
	def __init__( self, inputSize, hiddenSize, outputSize, hiddenLayer = None, outputLayer = None ):
		self.inputSize = inputSize
		self.hiddenSize = hiddenSize
		self.outputSize = outputSize

		if( hiddenLayer is None ):

			self.hiddenLayer = np.random.rand( inputSize + 1, hiddenSize ) - 0.5

		else:

			self.hiddenLayer = hiddenLayer

		if( outputLayer is None ):

			self.outputLayer = np.random.rand( hiddenSize + 1, outputSize ) - 0.5

		else:

			self.outputLayer = outputLayer


    # Calcula a saída da rede para um padrão de entrada
    # input: numpy array com tamanho indicado em inputSize
    # Retorna um numero inteiro entre zero e outputSize
	def run( self, pattern ):
    	
		#if( len(pattern) != self.inputSize ):
		#	print( "Erro de tamanho" )
		#	return
    	#
		
		ans = np.matmul( pattern, self.hiddenLayer[ :self.inputSize, : ] ) + self.hiddenLayer[ self.inputSize, :]
		#
    	#ans = self.actvation_function( ans )
		ans = np.matmul( ans, self.outputLayer[ :self.hiddenSize, : ] ) + self.outputLayer[ self.hiddenSize, : ]
		#ans = self.actvation_function( ans )

		return ans


	def write_to_file( self, nome_do_arquivo ):

		np.savetxt( nome_do_arquivo, self.hiddenLayer, delimiter=' ')
		np.savetxt( nome_do_arquivo, self.outputLayer, delimiter=' ')


    # vou usar a funcao de ativação mais tradicional e mais simples na literatura de redes neurais.
    # em tese, a funcao de ativaçao deveria fazer nenhuma ou muito pouca diferença no resultado final.
#    def actvation_function(self):

#    	return = 1.0 / ( 1.0 + np.exp( -x ) )
		



def teste():
	net = Network( 3, 5, 6 )
	print( net.run( np.array([ 1, 1, 1 ]).reshape(1,3) ) )



if __name__ == '__main__':
	teste()


