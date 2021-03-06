#!/usr/bin/python
# -*- coding: utf-8 -*-


#implementar todo o teste primeiro



''' teremos como foco inicial fazermos a conversão romano para decimal de 1 ao 10 e vice versa'''
''' 1- realizar o teste para ver se a conversao foi feita corretamente: pegaremos de inicio os inteiros
como I = 1 , V = 5 e X = 10 

para depois partimos para os demias...
  se for I retorna 1
  se for II reorna 2
  se dor III retorna 3
  se for IV retorna 4
  se for V retorna 5
  se for VI retorna 6
  se for VII retorna 7
  se for VIII retorna 8
  se for IX retorna 9
  se for X retorna 10
'''

'''2 - realizar o teste para verificar se o numero romano e valido'''

''' realizar teste para fazer a conversao de decimal para romano esta correta'''

import unittest

from conversorRomano import Conversor

class TesteClass(unittest.TestCase):

    ''' realizar os sempre efine os valores do objeto'''
    def setUp(self):
        self.c = Conversor()

    def teste_objeto(self):
        ''' testa se existe o objeto c '''
        self.assertTrue(self.c)

    def testa_conversao_romano_I (self):
        ''' testa se o resultado I = 1 '''
        self.assertEqual(self.c.conversorRomanoDecimal('I'),1)

    def testa_romano_V(self):
        '''testa conversão do V '''
        self.assertEqual(self.c.conversorRomanoDecimal('V'),5)
        
    def testa_conversao_romano_IV (self):
        ''' verifica algorismo romano com dois digitos e testa se IV = 4 '''
        self.assertEqual(self.c.conversorRomanoDecimal('IV'),4)

    def testar_conversao_romano_VI (self):
        ''' verifica a conversao'''
        self.assertEqual(self.c.conversorRomanoDecimal('VI'), 6)
        
    def testar_entrada(self):
        ''' testa entrada valida '''
        self.assertTrue(self.c.conversorRomanoDecimal('A,B,C,D,E,F,G'), msg='entrada invalida')
        

#    def teste_valor_invalido(self):
#        ''' verifica se a entrada e valida não permite entrar valores invalidos
#        que não contem no Algorismo romano '''
#        self.assertNotEqual(self.c.conversorRomanoDecimal('A','B','C','D'),'invalido')
#
#    def teste_valor_numerico(self):
#        ''' verifica se a entrada e valida não permite entrar valores numericos '''
#        self.assertEqual(self.c.conversorRomanoDecimal('1','2','3','4','5','6'),'invalido')




# executa teste
if __name__ == '__main__':
    unittest.main()



    

      

