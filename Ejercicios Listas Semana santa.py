import random
print('1: valores aleatorios del 1 al 10 al cuadrado y al cubo')
print('2: cadena de 5 elementos')
print('3: promedio de notas, nota mas alta y baja')
print('4: introducir numeros hasta un negativo')
print('5: orden de 10 numeros aleatorios')
print('6: dias del mes')
print('7: suma de 2 listas')
print('8: edades de alumnos')
print('9: temperayutas de 5 dias')
print('10: suma de una tabla en columnas y filas')
print('11: diagonal')
print('12: marco')
print('13: conductores y kms recorridos')
print('14: tiendas')
print('15: Torneo de tútbal')
print('16: manipular una lista')
print('17: introducir numeros hasta un negativo,se eliminan los repetidos ')
print('18: manipular cadenas')
NP=int(input('ingrese el numero de pregunta que desea revisar = '))

##############################################
if NP==1:
    x=0
    valores=[]
    while x<10:
        azar=random.randint(1,10)
        valores.append(azar)
        x=x+1
        cuadrado=azar**2
        cubo=azar**3
        print (azar,'al cuadrado es = ',cuadrado, 'y al cubo es = ',cubo)
##############################################
if NP==2:
    x=0
    lista=[]
    while x<5:
        v_ingresado=input('ingrese algo a agregar en una lista = ')
        lista.append(v_ingresado)
        x=x+1
    
    lista.reverse()
    print('los caracteres ingresados al revés son : ',lista)
##############################################
if NP==3:
    notas= []
    x=0
    while(x<5):
        nota=float(input('ingrese la nota ='))
       
        if(1.0<=nota<=7.0):
            notas.append(nota)
            x=x+1
            notas.sort()
            suma=sum(notas)
            promedio=suma/5
            if x==5:
                nota_baja=notas[0]
                nota_alta=notas[4]
                print('promedio = ',promedio,'\nnota mas alta = ', nota_alta, '\nnota mas baja = ',nota_baja)
       
        else:
            print('el valor ingresado no es valido')
##############################################
if NP==4:
    valores=[]
    
    while True:
        valor=input('ingrese valor = ')
        if(valor.isdigit()):
            valores.append(valor)
        else:
            print(valores)
            break
##############################################
if NP==5:
    numeros=[]
    for x in range (1,10):
        y=random.randint(1,100)
        numeros.append(y)
        numeros.sort()
    print(numeros)
##############################################
if NP==6:
    mes= int(input('ingrese el numero del mes'))
    
    if(1<=mes<=12):
        meses= {1:('Enero'),2:('Febrero'),3:('Marzo'),4:('Abril'),5:('Mayo'),6:('Junio'),7:('Julio'),8:('Agosto'),9:('Septiembre'),10:('Ocrubre'),11:('Nobiembre'),12:('Diciembre')}
        dias_meses={1:('31'),2:('28'),3:('31'),4:('30'),5:('31'),6:('30'),7:('31'),8:('31'),9:('30'),10:('31'),11:('30'),12:('31')}
        print(meses[mes], 'tiene',dias_meses[mes], 'dias')
    
    else:
        print('Ingrese un numero entre 1 y 12, no existe el mes numero',mes)
##############################################
if NP==7:
    lista1=[]
    lista2=[]
    lista3=[]
    ciclo=0
    
    for x in range (1,6):
        n1=int(input('ingrese valores para la lista 1 : '))
        lista1.append(n1)
    
    for y in range (1,6):
        n2=int(input('ingrese valores para la lista 2 : '))
        lista2.append(n2)
    
    while ciclo<5:
        n3= lista1[ciclo]+lista2[ciclo]
        lista3.append(n3)
        ciclo=ciclo+1
    
    print('La suma de ambas lista crea la siguiente lista: ',lista3)
##############################################
if NP==8:
    nombres=[]
    edades=[]
    mayores_e=[]
    mayores_n=[]
    bucle=0
    
    while True:
        alumno_n=input('ingrese el nombre del alumno : ')
        if alumno_n!='*':
            nombres.append(alumno_n)
            alumno_e=int(input('ingrese la edad de dicho alumno : '))
            edades.append(alumno_e)
            
        else:
            total=int(len(edades))
            
            while (bucle<total):
                if edades[bucle]>=18:
                    mayores_n.append(nombres[bucle])
                    mayores_e.append(edades[bucle])
                bucle=bucle+1
                mayores_n.sort()
            print ('Mayores de edad (más joven a más viejo): ',mayores_n)
            break
##############################################
if NP==9:
    t_max=[]
    t_min=[]
    t_prom=[]
    dias=[]
    repeticion=1
    
    while repeticion<6:
        print('dia',repeticion)
        dias.append(repeticion)
        t_ma=float(input('Ingrese la temperatura maxima del dia'))
        t_max.append(t_ma)
        t_mi=float(input('Ingrese la temperatura minima del dia'))
        t_min.append(t_mi)
        t_pro=(t_ma+t_mi)/2
        t_prom.append(t_pro)
        repeticion=repeticion+1
    
    repeticion=0
    
    print ('informacion:\n')
    
    while repeticion<5:
        print('temperatura promedio dia',repeticion+1,':',t_prom[repeticion])
        repeticion=repeticion+1
    
    print('dia con menor temperatura:',dias[t_prom.index(min(t_prom))])

##############################################
if NP==10:
    fila1=[]
    fila2=[]
    fila3=[]
    fila4=[]
    fila5=[]
    
    for x in range (1,6):
        numero1=int(input('ingrese un valor para agregar a la lista 1 = '))
        fila1.append(numero1)
    
    for x in range (1,6):
        numero2=int(input('ingrese un valor para agregar a la lista 2 = '))
        fila2.append(numero2)
    
    for x in range (1,6):
        numero3=int(input('ingrese un valor para agregar a la lista 3 = '))
        fila3.append(numero3)
    
    for x in range (1,6):
        numero4=int(input('ingrese un valor para agregar a la lista 4 = '))
        fila4.append(numero4)
    
    for x in range (1,6):
        numero5=int(input('ingrese un valor para agregar a la lista 5 = '))
        fila5.append(numero5)
        
    print(fila1,sum(fila1))
    print(fila2,sum(fila2))
    print(fila3,sum(fila3))
    print(fila4,sum(fila4))
    print(fila5,sum(fila5))
    print((fila1[0]+fila2[0]+fila3[0]+fila4[0]+fila5[0]),(fila1[1]+fila2[1]+fila3[1]+fila4[1]+fila5[1]),
          (fila1[2]+fila2[2]+fila3[2]+fila4[2]+fila5[2]),(fila1[3]+fila2[3]+fila3[3]+fila4[3]+fila5[3]),
          (fila1[4]+fila2[4]+fila3[4]+fila4[4]+fila5[4]))

##############################################
if NP==11:
    filaD1=[1,0,0,0,1]
    filaD2=[0,1,0,1,0]
    filaD3=[0,0,1,0,0]
    filaD4=[0,1,0,1,0]
    filaD5=[1,0,0,0,1]
        
    print(filaD1)
    print(filaD2)
    print(filaD3)
    print(filaD4)
    print(filaD5)

##############################################
if NP==12:
    valor0={0:'0'}
    valor1={0:'1'}
    
    print(valor1[0]*15)
    print(valor1[0]+valor0[0]*13+valor1[0])
    print(valor1[0]+valor0[0]*13+valor1[0])
    print(valor1[0]+valor0[0]*13+valor1[0])
    print(valor1[0]*15)

##############################################
if NP==13:
    conductor=[]
    kms_txC=[]
    kms=[]
    rep1=1
    rep2=1
    impresion=0
    
    while rep1==1:
        nombre=input('ingrese el nombre del conductor = ')
        conductor.append(nombre)
        rep1=0
        rep2=1
        while rep2==1:
            recorrido=float(input('ingrese los ksm recorridos = '))
            kms.append(recorrido)
            rep2=int(input('desea agregar mas kms recorridos? 1=si    0=no\n'))
        
        kms_txC.append(sum(kms))
        kms.clear()
        rep1=int(input('desea agregar otro conductor? 1=si    0=no\n'))
        
    while impresion<len(conductor):
        print('conductor = ',conductor[impresion],',kilometros recorridos = ',kms_txC[impresion])
        impresion=impresion+1

##############################################
if NP==14:
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    p=[]
    ganancia=[]
    
    precio1=int(input('ingrese el precio del articulo 1 = '))
    p.append(precio1)
    precio2=int(input('ingrese el precio del articulo 2 = '))
    p.append(precio2)
    precio3=int(input('ingrese el precio del articulo 3 = '))
    p.append(precio3)
    precio4=int(input('ingrese el precio del articulo 4 = '))
    p.append(precio4)
    precio5=int(input('ingrese el precio del articulo 5 = '))
    p.append(precio5)
    
    print('---------------------------------------------------------')
    
    print('SUCURSAL N*1')
    
    cantidad1_1=int(input('ingrese cantidad vendida del articulo 1 = '))
    t1.append(cantidad1_1)
    cantidad2_1=int(input('ingrese cantidad vendida del articulo 2 = '))
    t1.append(cantidad1_1)
    cantidad3_1=int(input('ingrese cantidad vendida del articulo 3 = '))
    t1.append(cantidad1_1)
    cantidad4_1=int(input('ingrese cantidad vendida del articulo 4 = '))
    t1.append(cantidad1_1)
    cantidad5_1=int(input('ingrese cantidad vendida del articulo 5 = '))
    t1.append(cantidad1_1)
    print('---------------------------------------------------------')
    
    print('SUCURSAL N*2')
    
    cantidad1_2=int(input('ingrese cantidad vendida del articulo 1 = '))
    t2.append(cantidad1_2)
    cantidad2_2=int(input('ingrese cantidad vendida del articulo 2 = '))
    t2.append(cantidad2_2)
    cantidad3_2=int(input('ingrese cantidad vendida del articulo 3 = '))
    t2.append(cantidad3_2)
    cantidad4_2=int(input('ingrese cantidad vendida del articulo 4 = '))
    t2.append(cantidad4_2)
    cantidad5_2=int(input('ingrese cantidad vendida del articulo 5 = '))
    t2.append(cantidad5_2)
    
    print('---------------------------------------------------------')
    
    print('SUCURSAL N*3')
    
    cantidad1_3=int(input('ingrese cantidad vendida del articulo 1 = '))
    t3.append(cantidad1_3)
    cantidad2_3=int(input('ingrese cantidad vendida del articulo 2 = '))
    t3.append(cantidad2_3)
    cantidad3_3=int(input('ingrese cantidad vendida del articulo 3 = '))
    t3.append(cantidad3_3)
    cantidad4_3=int(input('ingrese cantidad vendida del articulo 4 = '))
    t3.append(cantidad4_3)
    cantidad5_3=int(input('ingrese cantidad vendida del articulo 5 = '))
    t3.append(cantidad5_3)
    print('---------------------------------------------------------')
    
    print('SUCURSAL N*4')
    
    cantidad1_4=int(input('ingrese cantidad vendida del articulo 1 = '))
    t4.append(cantidad1_4)
    cantidad2_4=int(input('ingrese cantidad vendida del articulo 2 = '))
    t4.append(cantidad2_4)
    cantidad3_4=int(input('ingrese cantidad vendida del articulo 3 = '))
    t4.append(cantidad3_4)
    cantidad4_4=int(input('ingrese cantidad vendida del articulo 4 = '))
    t4.append(cantidad4_4)
    cantidad5_4=int(input('ingrese cantidad vendida del articulo 5 = '))
    t4.append(cantidad5_4)
    print('---------------------------------------------------------')
    print('INFORMACIÓN')
    print('---------------------------------------------------------')
    print ('Cantidad total de articulos vendidos = ',sum(t1)+sum(t2)+sum(t3)+sum(t4))
    print('cantidad de articulso vendida en la sucursal 2 = ',sum(t2))
    print('cantidad del articulo 3 en la sucursal 1 = ',t1[2])
    print('recaudación total de cada sucursal:')
    ganancia.append(t1[0]*p[0]+t1[1]*p[1]+t1[2]*p[2]+t1[3]*p[3]+t1[4]*p[4])
    ganancia.append(t2[0]*p[0]+t2[1]*p[1]+t2[2]*p[2]+t2[3]*p[3]+t2[4]*p[4])
    ganancia.append(t3[0]*p[0]+t3[1]*p[1]+t3[2]*p[2]+t3[3]*p[3]+t3[4]*p[4])
    ganancia.append(t4[0]*p[0]+t4[1]*p[1]+t4[2]*p[2]+t4[3]*p[3]+t4[4]*p[4])
    print('sucursal 1= ',ganancia[0])
    print('sucursal 2= ',ganancia[1])
    print('sucursal 3= ',ganancia[2])
    print('sucursal 4= ',ganancia[3])
    print('recaudación total de la empresa =',sum(ganancia))
    sucursal_mg=ganancia.index(max(ganancia))
    print('sucursal con mayor ganancia = ',sucursal_mg+1)

##############################################
if NP==15:
    equipos=[]
    goles=[]
    quiniela1=[]
    quiniela2=[]
    quiniela3=[]
    ganador_total=[]
    repeticion=1
    n_e=0
    
    while repeticion<9:
        print('----------------PRIEMRA FASE------------------')
        print('PARTIDO',repeticion)
        equipo1=input('ingres el nombre del equipo 1 = ')
        goles1=int(input('ingrese el numero de goles de dicho equipo'))
       
        equipos.append(equipo1)
        goles.append(goles1)
        
        equipo2=input('ingres el nombre del equipo 2 del partido = ')
        goles2=int(input('ingrese el numero de goles de dicho equipo = '))
        
        equipos.append(equipo2)
        goles.append(goles2)
        
        ganador=goles.index(max(goles))
        quiniela1.append(equipos[ganador])
        equipos.clear()
        
        repeticion=repeticion+1
    print('---------------------------------------------------')
    print('EQUIPOS QUE PASAN DE LA PRIMERA FASE:', quiniela1)
    repeticion=1
    while repeticion<5:
        print('----------------SEGUNDA FASE------------------')
        print('PARTIDO',repeticion)
        goles1=int(input(f'{quiniela1[n_e]},numero de goles= '))
        
        equipos.append(quiniela1[n_e])
        goles.append(goles1)
        n_e=n_e+1
        goles2=int(input(f'{quiniela1[n_e]},numero de goles= '))
        equipos.append(quiniela1[n_e])
        goles.append(goles2)
        n_e=n_e+1
        
        equipos.append(equipo2)
        goles.append(goles2)
        ganador=goles.index(max(goles))
        quiniela2.append(equipos[ganador])
        equipos.clear()
        
        repeticion=repeticion+1
    
    print('---------------------------------------------------')
    print('EQUIPOS QUE PASAN DE LA SEGUNDA FASE:', quiniela2)
    repeticion=1
    n_e=0
    while repeticion<3:
        print('----------------SEMIFINAL------------------')
        print('PARTIDO',repeticion)
        goles1=int(input(f'{quiniela2[n_e]},numero de goles= '))
        
        equipos.append(quiniela1[n_e])
        goles.append(goles1)
        n_e=n_e+1
        goles2=int(input(f'{quiniela2[n_e]},numero de goles= '))
        equipos.append(quiniela2[n_e])
        goles.append(goles2)
        n_e=n_e+1
        
        equipos.append(equipo2)
        goles.append(goles2)
        ganador=goles.index(max(goles))
        quiniela3.append(equipos[ganador])
        equipos.clear()
        
        repeticion=repeticion+1
    n_e=0
    print('---------------------------------------------------')
    print('EQUIPOS QUE PASAN DE LA SIMIFINAL:', quiniela3)
    print('----------------FINAL------------------')
    print('PARTIDO',repeticion)
    goles1=int(input(f'{quiniela3[n_e]},numero de goles= '))
    
    equipos.append(quiniela3[n_e])
    goles.append(goles1)
    n_e=n_e+1
    goles2=int(input(f'{quiniela3[n_e]},numero de goles= '))
    equipos.append(quiniela3[n_e])
    goles.append(goles2)
    n_e=n_e+1
    
    equipos.append(equipo2)
    goles.append(goles2)
    ganador=goles.index(max(goles))
    ganador_total.append(equipos[ganador])
    print('######################################################')
    print('GANADOR = ',ganador_total)

##############################################
if NP==16:
    lista=['.',0,0,0,0,0,0,0,0,0]
    print('lista = ',lista[1::])
    numero=int(input('ingrese un numero para agregar al final de la lista = '))
    lista.append(numero)
    print(lista[1::])
    nuevoN=int(input('ingrese un nuevo numero para agregar = '))
    posicion=int(input('y la posision para agregarlo (desde el uno hacia adelante)= '))
    lista[posicion]=nuevoN
    print(lista[1::])
    print('longitud de la lista = ',len(lista))
    lista.remove(lista[-1])
    print('lista sin el ultimo valor = ',lista[1::])
    borrar=int(input('ingrese una posicion para borrarla = '))
    lista.remove(lista[borrar])
    print(lista[1::])
    valor_a_c=int(input('ingrese un valor a contar = '))
    cuenta=lista.count(valor_a_c)
    print('el valor',valor_a_c,'se repite',cuenta,'vece(s)')

##############################################
if NP==17:
    valores=[]
    
    while True:
        
        valor=(input('ingrese valor = '))
        if(valor.isdigit()):
            valores.append(valor)
        else:
            for x in valores:
                y=valores.count(x)
                if y>1:
                    valores.remove(x)
                
            print('Se borran todos los numero repetidos, menos el ultimo')
            print(valores)
            break

##############################################
if NP==18:
    palabras=[]
    palabrasB=[]
    a=True
    
    while a:
        palabra=input('ingrese una palabra, ingrese un numero cuando desee parar\n')
        if palabra.isdigit():
            a=False
        else:
            palabras.append(palabra)
    
    print(palabras)
    switch=input('ingrese la palabra que desea cambiar = ')
    salida=input('ingrese la palabra por la cual la desea cambiar = ')
    
    for x in palabras:
        if x==switch:
            y=palabras.index(x)
            palabras[y]=salida
    
    print(palabras)
    
    borrar=input('ingrese la palabra que desea borrar de la lista = ')
    
    for z in palabras:
        if z != borrar:
            palabrasB.append(z)
        
    print(palabrasB)
##############################################
if 0>=NP or NP>18:
    print('ingrese el numero de un ejercicio valido')