from ForTwo.r2.local import Local

class Terminal(Local):
    def __init__(self):
        pessoas = [
                        'piloto', 'oficial1', 'oficial2'
                        ,'chefe de serviço', 'comissário1', 'comissário2'
                        ,'policial', 'presidiario'
                    ]

        super().__init__(self.__pessoas)

    def valida_saida(self, pessoa:str):
        if pessoa == 'policial' and 'presidiario' in self.__pessoas and self.__pessoas: 
            return False
