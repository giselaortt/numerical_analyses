# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


import numpy as np


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


