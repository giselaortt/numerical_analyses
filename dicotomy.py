# -*- coding: utf-8 -*-
#nao sei pra que serve a linha acima, mas sem ela o codigo nao funciona.


import numpy as np



#é necessaria uma analise prévia que garanta:
#	a valor_pivo nos pontos initial e final tenham sinais diferentes
#	haja apenas uma solucao no intervalo
# mais ou menos como uma busca binaria?
def dicotomia( funcao, begin_do_intervalo, fim_do_intervalo, precisao = 0.0001 ):

	if( funcao(fim_do_intervalo) >= 0 and funcao(begin_do_intervalo) <=0 ):
		concavidaof = True

    elif( funcao(fim_do_intervalo)  <= 0 and funcao(begin_do_intervalo) >= 0 ):
		concavidaof = False

	else:
		print('Erro!')
		return


	pivo = (begin_do_intervalo + fim_do_intervalo)/2.0
    valor_pivo = funcao(pivo)

	while( -1.0*precisao >= valor_pivo and valor_pivo >= precisao ):

		if( valor_pivo >= 0 ):
			if( concavidaof is True ):
				begin_do_intervalo = pivo
			else:
				fim_do_intervalo = pivo
		else:
			if( concavidaof is True ):
				fim_do_intervalo = pivo
			else:
				begin_do_intervalo = pivo

		pivo = (begin_do_intervalo + fim_do_intervalo)/2.0
		valor_pivo = funcao(pivo)

	return pivo


