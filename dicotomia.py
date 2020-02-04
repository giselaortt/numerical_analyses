# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


import numpy as np



#é necessaria uma analise prévia que garanta:
#	a valor_pivo nos pontos inicial e final tenham sinais diferentes
#	haja apenas uma solucao no intervalo
# mais ou menos como uma busca binaria?
def dicotomia( funcao, inicio_do_intervalo, fim_do_intervalo, precisao = 0.0001 ):

	if( funcao(fim_do_intervalo) >= 0 and funcao(inicio_do_intervalo) <=0 ):
		concavidade = True

    elif( funcao(fim_do_intervalo)  <= 0 and funcao(inicio_do_intervalo) >= 0 ):
		concavidade = False

	else:
		print('Erro!')
		return


	pivo = (inicio_do_intervalo + fim_do_intervalo)/2.0
    valor_pivo = funcao(pivo)

	while( -1.0*precisao >= valor_pivo and valor_pivo >= precisao ):

		if( valor_pivo >= 0 ):
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
		valor_pivo = funcao(pivo)

	return pivo


