from claseNodo import Nodo

class ArbolBinario:
    __raiz = None
    
    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self,SubArbol,clave):
        if self.__raiz == None:
            nodo = Nodo(clave)
            self.__raiz = nodo
        else:
            if clave > SubArbol.getClave():
                if SubArbol.getSigDerecho() == None:
                    nodo = Nodo(clave)
                    SubArbol.setSigDerecho(nodo)
                else:
                    self.insertar(SubArbol.getSigDerecho(),clave)            
            elif clave < SubArbol.getClave():
                if SubArbol.getSigIzquierdo() == None:
                    nodo = Nodo(clave)
                    SubArbol.setSigIzquierdo(nodo)
                else:
                    self.insertar(SubArbol.getSigIzquierdo(),clave)
            else:
                print('ERROR: Elemento ya existente!')
    
    def buscar(self, SubArbol, clave):
        if SubArbol != None:
            if clave == SubArbol.getClave():
                return SubArbol
            elif clave > SubArbol.getClave():
                nodo = self.buscar(SubArbol.getSigDerecho(),clave)
            else:
                nodo = self.buscar(SubArbol.getSigIzquierdo(), clave)
        else:
            print('Elmento no encontrado!')
            return None
        return nodo
    
    def getInfimo(self, raiz):
        subarbol = raiz
        if raiz.getSigDerecho() != None:
            subarbol = raiz.getSigDerecho()
            self.getInfimo(raiz.getSigDerecho())
        return subarbol
    
    def getPadre(self, subArbol,  elemento, ant):
        if subArbol != None:
            if subArbol.getClave() == elemento:
                return ant

            elif subArbol.getClave() > elemento:
                nodo = self.getPadre(subArbol.getSigIzquierdo(), elemento, subArbol)
            else:
                nodo = self.getPadre(subArbol.getSigDerecho(), elemento, subArbol)
        else:
            print('ERROR: Elemento no encontrado!')
        return nodo
    
    def Padre(self, clave_hijo, clave_padre):
        padre = self.buscar(self.__raiz,clave_padre)
        hijo = self.buscar(self.__raiz,clave_hijo)
        if padre != None and hijo != None:
            if padre.getSigIzquierdo().getClave() == clave_hijo or padre.getSigDerecho() == clave_hijo:
                return True
            else:
                return False
        else:
            print('Nodo padre o hijo no encontrado!') 
    
    def Hijo(self, clave_hijo, clave_padre):
        padre = self.buscar(self.__raiz,clave_padre)
        hijo = self.buscar(self.__raiz,clave_hijo)
        if padre != None and hijo != None:
            if padre.getSigIzquierdo().getClave() == clave_hijo or padre.getSigDerecho() == clave_hijo:
                return True
            else:
                return False
        else:
            print('Nodo padre o hijo no encontrado!') 
    
    def Altura(self, subArbol, altura = -1):
        if self.__raiz == None:
            print('ERROR: Arbol vacio')
            return 0
        else:
            if subArbol != None:
                nivel = self.Nivel(self.__raiz, subArbol.getClave())
                if altura < nivel:
                    altura = nivel
                altura = self.Altura(subArbol.getSigIzquierdo(),altura)
                altura = self.Altura(subArbol.getSigDerecho(),altura)
        return altura

    def Nivel(self,subArbol, clave, nivel = 0):
        if subArbol != None:
            if subArbol.getClave() == clave:
                return nivel
            elif subArbol.getClave() > clave:
                nivel+=1
                return self.Nivel(subArbol.getSigIzquierdo(), clave, nivel)
            else:
                nivel+=1
                return self.Nivel(subArbol.getSigDerecho(), clave, nivel)
        else:
            print('ERROR: Elemento no encontrado!!')


    def Hoja(self, clave):
        subArbol = self.buscar(self.__raiz,clave)
        if subArbol != None:
            if subArbol.getSigDerecho() == None and subArbol.getSigIzquierdo() == None:
                return True
            else:
                return False
        else:
            return None
    


    def suprimir(self, subArbol , clave):
        nodo = self.buscar(subArbol,clave)
        padre = self.getPadre(subArbol, clave, None)
        if nodo != None:
                if nodo.getSigIzquierdo() == None and nodo.getSigDerecho() == None:#Caso 1: El nodo es de grado 0
                    if padre == None:
                        self.__raiz = None
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(None)
                        else:
                            padre.setSigDerecho(None)
                elif nodo.getSigIzquierdo() != None and nodo.getSigDerecho() == None: #Caso 2: el nodo es de grado 1 
                    if padre == None:
                        if self.__raiz.getClave() > clave:
                            self.__raiz = self.__raiz.getSigDerecho()
                        else:
                      
                            self.__raiz = self.__raiz.getSigIzquierdo()
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(nodo.getSigIzquierdo())
                        else:
                            padre.setSigDerecho(nodo.getSigIzquierdo())
                   
                elif nodo.getSigIzquierdo() == None and nodo.getSigDerecho() != None:
                    if padre == None:
                        if self.__raiz.getClave() > clave:
                              self.__raiz = self.__raiz.getSigIzquierdo()
                        else:
                            self.__raiz = self.__raiz.getSigDerecho()
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(nodo.getSigDerecho())
                        else:
                            padre.setSigDerecho(nodo.getSigDerecho())
                    
                else:#Caso 3: el nodo es de grado 2
                    maximo = self.getInfimo(nodo.getSigIzquierdo())
                    nuevaClave = maximo.getClave()
                    self.suprimir(self.__raiz, nuevaClave)
                    nodo.setClave(nuevaClave)


    def Camino(self, SubArbol , clave_origen, clave_destino, camino = None, iniciar = False):
        if not iniciar:
            nivel_origen = self.Nivel(SubArbol, clave_origen)
            nivel_destino = self.Nivel(SubArbol, clave_destino)
            nodo_origen = self.buscar(SubArbol, clave_origen)
            if nivel_origen < nivel_destino and (nivel_origen != None and nivel_destino != None):
                return self.Camino(nodo_origen, clave_origen, clave_destino,camino = [], iniciar=True)
            else:
                print('ERROR: Camino no existente desde {} a {}'. format(clave_origen,clave_destino))
        else:
                if SubArbol != None:
                    if SubArbol.getClave() == clave_destino:
                        camino.append(clave_destino)
                        return camino
                    elif SubArbol.getClave() > clave_destino:
                        camino.append(SubArbol.getClave())
                        return self.Camino(SubArbol.getSigIzquierdo(), clave_origen, clave_destino,camino,iniciar)
                    else:
                        camino.append(SubArbol.getClave())
                        return self.Camino(SubArbol.getSigDerecho(), clave_origen, clave_destino,camino,iniciar)
    
    def Frontera(self, subArbol, frontera = []):
        if subArbol != None:
            if self.Hoja(subArbol.getClave()):
                frontera.append(subArbol.getClave())
            self.Frontera(subArbol.getSigIzquierdo(),frontera)
            self.Frontera(subArbol.getSigDerecho(),frontera)
        return frontera
    
    #RECORRIDOS DEL ARBOL
    def InOrder(self,SubArbol):
        if not SubArbol == None:
            self.InOrder(SubArbol.getSigIzquierdo())
            print(SubArbol.getClave())
            self.InOrder(SubArbol.getSigDerecho())

    def preOrder(self,SubArbol):
        if not SubArbol == None:
            print(SubArbol.getClave())
            self.preOrder(SubArbol.getSigIzquierdo())
            self.preOrder(SubArbol.getSigDerecho())
    
    def postOrder(self, subArbol):
        if not subArbol == None:
            self.postOrder(subArbol.getSigIzquierdo())
            self.postOrder(subArbol.getSigDerecho())
            print(subArbol.getClave())