import random
import copy

print('bienvenido a `Abeja Polinizadora`!, en este juego usted controla a una abeja (@) debe encontrar las flores (☼) que estaran dispersas por el tablero, usted escoje las dimensiones del tablero, la cantidad de flores, y la cantidad de movimientos que posee.')
N_flores=input('seleccione la cantidad de flores que desea repartir\n')
print('la cantidad de movimiento que tendra a su disposicion estaran en relacion al tamaño del tablero\n')
alto=input('ingrese de cuantos espacion desea el largo del tablero\n')
ancho=input('ingrese de cuantos espacion desea el ancho del tablero\n')
#Se establecen los valores con los cuales se va a generar todo
try:
    N_flores=int(N_flores)
    alto=int(alto)
    ancho=int(ancho)
    #conidicion en las que, si el usuario ingresa algo que no sea un numero, no se cae el codigo
    #y se le solicita ingresar valores validos
    intentos=int((alto*ancho)*0.8)
    #los movimientos disponibles seran de 2/3 del area del tablero
    simbolos= {1:('+'), 2:('-'), 3:(' '), 4:('|')}
    #El diccionario simbolos es ocupado para la generacion del tablero
    abeja='@'
    flor='☼'
    vacio=' '
    espacio=[]
    coordenadas_flores=[]
    switch=True
    #la variable switch es ocupada para re odenar las flores segun sus posiciones
    llave=0
    #la variable llave sera ocupada para mostrar las flores en el tablero si es que se llegan a encontrar
    if N_flores>0:
    #condicion que revisa que la cantidad de flores no sea 0 o negativa
        if alto<=1 or ancho<=1:
            print('las dimensiones minimas del tablero es de una fila o una clumna')
        #limite de espacio del tablero, no puede ser de 1x1 
        while N_flores>(alto*ancho)-1:
            print('No pueden haber mas flores que el espacio disponible')
            break
        #limite en caso de querer generar mas flores de las que puede contener la matriz
        else:
            print('\n')
            print('moverse hacia:\narriba=w\nabajo=s\nderecha=d\nizquierda=a\n')
        
            for x in range(0,alto):
                linea= ((simbolos[4]+simbolos[3])*ancho+simbolos[4])
                linea=list(linea)
                espacio.append(linea)
            #aca se genera la lista espacio, con la el usuario va a interactuar
            sin_ocupar=[]        
            for x in range(len(espacio[0])):
                if x%2!=0:
                    sin_ocupar.append(x)
            #en este paso se detectan todos los espacios vacios a lo largo de una fila, los cuales pueden
            #contener flores (los valores pares son las lineas del tablero, y los impares son espacion 'vacios')
            #y se agregan a la lista 'sin ocupar'
            
            largo=len(espacio)
            ubicacion_abeja1=random.randint(0,largo-1)
            ubicacion_abeja2=random.choice(sin_ocupar)
            espacio[ubicacion_abeja1][ubicacion_abeja2]=abeja
            #aca se selecciona de manera aleatoria la posicion de la abeja a traves de la matriz y 
            #la lista 'sin ocupar'
        
            def ubicacion_abeja(espacio):
                for x in range(len(espacio)):
                    for y in range(len(espacio[x])):
                        if espacio[x][y]==abeja:
                            lugar1=x
                            lugar2=y
                            return(lugar1,lugar2)
                #esta funcion detecta de manera continua las 'coordenadas' de la abeja dentro de la matriz 
                #esta funcion es de suma importancia para los movimientos del jugador dentro del juego
            
            def generacion_tablero(espacio):  
                for x in range(len(espacio)):
                    print ((simbolos[1]+simbolos[2])*ancho+simbolos[1])
                    print(*espacio[x],sep='')
                return ((simbolos[1]+simbolos[2])*ancho+simbolos[1])
                #esta funcion genera el tablero en pantalla, la cual sera ocupada mas adelante
            
            espacio_flor=copy.deepcopy(espacio)
            #en esta linea se genera una 'deepcopy' de la lista espacio, la cual contendra a todas las
            #flores y no sera visible para el usuario.
            #ocupo la funcion deepcopy() de la libreria copy para poder separarlas y que al modificar
            #una, no cambie la otra
            
            while switch:
            #la variable switch hace que, al no cumplirse las conidiciones de este bloque, se reordenen
            #de manera continua las flores
                for x in range(N_flores):
                    ubicacion_flor1=random.randint(0,largo-1)
                    ubicacion_flor2=random.choice(sin_ocupar)
                    espacio_flor[ubicacion_flor1][ubicacion_flor2]=flor
                    #aca se selecciona de manera al azar una posicion de la lista 'espacio_flor'para insertar
                    #las flores dentro de la lista 'espacio_flor'
                    for x in range(len(espacio_flor)):
                        for y in range(len(espacio_flor[x])):
                            if espacio_flor[x][y]==flor:
                                lugar_flor=(x,y)
                                #en este bloque se detectan todas las coordendas de las flores, las
                                #cuales seran ocupadas mas adelante
                                if lugar_flor not in coordenadas_flores:
                                    coordenadas_flores.append(lugar_flor)
                                    #con este 'if' solo se agregan las coordendas que son distintas entre
                                    #si, y el largo de esta lista sera ocupado para la variable switch
                if ubicacion_abeja(espacio) in coordenadas_flores:
                    espacio_flor.clear()
                    espacio_flor=copy.deepcopy(espacio)
                    coordenadas_flores.clear()
                    switch=True
                    #este bloque 'if' verifica que las flores esten en distintas coordendas a la abeja,
                    #si esa condicion no se cumple, se resetean todas las listas moidificadas, se realiza
                    #de nuevo la 'deepcopy' y se repite todo desde 'while switch'
                else:
                    if len(coordenadas_flores)!=N_flores:
                        switch=True
                        #estas 2 lineas detectan que las flores esten en distintas coordenadas, y esto
                        #fue limitado con anterioridad, si existian coordenadas iguales no se agregan
                        #a la lista 'coordendas_flores' y, por ende, el largo de esta lista es menor
                        #al numero de flores que deberian de estar repartidas
                    else:
                        switch=False
                        #si no se cumplen ninguna de las condiciones anteriores (es decir, todas las
                        #flores estan dispersadas de manera correcta), se continua a el juego
                                
            bucle=0
            #la variable 'bucle' determina el intento actual del jugador, y se ocupara para limitar
            #los movimientos de este
        
            while bucle<intentos:
                if intentos-bucle>1:
                    print('le quedan',intentos-bucle,'movimientos')
                if intentos-bucle==1:
                    print('le queda 1 movimiento')
                ubicacion_abeja1=ubicacion_abeja(espacio)[0]
                ubicacion_abeja2=ubicacion_abeja(espacio)[1]
                #ubicacion_abeja1 detecta la posicion vertical de la abeja en la matriz
                #ubicacion_abeja2 detecta la posicion horizontal de la abeja en la matriz
                arriba=1
                abajo=1
                izquierda=2
                derecha=2
                #estas variables dictan los movimientos de la abeja dentro de la matriz
                print(generacion_tablero(espacio))
                #aca se imprime el tablero con la funcion creada anteriormente
                movimiento=(input('ingrese un movimiento\n'))
                #la variable 'movimiento' determina la direccion de la abeja, si no se ingresa alguna
                #de las opciones explicada en las instrucciones, la abeja no se movera y no restara
                #movimientos
                
                if movimiento=='w':
                    if abeja not in espacio[0]:
                        #esta condicion detecta y la abeja no esta en el limite superior, si no se 
                        #cumple, la abeja se mueve
                        coordenadas=ubicacion_abeja(espacio)[0]
                        #la variable coordenada determina el movimiento vertical(el punto original de este)
                        espacio[coordenadas-arriba][ubicacion_abeja2]=abeja
                        #si se decide subir, pasa a una lista menor que la original, pero se mantiene
                        #la posicion horizontal
                        espacio[coordenadas][ubicacion_abeja2]=vacio
                        #al moverse, se deja la coordenada original como un espacio vacio
        
                        bucle=bucle+1
                        #la cuenta bucle aumenta, lo cual limita el numero de los futuros movimientos
                    else:
                        movimiento=input('no puede salirse de los limites del mapa,ingrese otro movimiento\nescriba cualquier numero para continuar\n')
                        #si el movimiento ingresado no es valido (saca al usuario del tablero), se le 
                        #notifica y se le pide ingresar cualquier numero para poder seguir
                        
                if movimiento=='s':
                    if abeja not in espacio[-1]:
                        #si la abeja no esta en la ultima fila, se ingresa el movimiento
                        coordenadas=ubicacion_abeja(espacio)[0]
                        #la variable coordenadas determina el movimiento horizontal (desde donde se origina)
                        espacio[coordenadas+abajo][ubicacion_abeja2]=abeja
                        #si se decide bajar, pasa a una lista mayor que la original, pero se mantiene
                        #la posicion horizontal
                        espacio[coordenadas][ubicacion_abeja2]=vacio
                        #al moverse, se deja la coordenada original como un espacio vacio
        
                        bucle=bucle+1
                        #la cuenta bucle aumenta, lo cual limita el numero de los futuros movimientos
                    else:
                        movimiento=input('no puede salirse de los limites del mapa,ingrese otro movimiento\nescriba cualquier numero para continuar\n')
                        #esta linea cumple la misma que la mencionada en el bloque anterior 
                if movimiento=='a':
                    u_altura=ubicacion_abeja(espacio)[0]
                    #la variable u_altura se adapta a la fila en la que se ubica la abeja, y esto se 
                    #ocupara para limitar los movimientos
                    if abeja not in espacio[u_altura][1]:
                        #si la abeja no se ubica en la parte mas izquierda del tablero, se ejecuta 
                        #este bloque
                        coordenadas=ubicacion_abeja(espacio)[1]
                        #se detecta la posicion horizontal de la abeja
                        espacio[ubicacion_abeja1][coordenadas-izquierda]=abeja
                        #si se decide moverce hacia la izquierda, se mueve en la misma lista, pero
                        #se mantiene la posicion vertical
                        espacio[ubicacion_abeja1][coordenadas]=vacio
                        #al moverse, deja la posicion original como un espacio vacio
        
                        bucle=bucle+1
                        #la cuenta bucle aumenta, lo cual limita el movimiento de los futuros movimientos
                    else:
                        movimiento=input('no puede salirse de los limites del mapa,ingrese otro movimiento\nescriba cualquier numero para continuar\n')
                        #se le pide al usuario otro movimiento si es que esta al limite izquierdo del
                        #mapa
                if movimiento=='d':
                    u_altura=ubicacion_abeja(espacio)[0]
                    #la variable u_altura se adapta a la fila en la que se ubica la abeja, y esto se 
                    #ocupara para limitar los movimientos
                    if abeja not in espacio[u_altura][-2]:
                        #si la abeja no se ubica en la parte mas derecha del tablero, se ejecuta 
                        #este bloque
                        coordenadas=ubicacion_abeja(espacio)[1]
                        #se detecta la posicion horizontal de la abeja
                        espacio[ubicacion_abeja1][coordenadas+derecha]=abeja
                        #si se decide moverce hacia la derecha, se mueve en la misma lista, pero
                        #se mantiene la posicion vertical
                        espacio[ubicacion_abeja1][coordenadas]=vacio
                        #al moverse, deja la posicion original como un espacio vacio
                        bucle=bucle+1
                        #la cuenta bucle aumenta, lo cual limita el movimiento de los futuros movimientos
                    else:
                        movimiento=input('no puede salirse de los limites del mapa,ingrese otro movimiento\nescriba cualquier numero para continuar\n')
                        #se le pide al usuario otro movimiento si es que esta al limite derecho del
                        #mapa
                if llave==1:
                    espacio[ubicacion_abeja1][ubicacion_abeja2]=flor
                    #la variable llave solo se modifica en el siguente bloque y se igula a 1, esto quiere
                    #decir que el usuario pasó por una flor, pero no puedo modificar el caracter en el
                    #mismo bloque ya que la abeja no tendria coordendas, por ello al siguente bucle
                    #se cambia el bloque que ocupo la abeja si es que paso arriba de una flor
                    llave=0
                    #llave se iguala a 0 para que solo se repita si se cumple el siguente bloque
                    
                if ubicacion_abeja(espacio) in coordenadas_flores:
                    #se compara la coordenada de la abeja con la de las flores, y si existe alguna
                    #igual, se ejecuta este bloque
                    coordenadas_flores.remove(ubicacion_abeja(espacio))
                    #se elimina la coordenada de dicha flor de la lista 'coordenadas_flores', lo que
                    #quiere decir que fue encontrada por el usuario
                    print('encontraste una flor, quedan ',len(coordenadas_flores))
                    #se imprime el mensaje de haber encontrado una flor
                    llave=1
                    #llave se iguala a 1 para ejecutar el bloque anterior al siguente movimiento
                       
                if len(coordenadas_flores)==0:
                    print('------------------------------------------')
                    print('------------------GANASTE-----------------')
                    print('------------------------------------------')
                    #en caso de que el largo de la lista 'coordenadas_flores' sea 0, significa que el
                    #usuario encontro todas las flores, por lo que se imprime el mensaje de victoria
                    #y se termina el programa
                    break
            
            if bucle==intentos and len(coordenadas_flores)>0:
                print('------------------------------------------')
                print('------------------PERDISTE----------------')
                print('------------------------------------------')
                if len(coordenadas_flores)>1:
                    print('quedaron',len(coordenadas_flores),'flores sin encontrar')
                if len(coordenadas_flores)==1:
                    print('quedo una flor sin encontrar')
                #si el bucle es igual a el valor de intentos y el largo de flores es mayor a 0, significa
                #que el usuario no pudo encontrar todas las flores, y se desplega el mensaje de
                #derrota
    else:
        print('no puede jugar con ninguna flor, ingrese otra cantidad que sea mayor a 0')
except:
    print('los valores ingresados no son validos, solo se pueden ingresar numeros, intentelo nuevamente')