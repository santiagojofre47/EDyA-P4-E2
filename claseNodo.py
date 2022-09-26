class Nodo:
    __clave = None
    __sigIzq = None
    __sigDer = None
    
    def __init__(self, clave):
        self.__clave = clave
        self.__sigIzq = None
        self.__sigDer = None
    
    def setSigIzquierdo(self, sig):
        self.__sigIzq = sig
    
    def setSigDerecho(self, sig):
        self.__sigDer = sig
    
    def setClave(self, clave):
        self.__clave = clave
    
    def getClave(self):
        return self.__clave
    
    def getSigIzquierdo(self):
        return self.__sigIzq
    
    def getSigDerecho(self):
        return self.__sigDer
    
    