from claseArbolBinario import ArbolBinario

if __name__ == '__main__':
    objArbol = ArbolBinario()
    objArbol.insertar(objArbol.getRaiz(),50)
    objArbol.insertar(objArbol.getRaiz(), 45)
    objArbol.insertar(objArbol.getRaiz(), 70)
    objArbol.insertar(objArbol.getRaiz(),80)
    objArbol.insertar(objArbol.getRaiz(), 55)
    frontera = objArbol.Frontera(objArbol.getRaiz())
    print('Frontera del arbol:')
    for nodo in frontera:
        print(nodo)
