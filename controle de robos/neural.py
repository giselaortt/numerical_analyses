#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import numpy as np
from random import randint
import random
from math import sin
#from datetime import datetime
#import time

'''
Pesquisar:
	Variaveis globais ou define em python
	funções de ativação e suas características

	
	#como verificar se um aray é um vetor ou uma matriz?
'''

#funcao de ativacao linear?
class Network:
	def __init__( self, inputSize, hiddenSize, outputSize, hiddenLayer = None, outputLayer = None ):
		self.inputSize = inputSize
		self.hiddenSize = hiddenSize
		self.outputSize = outputSize

		#np.random.seed( int(time.time()) )

		if( hiddenLayer is None ):

			self.hiddenLayer = np.random.rand( inputSize + 1, hiddenSize )*10 - 5

		else:

			self.hiddenLayer = hiddenLayer

		if( outputLayer is None ):

			self.outputLayer = np.random.rand( hiddenSize + 1, outputSize )*10 - 5

		else:

			self.outputLayer = outputLayer


    # Calcula a saída da rede para um padrão de entrada
    # input: numpy array com tamanho indicado em inputSize
    # Retorna um numero inteiro entre zero e outputSize


    #A saida precisa ser binária!!!
	def run( self, pattern ):
		
		if( pattern.shape[0] != self.inputSize ):
			print( pattern.shape[0] )
			print( "erro de tamanho, tente novamente!" )

		ans = np.matmul( pattern, self.hiddenLayer[ :self.inputSize, : ] ) + self.hiddenLayer[ self.inputSize, :]
		#
		#print(ans)
		ans = self.activation_function( ans )
		np.apply_along_axis( self.activation_function, 0, ans )
		#print(ans)
		ans = np.matmul( ans, self.outputLayer[ :self.hiddenSize, : ] ) + self.outputLayer[ self.hiddenSize, : ]
		#print(ans)
		ans = self.activation_function( ans )

		#np.apply_along_axis( self.activation_function, 0, ans )

		#print(ans)
		#print(ans)

		return ans


	def activation_function( self, vector ):

		return 1 / (1 + np.exp(-vector))
		#for i in range( len( vector ) ):
		#	if( vector[i] > 0 ):
		#		vector[i]  = 1
		#	else:
		#		vector[i] = -1


	def run_multiple( self, pattern ):
		#if( pattern.shape )
		ans = []
		for line in pattern:
			#print(line)
			#print(line.shape)
			ans.append( self.run(line) )
		return np.array( ans )

	#TODO FIX TRHIS SHIT!
	def write_to_file( self, nome_do_arquivo ):

		np.savetxt( nome_do_arquivo, self.hiddenLayer, delimiter=' ')
		np.savetxt( nome_do_arquivo, self.outputLayer, delimiter=' ')



	def normalizar():
		pass

    # vou usar a funcao de ativação mais tradicional e mais simples na literatura de redes neurais.
    # em tese, a funcao de ativaçao deveria fazer nenhuma ou muito pouca diferença no resultado final.
#    def activation_function(self):

#    	return = 1.0 / ( 1.0 + np.exp( -x ) )
		


if __name__ == '__main__':
	pass


