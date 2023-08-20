import random
lista1=[' ',' ','□','--','-','-','□']
lista2=[' ',' ','|','  ',' ','  ','|']
lista3=[' ',' ','O','  ',' ','  ','|']
lista4=[' ','/','|','\ ',' ','🔥','🔥','🔥']
lista5=[' ',' ','|',]
lista6=[' ','/',' ','\ ']
tablero=[lista1,lista2,lista3,lista4,lista5,lista6]
palabras=['ChatGPT', 'JavaScript', 'VSCode', 'Discord', 'Universidad', 'GitHub', 'Minecraft', 'Anaconda'
          ,'Windows', 'Linux', 'Macintosh', 'Nintendo', 'Oculus', 'Nvidia', 'Intel', 'GigaByte','Steam'
          ,'Valorant', 'Sony', 'HyperX', 'Razer', 'Informatica', 'Consigna', 'Minima', 'Python', 'Spyder',
          'Ahorcado', 'Examen', 'IPhone', 'Samsung', 'Desarrollo', 'Programacion', 'Microsoft',
          'Decimas', 'Instagram', 'Facebook', 'Twitter', 'Netflix', 'Blockbuster', 'Ciberseguridad',
          'Waze', 'Google', 'Opera', 'FireFox', 'Bios', 'Procesador', 'Mouse', 'Monitor', 'Gabinete',
          'Teclado']
#definicion de variables para iniciar el juego

def palabra(lista_palabras):
    x=random.choice(lista_palabras)
    return x
#funcion seleccion de la palabra

def impresion_tablero(tablero):
    for x in tablero:
        impresion=''.join(x)
        print(impresion)
        #funcion impresion del tablero

def existeletra(letra,palabra):
    mayus=letra.upper()
    minus=letra.lower()
    if mayus in palabra or minus in palabra:
        return True
    else:
        return False
    #funcion de comprobación en caso de ingresar una letra presente en la palabra, se verifica su la letra
    #en mayuscula o minuscula se encuentra en la palabra, y si es asi se retorna True

def ganar(lista_v,lista):
    if lista_v==lista:
        return True
    else:
        return False
    #funcion encargada de corroborar si acerto la palabra

def tresintentos(palabra,lista):
    verificar=[]
    for x in range(len(palabra)):
        mayus=palabra[x].upper()
        minus=palabra[x].lower()
        if mayus in lista or minus in lista:
            verificar.append(palabra[x])
    if len(verificar)==len(lista):
        return True
    else:
        return False
    #funcion encargada de verificar los tres intentos para ingresar una palabra, se verifica cada letra,
    #si esta en la palabra se agrea a la lista verificar y si el largo de esta lista el el mismo que el de
    #la palabra, se retorna True
    
def pantalla(lista_v,espacios):
    print(*lista_v)
    print(*espacios)
    #funcion que imprime las palabras acertadas y los espacios disponibles

lista=list(palabra(palabras))
espacios=['¯']*len(lista)
lista_vacia=[' ']*len(lista)
#definicion de listas claves para el juego

y=0

while y<5:
    #bucle para los fallos de 5 letras
    impresion_tablero(tablero)
    ubicacion1=[]
    ubicacion2=[]
    pantalla(lista_vacia,espacios)
    letra=input(f'ingrese una letra, puede fallar {5-y} veces mas\n')
    veredicto=existeletra(letra, lista)
    #comprocacion en caso de acertar una letra
    if veredicto:
        for x in range(len(lista)):
            Mayus=letra.upper()
            minus=letra.lower()
            if lista[x]==Mayus:
                ubicacion1.append(x)
            if lista[x]==minus:
                ubicacion2.append(x)
        for x in ubicacion1:
            lista_vacia[x]=Mayus
        for x in ubicacion2:
            lista_vacia[x]=minus
            #compropacion de la ubicacion de la letra, y se ocupa el lower y upper para poder recibir
            #ambas opciones, además, las palabras disponibles presentan mayusculas y minusculas (para
            #que se puedan entender mejor)
    else:
        if len(letra)!=1:
            print('ingrese solamente una letra')
            #caso de que el usuario intente ingresar una frase
        else:
            if y==0:
                lista3[6]='🔥'
            if y==1:
                lista2[6]='🔥'
            if y==2:
                lista1[5]='🔥'
            if y==3:
                lista1[4]='🔥'
            if y==4:
                lista1[3]='🔥'
            y+=1  
            #caso de fallar una letra. Se le agrega un error y el fuego avanza por el dibujo que
            #representa el numero de fallos
    
    final=ganar(lista_vacia,lista)
    #la variable final se designa segun la funcion ganar
    if final:
        #si final es True, se ejecuta el siguente bloque
        for x in range(len(lista)):
            Mayus=letra.upper()
            minus=letra.lower()
            if lista[x]==Mayus:
                ubicacion1.append(x)
            if lista[x]==minus:
                ubicacion2.append(x)
        for x in ubicacion1:
            lista_vacia[x]=Mayus
        for x in ubicacion2:
            lista_vacia[x]=minus
        pantalla(lista_vacia,espacios)
        y=5
        #se agrega la letra faltante a la lista llamda lista_vacia y la variable 'y' se fija a 5 para
        #poder salir del bucle
        
if ganar(lista_vacia,lista):
    print('Ganaste!')
    #se comprueba si se salio del bucle por fallar las  cinco veces o por si se acerto la palabra

else:
    y=0
    #se fija la variable 'y' a 0 para poder ingresar a un nuevo bucle
    while y<3:
        impresion_tablero(tablero)
        pantalla(lista_vacia,espacios)
        ultima_oportunidad=input(f'ya fallaste 5 veces, intente ingresar la palabra completa para ganar (tiene {3-y} intentos)\n')
        if tresintentos(ultima_oportunidad,lista):
            print('Ganaste!')
            y=3
            final=1
            #si tresintentos es True, se imprime el mensaje de victoria, la variable 'y' se fija a 3
            #para salir del bucle y la variable final se iguala a 1 para no arrojar los mensajes de 
            #derrota
        else:
            if len(ultima_oportunidad)==1:
                print('ingrese solamente palabras')
                #mensaje que aparece en caso de que el usuario ingrese una letra en vez de una palabra
            if len(ultima_oportunidad)!=1 and final!=1 and y<3:
                y+=1
                #se comprueba las variables ya definidas y, en caso de fallar, se agrega un error a la cuenta
            if final!=1 and y==3:
                lista2[2]=lista3[2]=lista4[1]=lista4[2]=lista4[3]=lista5[2]=lista6[1]=lista6[3]='🔥'
                impresion_tablero(tablero)
                x=''.join(lista)
                print('perdiste, la palabra era',x)
                #si se alcanzan los 3 errores, la figura se quema por completo y se imprime el mensaje
                #de derrota, junto a la palabra que habia sido previamente seleccionada que debia ser
                #adivinada