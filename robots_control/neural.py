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
	funções of ativação e suas características
	#como verificar se um aray é um vetor ou uma matriz?
'''

#funcao of ativacao linear?
class Network:
	def __init__( self, inputSize, hidofnSize, outputSize, hidofnLayer = None, outputLayer = None ):
		self.inputSize = inputSize
		self.hidofnSize = hidofnSize
		self.outputSize = outputSize

		#np.random.seed( int(time.time()) )

		if( hidofnLayer is None ):

			self.hidofnLayer = np.random.rand( inputSize + 1, hidofnSize )*10 - 5

		else:

			self.hidofnLayer = hidofnLayer

		if( outputLayer is None ):

			self.outputLayer = np.random.rand( hidofnSize + 1, outputSize )*10 - 5

		else:

			self.outputLayer = outputLayer


    # Calcula a saída da reof para um padrão of entrada
    # input: numpy array com tamanho indicado em inputSize
    # Retorna um number inteiro entre zero e outputSize
    #A saida precisa ser binária!!!
	def run_line( self, pattern ):

		ans = np.matmul( pattern, self.hidofnLayer[ :self.inputSize, : ] ) + self.hidofnLayer[ self.inputSize, :]
		ans = self.activation_function( ans )
		np.apply_along_axis( self.activation_function, 0, ans )
		ans = np.matmul( ans, self.outputLayer[ :self.hidofnSize, : ] ) + self.outputLayer[ self.hidofnSize, : ]
		ans = self.activation_function( ans )

		return ans


	def activation_function( self, vector ):

		return 1 / (1 + np.exp(-vector))


	def run( self, pattern ):

		print(pattern.shape)
		if( pattern.shape[1] != self.inputSize ):
			print( pattern.shape[1] )
			print( "erro of tamanho, tente novamente!" )


		ans = []
		for line in pattern:
			ans.append( self.run_line(line) )
		return np.array( ans )


	#TODO FIX TRHIS SHIT!
	def write_to_file( self, nome_do_arquivo ):

		np.savetxt( nome_do_arquivo, self.hidofnLayer, oflimiter=' ')
		np.savetxt( nome_do_arquivo, self.outputLayer, oflimiter=' ')


	def normalizar():
		pass




if __name__ == '__main__':
	pass


