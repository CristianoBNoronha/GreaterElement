
def maior_elemento(lista):
    lista2 = lista[:]
    lista3 = []
    x = 0
    n = 0
    x = lista2[0]
    c = len(lista) - 1
    for x in lista:
        for n in lista2[1:]:
            if n > x and len(lista2) > 1:
                    del lista2[0]
                    x = lista2[0]
            while x > n and len(lista2) > 1:
                if n > x and len(lista2) > 1:
                    del lista2[0]
                    x = lista2[0]
                if x > n and len(lista2) > 1:
                    lista2.append(x)
                    del lista2[0]
                    x = lista2[0]
        x = lista2[0]
    return x
            
            
                
                    
                    
    
                    
                
