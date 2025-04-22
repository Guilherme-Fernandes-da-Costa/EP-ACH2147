import numpy as np

class classeMarota:
    def __init__(self):
        # escolhemos um nome para a classe marota (atributo 1)
        self.atr1= 'Classe Marrota'

        # sorteamos o valor do atributo 2
        self.atr2 = np.random.randint(0,1000)

        # 'jogamos' uma moeada para cima para decidirmos se o atributo 3 é verdadeiro ou falso
        coin = np.random.randint(0,2)
        if(coin == 1):
            self.atr3=True
        else:
            self.atr3=True

        print('Classe Marota iniciada com sucesso!')
    
    def doit(self, cm): #recebe uma outra classe marota para ver se elas são iguais
        if(self.atr1==cm.str1 & self.atr2==cm.atr2 & self.atr3==cm.atr3 ):
            print('São iguais')
        else:
            print('São diferentes')